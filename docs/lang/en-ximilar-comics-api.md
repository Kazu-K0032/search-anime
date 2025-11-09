# Ximilar Comics API Token Registration Guide

[日本語](../XIMILAR_COMICS_API.md) | English

Setup instructions for using the Ximilar Comics API to identify comic works from images.

## 1. Overview of Ximilar Comics API

Ximilar Comics API is an image recognition API that identifies comic work information from comic cover images. It can retrieve detailed information such as work name, title, publication date, issue number, publisher, etc.

**Note**: The free plan only provides access to the basic Collectibles Recognition API (the `/collectibles/v2/analyze` endpoint). For more detailed information, consider using a paid plan.

## 2. Create Ximilar Account

1. Access the [Ximilar App](https://app.ximilar.com/)
2. Click the "Sign Up" or "Register" link
3. Enter the required information to create an account:
   - Email address
   - Password
   - Other necessary information

## 3. Get API Token

1. After creating an account, log in to the [Ximilar App](https://app.ximilar.com/)
2. Navigate to the dashboard or settings page
3. Check or generate the API Token
4. If the token is not displayed, check the API section or settings page

**Note**: Using the Ximilar Comics API may require a paid subscription plan. Please check the official website for details.

## 4. Configure API Token

Set the obtained API token in the project's `.env` file:

```bash
# Create .env file (or edit if it already exists)
cp .env.example .env
```

Write the following in the `.env` file:

```
XIMILAR_API_TOKEN=your_api_token_here
```

Replace `your_api_token_here` with the actual API token you obtained.

## 5. API Usage

### 5.1 Search Using Image File

Search using a local image file:

```bash
python ximilar_comics_cli.py /path/to/image.jpg
```

### 5.2 API Response Format

The API response is returned in JSON format and includes the following information:

```json
{
  "records": [
    {
      "_objects": [
        {
          "_identification": {
            "best_match": {
              "name": "Work Name",
              "title": "Title",
              "date": "Publication Date",
              "number": "Issue Number",
              "publisher": "Publisher",
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

## 6. Notes

- API tokens are confidential information. Be careful not to commit them to Git repositories (the `.env` file is included in `.gitignore`)
- Using the Ximilar Comics API may require a paid subscription plan
- Do not share your API token with others
- For API usage limits and pricing, please check the official website
- For the latest information and details on API usage, please refer to the official documentation

## 7. Reference Links

- [Ximilar App](https://app.ximilar.com/)
- [Ximilar Official Website](https://www.ximilar.com/)
- [Ximilar Comics API Documentation](https://docs.ximilar.com/collectibles/recognition)
