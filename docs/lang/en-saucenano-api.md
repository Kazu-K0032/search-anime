# SauceNAO API Key Registration Guide

[日本語](../SAUCENAO_API.md) | English

To use the SauceNAO API, you need to obtain an API key. Please follow the steps below to get your API key.

## 1. Create a SauceNAO Account

1. Visit the [SauceNAO official website](https://saucenao.com/)
2. Click the "Register" or "Sign Up" link in the top right corner of the site
3. Enter the required information to create an account:
   - Username
   - Email address
   - Password

## 2. Verify Email Address

1. A confirmation email will be sent to the email address you entered during registration
2. Click the link in the email to activate your account

## 3. Log In

1. Once your account is activated, log in to the [SauceNAO official website](https://saucenao.com/)

## 4. Get API Key

1. After logging in, access the [user page](https://saucenao.com/user.php)
2. Check the API key displayed on the user page
3. If the API key is not displayed, check the "API Key" section on the page

## 5. Configure API Key

Set the obtained API key in the project's `.env` file:

```bash
# Create .env file
cp .env.example .env
```

Write the following in the `.env` file:

```
SAUCENAO_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with the actual API key you obtained.

## Notes

- API keys are confidential information. Be careful not to commit them to Git repositories (the `.env` file is included in `.gitignore`)
- API keys can be obtained even on the free plan, but usage limits may apply
- Do not share your API key with others

## Reference Links

- [SauceNAO Official Website](https://saucenao.com/)
- [SauceNAO User Page](https://saucenao.com/user.php)
- [SauceNAO API Documentation](https://saucenao.com/user.php?page=search-api)
