# Search-Anime

[日本語](../../README.md) | English

## Repository Setup

### 1. Clone the Repository

```bash
git clone <repository>
cd search-anime
```

### 2. Create and Activate Virtual Environment

```bash
# Linux (if needed)
sudo apt update && sudo apt install -y python3.12-venv

# Create Python virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
# Create .env file
cp env.example .env
```

## Usage

### SauceNAO CLI

A CLI tool to identify anime and manga works from image files.

```bash
python saucenao_cli.py <image_file_path>
```

#### Usage Example

```bash
# Search by specifying an image file
python saucenao_cli.py /path/to/image.jpg

# Search results will be displayed
# Information such as work name, similarity, URL, etc. will be shown
```

#### Output Example

```
Search Results (3 items):

==================================================

[1]
Title: Work Name
Similarity: 95.5%
URL: https://example.com
Author: Author Name
--------------------------------------------------

[2]
Title: Another Work Name
Similarity: 87.2%
URL: https://example2.com
--------------------------------------------------

==================================================
```

### trace.moe CLI

A CLI tool to identify anime works from image files. Specialized for anime scene search, it can also retrieve episode information and scene timing information.

```bash
python tracemoe_cli.py <image_file_path>
```

#### Usage Example

```bash
# Search by specifying an image file
python tracemoe_cli.py /path/to/image.jpg

# Search results will be displayed
# Information such as work name, episode, similarity, scene timing, video URL, etc. will be shown
```

#### Output Example

```
Search Results (3 items):

==================================================

[1]
Title: Anime Title
Similarity: 95.00%
Episode: 1
Scene Time: 00:12 - 00:15
Video URL: https://media.trace.moe/video/...
Image URL: https://media.trace.moe/image/...
AniList ID: 12345
--------------------------------------------------

[2]
Title: Another Anime Title
Similarity: 87.20%
Episode: 5
Scene Time: 01:23 - 01:26
Video URL: https://media.trace.moe/video/...
--------------------------------------------------

==================================================
```

### Ximilar Comics CLI

A CLI tool to identify comic works from image files. Uses the Ximilar Comics API to retrieve detailed information such as work name, title, publication date, issue number, publisher, etc.

```bash
python ximilar_comics_cli.py <image_file_path>
```

#### Usage Example

```bash
# Search by specifying an image file
python ximilar_comics_cli.py /path/to/image.jpg

# Search results will be displayed
# Information such as work name, title, similarity, publisher, publication date, issue number, etc. will be shown
```

#### Output Example

```
Search Results (top 3 / total 5):

==================================================

[1]
Title: Work Name
Title: Title
Similarity: 95.00%
Publisher: Publisher Name
Publication Date: January 2024
Issue Number: 1
--------------------------------------------------

[2]
Title: Another Work Name
Title: Another Title
Similarity: 87.20%
Publisher: Another Publisher
--------------------------------------------------

==================================================
```

**Note**: Using the Ximilar Comics API requires an API token. See the [Ximilar Comics API documentation](./en-ximilar-comics-api.md) for details.
