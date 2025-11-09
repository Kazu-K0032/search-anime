"""漫画検索リポジトリインターフェース"""
from abc import ABC, abstractmethod
from typing import List
from ..entities.comic_result import ComicResult


class ComicSearchRepository(ABC):
    """漫画検索リポジトリのインターフェース"""
    
    @abstractmethod
    def search(self, image_path: str) -> List[ComicResult]:
        """
        画像ファイルから漫画を検索する
        
        Args:
            image_path: 検索対象の画像ファイルパス
            
        Returns:
            検索結果のリスト
            
        Raises:
            FileNotFoundError: 画像ファイルが存在しない場合
            Exception: API呼び出しエラーなど
        """
        pass

