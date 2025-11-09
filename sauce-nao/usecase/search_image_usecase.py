"""画像検索ユースケース"""
from typing import List
from ..domain.entities.search_result import SearchResult
from ..domain.repositories.image_search_repository import ImageSearchRepository


class SearchImageUseCase:
    """画像検索を実行するユースケース"""
    
    def __init__(self, repository: ImageSearchRepository):
        """
        初期化
        
        Args:
            repository: 画像検索リポジトリ
        """
        self.repository = repository
    
    def execute(self, image_path: str) -> List[SearchResult]:
        """
        画像検索を実行する
        
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

