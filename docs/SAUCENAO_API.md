# SauceNAO API キー発行手順

[English](./lang/en-saucenano-api.md) | 日本語

SauceNAO API を使用するには、API キーの取得が必要です。以下の手順に従って API キーを取得してください。

## 1. SauceNAO アカウントの作成

1. [SauceNAO 公式サイト](https://saucenao.com/)にアクセスします
2. サイト右上の「Register」または「Sign Up」リンクをクリックします
3. 必要な情報を入力してアカウントを作成します：
   - ユーザー名
   - メールアドレス
   - パスワード

## 2. メールアドレスの確認

1. 登録時に入力したメールアドレスに確認メールが送信されます
2. メール内のリンクをクリックしてアカウントを有効化してください

## 3. ログイン

1. アカウントが有効化されたら、[SauceNAO 公式サイト](https://saucenao.com/)にログインします

## 4. API キーの取得

1. ログイン後、[ユーザーページ](https://saucenao.com/user.php)にアクセスします
2. ユーザーページに表示されている API キーを確認します
3. API キーが表示されていない場合は、ページ内の「API Key」セクションを確認してください

## 5. API キーの設定

取得した API キーをプロジェクトの`.env`ファイルに設定します：

```bash
# .envファイルを作成
cp .env.example .env
```

`.env`ファイルに以下を記述します：

```
SAUCENAO_API_KEY=your_api_key_here
```

`your_api_key_here`の部分を、実際に取得した API キーに置き換えてください。

## 注意事項

- API キーは機密情報です。Git リポジトリにコミットしないよう注意してください（`.env`ファイルは`.gitignore`に含まれています）
- 無料プランでも API キーは取得可能ですが、使用制限がある場合があります
- API キーを他人に共有しないでください

## 参考リンク

- [SauceNAO 公式サイト](https://saucenao.com/)
- [SauceNAO ユーザーページ](https://saucenao.com/user.php)
- [SauceNAO API ドキュメント](https://saucenao.com/user.php?page=search-api)
