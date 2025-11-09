"""アニメ検索ユースケース"""
from typing import List
from ..domain.entities.anime_result import AnimeResult
from ..domain.repositories.anime_search_repository import AnimeSearchRepository


class SearchAnimeUseCase:
    """アニメ検索を実行するユースケース"""
    
    def __init__(self, repository: AnimeSearchRepository):
        """
        初期化
        
        Args:
            repository: アニメ検索リポジトリ
        """
        self.repository = repository
    
    def execute(self, image_path: str) -> List[AnimeResult]:
        """
        アニメ検索を実行する
        
        Args:
            image_path: 検索対象の画像ファイルパス
            
        Returns:
            検索結果のリスト（類似度の高い順）
            
        Raises:
            FileNotFoundError: 画像ファイルが存在しない場合
            Exception: API呼び出しエラーなど
        """
        results = self.repository.search(image_path)
        # 類似度の高い順にソート
        return sorted(results, key=lambda x: x.similarity, reverse=True)

