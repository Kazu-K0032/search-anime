# Search-Anime

[English](./docs/lang/en.md) | 日本語

## リポジトリのセットアップ

### 1. リポジトリのクローン

```bash
git clone <repository>
cd search-anime
```

### 2. 仮想環境の作成とアクティベート

```bash
# Linux(必要に応じて)
sudo apt update && sudo apt install -y python3.12-venv

# Python仮想環境を作成
python3 -m venv venv

# 仮想環境をアクティベート
source venv/bin/activate
```

### 3. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 4. 環境変数の設定

```bash
# .envファイルを作成
cp env.example .env
```

## 利用

### SauceNAO CLI

画像ファイルからアニメ・漫画作品を特定する CLI ツールです。

```bash
python saucenao_cli.py <画像ファイルパス>
```

#### 使用例

```bash
# 画像ファイルを指定して検索
python saucenao_cli.py /path/to/image.jpg

# 検索結果が表示されます
# 作品名、類似度、URLなどの情報が表示されます
```

#### 出力例

```
検索結果 (3件):

==================================================

[1]
作品名: 作品名
類似度: 95.5%
URL: https://example.com
作者: 作者名
--------------------------------------------------

[2]
作品名: 別の作品名
類似度: 87.2%
URL: https://example2.com
--------------------------------------------------

==================================================
```

### trace.moe CLI

画像ファイルからアニメ作品を特定する CLI ツールです。アニメシーン検索に特化しており、エピソード情報やシーン時刻情報も取得できます。

```bash
python tracemoe_cli.py <画像ファイルパス>
```

#### 使用例

```bash
# 画像ファイルを指定して検索
python tracemoe_cli.py /path/to/image.jpg

# 検索結果が表示されます
# 作品名、エピソード、類似度、シーン時刻、動画URLなどの情報が表示されます
```

#### 出力例

```
検索結果 (3件):

==================================================

[1]
作品名: アニメタイトル
類似度: 95.00%
エピソード: 1
シーン時刻: 00:12 - 00:15
動画URL: https://media.trace.moe/video/...
画像URL: https://media.trace.moe/image/...
AniList ID: 12345
--------------------------------------------------

[2]
作品名: 別のアニメタイトル
類似度: 87.20%
エピソード: 5
シーン時刻: 01:23 - 01:26
動画URL: https://media.trace.moe/video/...
--------------------------------------------------

==================================================
```
