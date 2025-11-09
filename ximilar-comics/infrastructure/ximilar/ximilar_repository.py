"""Ximilar Comics APIリポジトリ実装"""
import os
import base64
from typing import List
import requests
from dotenv import load_dotenv
from ...domain.entities.comic_result import ComicResult
from ...domain.repositories.comic_search_repository import ComicSearchRepository


class XimilarRepository(ComicSearchRepository):
    """Ximilar Comics APIを使用した漫画検索リポジトリの実装"""
    
    API_URL = "https://api.ximilar.com/collectibles/v2/analyze"
    
    def __init__(self):
        """初期化（環境変数からAPIトークンを読み込み）"""
        load_dotenv()
        self.api_token = os.getenv("XIMILAR_API_TOKEN")
        
        if not self.api_token:
            raise ValueError(
                "XIMILAR_API_TOKENが環境変数に設定されていません。"
                ".envファイルにXIMILAR_API_TOKENを設定してください。"
            )
    
    def search(self, image_path: str) -> List[ComicResult]:
        """
        画像ファイルをXimilar Comics APIで検索する
        
        Args:
            image_path: 検索対象の画像ファイルパス
            
        Returns:
            検索結果のリスト
            
        Raises:
            FileNotFoundError: 画像ファイルが存在しない場合
            requests.RequestException: API呼び出しエラー
            ValueError: APIレスポンスが不正な場合
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")
        
        try:
            # 画像をbase64エンコード
            with open(image_path, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode("utf-8")
            
            # APIリクエストの準備
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Token {self.api_token}"
            }
            
            data = {
                "records": [
                    {
                        "_base64": image_data
                    }
                ]
            }
            
            response = requests.post(
                self.API_URL,
                headers=headers,
                json=data,
                timeout=30
            )
            
            # 401エラーの場合は詳細なエラーメッセージを表示
            if response.status_code == 401:
                error_detail = ""
                try:
                    error_response = response.json()
                    if "detail" in error_response:
                        error_detail = f"\nエラー詳細: {error_response['detail']}"
                    elif "message" in error_response:
                        error_detail = f"\nエラー詳細: {error_response['message']}"
                    elif "error" in error_response:
                        error_detail = f"\nエラー詳細: {error_response['error']}"
                    else:
                        error_detail = f"\nレスポンス内容: {error_response}"
                except:
                    error_detail = f"\nレスポンス本文: {response.text[:500]}"
                
                # デバッグ情報（開発時のみ）
                debug_info = f"\n\nデバッグ情報:\n"
                debug_info += f"- エンドポイント: {self.API_URL}\n"
                debug_info += f"- 認証ヘッダー: Authorization: Token {self.api_token[:10]}...\n"
                debug_info += f"- ステータスコード: {response.status_code}\n"
                debug_info += f"- レスポンスヘッダー: {dict(response.headers)}"
                
                raise Exception(
                    f"Ximilar Comics API認証エラー (401 UNAUTHORIZED):\n"
                    f"APIトークンが無効、期限切れ、または権限が不足しています。{error_detail}\n"
                    f"以下を確認してください：\n"
                    f"1. .envファイルにXIMILAR_API_TOKENが正しく設定されているか\n"
                    f"2. APIトークンが有効期限内であるか\n"
                    f"3. APIトークンにComics APIへのアクセス権限があるか\n"
                    f"4. Ximilarアプリ（https://app.ximilar.com/）でAPIトークンを再確認してください{debug_info}"
                )
            
            response.raise_for_status()
            
            result_data = response.json()
            return self._parse_response(result_data)
        
        except requests.RequestException as e:
            # 401エラーの場合は既に詳細なメッセージを表示しているので、そのまま再スロー
            if "401" in str(e) or "UNAUTHORIZED" in str(e):
                raise
            raise Exception(f"Ximilar Comics API呼び出しエラー: {str(e)}")
    
    def _parse_response(self, data: dict) -> List[ComicResult]:
        """
        APIレスポンスをパースしてComicResultリストに変換
        
        Args:
            data: APIレスポンスのJSONデータ
            
        Returns:
            検索結果のリスト
        """
        results = []
        
        if "records" not in data or not data["records"]:
            return results
        
        for record in data["records"]:
            # analyzeエンドポイントのレスポンス形式に対応
            if "_objects" not in record or not record["_objects"]:
                continue
            
            for obj in record["_objects"]:
                # 類似度スコアを取得
                similarity = None
                if "_score" in obj:
                    similarity = float(obj["_score"])
                
                # 識別情報を取得
                identification = obj.get("_identification", {})
                
                # best_matchがある場合
                if "best_match" in identification:
                    best_match = identification["best_match"]
                    
                    # 作品名を取得
                    name = best_match.get("name") or best_match.get("title") or "不明"
                    
                    # その他の情報を取得
                    title = best_match.get("title")
                    date = best_match.get("date") or best_match.get("year")
                    number = best_match.get("number") or best_match.get("issue_number")
                    publisher = best_match.get("publisher")
                    url = best_match.get("url")
                    
                    result = ComicResult(
                        name=name,
                        title=title,
                        similarity=similarity,
                        date=date,
                        number=number,
                        publisher=publisher,
                        url=url
                    )
                    
                    results.append(result)
                else:
                    # best_matchがない場合でも、基本的な情報があれば結果を作成
                    name = obj.get("name") or obj.get("subcategory") or "不明"
                    
                    result = ComicResult(
                        name=name,
                        title=obj.get("title"),
                        similarity=similarity,
                        date=obj.get("date") or obj.get("year"),
                        number=obj.get("number") or obj.get("issue_number"),
                        publisher=obj.get("publisher"),
                        url=obj.get("url")
                    )
                    
                    results.append(result)
        
        return results

