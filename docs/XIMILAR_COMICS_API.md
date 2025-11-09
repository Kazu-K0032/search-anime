# Ximilar Comics API トークン発行手順

[English](./lang/en-ximilar-comics-api.md) | 日本語

Ximilar Comics API を使用して画像から漫画作品を特定する機能を利用するための設定手順です。

## 1. Ximilar Comics API の概要

Ximilar Comics API は、漫画の表紙画像から作品情報を特定するための画像認識 API です。作品名、タイトル、発行日、号数、出版社などの詳細な情報を取得できます。

**注意**: 無料プランでは、基本的な Collectibles Recognition API（`/collectibles/v2/analyze`エンドポイント）のみ利用可能です。より詳細な情報が必要な場合は、有料プランの利用を検討してください。

## 2. Ximilar アカウントの作成

1. [Ximilar アプリ](https://app.ximilar.com/)にアクセスします
2. 「Sign Up」または「登録」リンクをクリックします
3. 必要な情報を入力してアカウントを作成します：
   - メールアドレス
   - パスワード
   - その他の必要情報

## 3. API トークンの取得

1. アカウント作成後、[Ximilar アプリ](https://app.ximilar.com/)にログインします
2. ダッシュボードまたは設定ページに移動します
3. API トークン（API Token）を確認または生成します
4. トークンが表示されていない場合は、API セクションまたは設定ページを確認してください

**注意**: Ximilar Comics API の利用には、有料サブスクリプションプランが必要な場合があります。詳細は公式サイトを確認してください。

## 4. API トークンの設定

取得した API トークンをプロジェクトの`.env`ファイルに設定します：

```bash
# .envファイルを作成（既に存在する場合は編集）
cp .env.example .env
```

`.env`ファイルに以下を記述します：

```
XIMILAR_API_TOKEN=your_api_token_here
```

`your_api_token_here`の部分を、実際に取得した API トークンに置き換えてください。

## 5. API の使用方法

### 5.1 画像ファイルを使用した検索

ローカルの画像ファイルを使用して検索を行います：

```bash
python ximilar_comics_cli.py /path/to/image.jpg
```

### 5.2 API レスポンスの形式

API からのレスポンスは JSON 形式で返され、以下のような情報が含まれます：

```json
{
  "records": [
    {
      "_objects": [
        {
          "_identification": {
            "best_match": {
              "name": "作品名",
              "title": "タイトル",
              "date": "発行日",
              "number": "号数",
              "publisher": "出版社",
              "url": "URL"
            },
            "_score": 0.95
          }
        }
      ]
    }
  ]
}
```

## 6. 注意事項

- API トークンは機密情報です。Git リポジトリにコミットしないよう注意してください（`.env`ファイルは`.gitignore`に含まれています）
- Ximilar Comics API の利用には、有料サブスクリプションプランが必要な場合があります
- API トークンを他人に共有しないでください
- API の利用制限や料金については、公式サイトを確認してください
- API の利用に関する最新情報や詳細は、公式ドキュメントを参照してください

## 7. 参考リンク

- [Ximilar アプリ](https://app.ximilar.com/)
- [Ximilar 公式サイト](https://www.ximilar.com/)
- [Ximilar Comics API ドキュメント](https://docs.ximilar.com/collectibles/recognition)
