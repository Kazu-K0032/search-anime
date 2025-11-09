"""trace.moe APIリポジトリ実装"""
import os
from typing import List
import requests
from dotenv import load_dotenv
from ...domain.entities.anime_result import AnimeResult
from ...domain.repositories.anime_search_repository import AnimeSearchRepository


class TraceMoeRepository(AnimeSearchRepository):
    """trace.moe APIを使用したアニメ検索リポジトリの実装"""
    
    API_URL = "https://api.trace.moe/search"
    
    def __init__(self):
        """初期化（環境変数からAPIキーを読み込み、オプション）"""
        load_dotenv()
        self.api_key = os.getenv("TRACE_MOE_API_KEY")
        # APIキーはオプション（無料でも利用可能だが制限あり）
    
    def search(self, image_path: str) -> List[AnimeResult]:
        """
        画像ファイルをtrace.moe APIで検索する
        
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
                files = {"image": image_file}
                params = {
                    "anilistInfo": 1,  # AniList情報を含める
                }
                
                # APIキーが設定されている場合は追加
                if self.api_key:
                    params["api_key"] = self.api_key
                
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
            raise Exception(f"trace.moe API呼び出しエラー: {str(e)}")
    
    def _parse_response(self, data: dict) -> List[AnimeResult]:
        """
        APIレスポンスをパースしてAnimeResultリストに変換
        
        Args:
            data: APIレスポンスのJSONデータ
            
        Returns:
            検索結果のリスト
        """
        results = []
        
        if "result" not in data:
            return results
        
        for result_data in data["result"]:
            similarity = result_data.get("similarity", 0)
            
            # AniList情報を取得
            anilist = result_data.get("anilist", {})
            title_info = anilist.get("title", {})
            
            # タイトルを取得（優先順位: romaji > native > english）
            title = (
                title_info.get("romaji") or
                title_info.get("native") or
                title_info.get("english") or
                "不明"
            )
            
            # エピソード情報
            episode = result_data.get("episode")
            
            # URL情報
            video_url = result_data.get("video")
            image_url = result_data.get("image")
            
            # 時刻情報
            from_time = result_data.get("from")
            to_time = result_data.get("to")
            
            # AniList ID
            anilist_id = anilist.get("id")
            
            result = AnimeResult(
                title=title,
                episode=episode,
                similarity=similarity,
                video_url=video_url,
                image_url=image_url,
                from_time=from_time,
                to_time=to_time,
                anilist_id=anilist_id,
                title_native=title_info.get("native"),
                title_romaji=title_info.get("romaji"),
                title_english=title_info.get("english"),
            )
            
            results.append(result)
        
        return results

