# Getting Started

This document will guide you through the initial usage process of the New API platform.

## 🎯 Prerequisites

- Deployed New API instance (access URL, e.g., https://www.sunthycloud.ai)
- Modern browser (Chrome, Firefox, Edge, etc.)
- Tool for API calls (curl, Postman, or programming language SDK)

## 📝 Step 1: Register Account

### Web Registration
1. Visit your New API instance homepage (e.g., https://www.sunthycloud.ai)
2. Click the "Register" button in the top right corner
3. Fill in registration information:
   - Username (unique identifier)
   - Email address (for verification and password recovery)
   - Password (recommend using a strong password)
4. Click "Submit Registration"
5. Check email to complete verification (if email verification is enabled)

### API Registration (Optional)
```bash
curl -X POST https://www.sunthycloud.ai/api/user/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password",
    "email": "your_email@example.com"
  }'
```

## 🔐 Step 2: Login to System

### Web Login
1. Visit the login page (usually the homepage)
2. Enter username/email and password
3. Click "Login"
4. After successful login, enter the dashboard

### Get Access Token (for API authentication)
```bash
curl -X POST https://www.sunthycloud.ai/api/user/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```

Response example:
```json
{
  "code": 200,
  "message": "Login successful",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": 1,
      "username": "your_username",
      "role": "user"
    }
  }
}
```

## 🔑 Step 3: Get API Key

### Create Token via Dashboard
1. After login, click "Token Management" in the left menu
2. Click the "New Token" button
3. Configure token parameters:
   - **Token Name**: Easy-to-identify name (e.g., "Production API Key")
   - **Model Permissions**: Select AI models accessible by this token
   - **Quota Limit**: Set usage quota (optional)
   - **Expiration Time**: Set validity period (optional)
4. Click "Create"
5. **Immediately copy the generated API key** (only shown once)

### Create Token via API
```bash
curl -X POST https://www.sunthycloud.ai/api/token \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Production API Key",
    "models": ["gpt-4", "claude-3"],
    "remain_quota": 1000000
  }'
```

The `key` field in the response is the API key.

## 🚀 Step 4: First API Call

### OpenAI Compatible Interface
```bash
curl https://www.sunthycloud.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello, introduce yourself."}
    ],
    "temperature": 0.7,
    "max_tokens": 500
  }'
```

### Claude Messages Format
```bash
curl https://www.sunthycloud.ai/v1/messages \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Hello, Claude!"}
    ]
  }'
```

### Google Gemini Format
```bash
curl https://www.sunthycloud.ai/v1beta/gemini \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.0-flash",
    "contents": [
      {"parts": [{"text": "Hello, Gemini!"}]}
    ]
  }'
```

## 📊 Step 5: Check Usage

### Dashboard View
1. Go to "Statistics" page to view usage charts
2. Check remaining quota in "Token Management"
3. Use "Logs" feature to view API call history

### API Query Usage
```bash
curl https://www.sunthycloud.ai/api/token/usage \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 🔧 Common Configurations

### 1. Environment Variables (Recommended)
```bash
export NEW_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export NEW_API_BASE="https://www.sunthycloud.ai"
```

### 2. Python SDK Example
```python
import openai

client = openai.OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://www.sunthycloud.ai/v1"
)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)
print(response.choices[0].message.content)
```

### 3. JavaScript/Node.js Example
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://www.sunthycloud.ai/v1',
});

const response = await client.chat.completions.create({
  model: 'gpt-4',
  messages: [{ role: 'user', content: 'Hello!' }],
});

console.log(response.choices[0].message.content);
```

## ⚠️ Important Notes

1. **API Key Security**
   - Do not commit API keys to version control systems
   - Use environment variables or key management services
   - Rotate keys regularly

2. **Quota Management**
   - Monitor usage to avoid exceeding limits
   - Set up usage alerts
   - Understand billing strategies

3. **Model Compatibility**
   - Confirm token has access to corresponding models
   - Different interface formats require different request structures
   - Check supported model list

## 🆘 Having Problems?

- Check network connection and API address
- Verify API key is correct
- Confirm token has sufficient quota and correct model permissions
- Check error logs for detailed information

---

**Next Step**: [Dashboard Usage →](./dashboard.md) | [Back to Home](./index.md)
