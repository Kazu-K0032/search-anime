# trace.moe API 使用方法

[English](./lang/en-tracemoe-api.md) | 日本語

trace.moe API を使用して画像からアニメ作品を特定する機能を利用するための設定手順です。

## 1. trace.moe API の概要

trace.moe は、アニメのスクリーンショットから作品名やエピソード情報を特定するための画像検索 API です。アニメシーン検索に特化しており、エピソード情報やシーン時刻情報も取得できます。

**重要**: trace.moe API は **API キーなしで利用可能** です。パブリック API として無料で利用できますが、利用制限があります。

## 2. セットアップ

### 2.1 環境変数の設定（不要）

trace.moe API は API キーなしで利用可能なため、環境変数の設定は **不要** です。

ただし、セルフホスティングや高頻度利用のために API キーを取得した場合は、`.env`ファイルに設定できます：

```
TRACE_MOE_API_KEY=your_api_key_here
```

### 2.2 パブリック API の利用制限

パブリック API には以下のような制限があります：

- リクエスト数の制限
- レート制限
- 商用利用の制限

詳細は公式ドキュメントを確認してください。

## 3. API の使用方法

### 3.1 画像ファイルを使用した検索

ローカルの画像ファイルを使用して検索を行います：

```bash
python tracemoe_cli.py /path/to/image.jpg
```

### 3.2 API レスポンスの形式

API からのレスポンスは JSON 形式で返され、以下のような情報が含まれます：

```json
{
  "result": [
    {
      "anilist": {
        "id": 12345,
        "title": {
          "romaji": "Anime Title",
          "native": "アニメタイトル",
          "english": "Anime Title"
        }
      },
      "episode": 1,
      "from": 12.34,
      "to": 15.67,
      "similarity": 0.95,
      "video": "https://media.trace.moe/video/...",
      "image": "https://media.trace.moe/image/..."
    }
  ]
}
```

## 4. 注意事項

- trace.moe API は API キーなしで利用可能です
- パブリック API は利用制限があります。高頻度の利用や商用利用を検討している場合は、セルフホスティングを検討してください
- API の利用に関する最新情報や詳細は、公式ドキュメントを参照してください

## 5. 参考リンク

- [trace.moe API 公式ドキュメント](https://soruly.github.io/trace.moe-api/#/)
- [trace.moe GitHub リポジトリ](https://github.com/soruly/trace.moe)
- [trace.moe 公式サイト](https://trace.moe/)
