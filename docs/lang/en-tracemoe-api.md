# trace.moe API Usage Guide

[日本語](../TRACE_MOE_API.md) | English

Setup instructions for using the trace.moe API to identify anime works from images.

## 1. Overview of trace.moe API

trace.moe is an image search API that identifies anime work names and episode information from anime screenshots. It specializes in anime scene search and can also retrieve episode information and scene timing information.

**Important**: trace.moe API can be used **without an API key**. It is available as a free public API, but with usage limitations.

## 2. Setup

### 2.1 Environment Variable Configuration (Not Required)

trace.moe API can be used without an API key, so environment variable configuration is **not required**.

However, if you have obtained an API key for self-hosting or high-frequency use, you can set it in the `.env` file:

```
TRACE_MOE_API_KEY=your_api_key_here
```

### 2.2 Public API Usage Limitations

The public API has the following limitations:

- Request number limits
- Rate limiting
- Commercial use restrictions

Please check the official documentation for details.

## 3. API Usage

### 3.1 Search Using Image File

Search using a local image file:

```bash
python tracemoe_cli.py /path/to/image.jpg
```

### 3.2 API Response Format

The API response is returned in JSON format and includes the following information:

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

## 4. Notes

- trace.moe API can be used without an API key
- The public API has usage limitations. If you are considering high-frequency use or commercial use, consider self-hosting
- For the latest information and details on API usage, please refer to the official documentation

## 5. Reference Links

- [trace.moe API Official Documentation](https://soruly.github.io/trace.moe-api/#/)
- [trace.moe GitHub Repository](https://github.com/soruly/trace.moe)
- [trace.moe Official Website](https://trace.moe/)
