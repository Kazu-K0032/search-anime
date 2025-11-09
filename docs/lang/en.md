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
