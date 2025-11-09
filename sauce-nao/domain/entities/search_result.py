"""検索結果エンティティ"""
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class SearchResult:
    """SauceNAO検索結果を表現するエンティティ"""
    title: str
    similarity: float
    url: Optional[str]
    author: Optional[str] = None
    material: Optional[str] = None
    characters: Optional[str] = None
    source: Optional[str] = None
    ext_urls: Optional[List[str]] = None

    def __str__(self) -> str:
        """コンソール出力用の文字列表現"""
        lines = [
            f"作品名: {self.title}",
            f"類似度: {self.similarity}%",
        ]
        
        if self.url:
            lines.append(f"URL: {self.url}")
        
        if self.author:
            lines.append(f"作者: {self.author}")
        
        if self.material:
            lines.append(f"素材: {self.material}")
        
        if self.characters:
            lines.append(f"キャラクター: {self.characters}")
        
        if self.source:
            lines.append(f"ソース: {self.source}")
        
        return "\n".join(lines)

