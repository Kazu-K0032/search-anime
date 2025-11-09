"""画像検索リポジトリインターフェース"""
from abc import ABC, abstractmethod
from typing import List
from ..entities.search_result import SearchResult


class ImageSearchRepository(ABC):
    """画像検索リポジトリのインターフェース"""
    
    @abstractmethod
    def search(self, image_path: str) -> List[SearchResult]:
        """
        画像ファイルを検索する
        
        Args:
            image_path: 検索対象の画像ファイルパス
            
        Returns:
            検索結果のリスト
            
        Raises:
            FileNotFoundError: 画像ファイルが存在しない場合
            Exception: API呼び出しエラーなど
        """
        pass

