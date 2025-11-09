"""SauceNAO APIリポジトリ実装"""
import os
from typing import List
import requests
from dotenv import load_dotenv
from ...domain.entities.search_result import SearchResult
from ...domain.repositories.image_search_repository import ImageSearchRepository


class SauceNAORepository(ImageSearchRepository):
    """SauceNAO APIを使用した画像検索リポジトリの実装"""
    
    API_URL = "https://saucenao.com/search.php"
    
    def __init__(self):
        """初期化（環境変数からAPIキーを読み込み）"""
        load_dotenv()
        self.api_key = os.getenv("SAUCENAO_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "SAUCENAO_API_KEYが環境変数に設定されていません。"
                ".envファイルにSAUCENAO_API_KEYを設定してください。"
            )
    
    def search(self, image_path: str) -> List[SearchResult]:
        """
        画像ファイルをSauceNAO APIで検索する
        
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
            with open(image_path, "rb") as image_file:
                files = {"file": image_file}
                params = {
                    "api_key": self.api_key,
                    "output_type": 2,  # JSON形式
                    "numres": 5,  # 最大5件の結果を取得
                }
                
                response = requests.post(
                    self.API_URL,
                    files=files,
                    params=params,
                    timeout=30
                )
                response.raise_for_status()
                
                data = response.json()
                return self._parse_response(data)
        
        except requests.RequestException as e:
            raise Exception(f"SauceNAO API呼び出しエラー: {str(e)}")
    
    def _parse_response(self, data: dict) -> List[SearchResult]:
        """
        APIレスポンスをパースしてSearchResultリストに変換
        
        Args:
            data: APIレスポンスのJSONデータ
            
        Returns:
            検索結果のリスト
        """
        results = []
        
        if "results" not in data:
            return results
        
        for result_data in data["results"]:
            header = result_data.get("header", {})
            data_fields = result_data.get("data", {})
            
            similarity = float(header.get("similarity", 0))
            
            # 作品名を取得（複数のフィールドから取得を試みる）
            title = (
                data_fields.get("title") or
                data_fields.get("source") or
                data_fields.get("eng_name") or
                data_fields.get("jp_name") or
                "不明"
            )
            
            # URLを取得
            ext_urls = data_fields.get("ext_urls", [])
            url = ext_urls[0] if ext_urls else None
            
            # その他のメタデータ
            author = data_fields.get("creator") or data_fields.get("author")
            material = data_fields.get("material")
            characters = data_fields.get("characters")
            source = data_fields.get("source")
            
            result = SearchResult(
                title=title,
                similarity=similarity,
                url=url,
                author=author,
                material=material,
                characters=characters,
                source=source,
                ext_urls=ext_urls
            )
            
            results.append(result)
        
        return results

