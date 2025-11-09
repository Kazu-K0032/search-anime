"""アニメ検索結果エンティティ"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class AnimeResult:
    """trace.moe検索結果を表現するエンティティ"""
    title: str
    episode: Optional[int]
    similarity: float
    video_url: Optional[str]
    image_url: Optional[str]
    from_time: Optional[float] = None  # シーン開始時刻（秒）
    to_time: Optional[float] = None    # シーン終了時刻（秒）
    anilist_id: Optional[int] = None   # AniList ID
    title_native: Optional[str] = None  # 日本語タイトル
    title_romaji: Optional[str] = None  # ローマ字タイトル
    title_english: Optional[str] = None  # 英語タイトル

    def __str__(self) -> str:
        """コンソール出力用の文字列表現"""
        lines = [
            f"作品名: {self.title}",
            f"類似度: {self.similarity:.2%}",
        ]
        
        if self.episode is not None:
            lines.append(f"エピソード: {self.episode}")
        
        # シーン時刻は参考情報として簡潔に表示
        if self.from_time is not None:
            from_min = int(self.from_time // 60)
            from_sec = int(self.from_time % 60)
            lines.append(f"該当シーン: {from_min:02d}:{from_sec:02d}付近")
        
        if self.video_url:
            lines.append(f"動画URL: {self.video_url}")
        
        if self.image_url:
            lines.append(f"画像URL: {self.image_url}")
        
        if self.anilist_id:
            lines.append(f"AniList ID: {self.anilist_id}")
        
        return "\n".join(lines)

