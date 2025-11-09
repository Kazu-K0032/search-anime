"""漫画検索結果エンティティ"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class ComicResult:
    """Ximilar Comics検索結果を表現するエンティティ"""
    name: str  # 作品名
    title: Optional[str] = None  # タイトル
    similarity: Optional[float] = None  # 類似度スコア
    date: Optional[str] = None  # 発行日
    number: Optional[str] = None  # 号数
    publisher: Optional[str] = None  # 出版社
    url: Optional[str] = None  # URL

    def __str__(self) -> str:
        """コンソール出力用の文字列表現"""
        lines = [
            f"作品名: {self.name}",
        ]
        
        if self.title:
            lines.append(f"タイトル: {self.title}")
        
        if self.similarity is not None:
            lines.append(f"類似度: {self.similarity:.2%}")
        
        if self.publisher:
            lines.append(f"出版社: {self.publisher}")
        
        if self.date:
            lines.append(f"発行日: {self.date}")
        
        if self.number:
            lines.append(f"号数: {self.number}")
        
        if self.url:
            lines.append(f"URL: {self.url}")
        
        return "\n".join(lines)

