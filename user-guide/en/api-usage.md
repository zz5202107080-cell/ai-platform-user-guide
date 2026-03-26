# API Usage Guide

This document details various API interface formats and calling methods supported by New API.

## 📋 API Basics

### Authentication Method
All API requests need to carry authentication information in the Header:

```bash
Authorization: Bearer YOUR_API_KEY
```

### Base URL
- **OpenAI Compatible Interface**: `https://api.your-domain.com/v1/`
- **Claude Messages Interface**: `https://api.your-domain.com/v1/messages`
- **Google Gemini Interface**: `https://api.your-domain.com/v1beta/gemini`

### Response Format
Default returns JSON format data, containing the following fields:
```json
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-4",
  "choices": [...],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
```

## 🤖 OpenAI Compatible Interface

New API is fully compatible with OpenAI API specifications, supporting the following interfaces:

### 1. Chat Completions
```bash
curl https://api.your-domain.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Write a poem about spring."}
    ],
    "temperature": 0.7,
    "max_tokens": 500,
    "stream": false
  }'
```

#### Streaming Response
```bash
curl https://api.your-domain.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello"}],
    "stream": true
  }'
```

#### Function Calling
```bash
curl https://api.your-domain.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "What's the weather like in Beijing today?"}],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "Get city weather information",
          "parameters": {
            "type": "object",
            "properties": {
              "city": {"type": "string", "description": "City name"}
            },
            "required": ["city"]
          }
        }
      }
    ],
    "tool_choice": "auto"
  }'
```

### 2. Image Generation
```bash
curl https://api.your-domain.com/v1/images/generations \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "dall-e-3",
    "prompt": "A cute cat playing in the garden",
    "n": 1,
    "size": "1024x1024",
    "quality": "standard"
  }'
```

### 3. Speech to Text
```bash
# Upload audio file for transcription
curl https://api.your-domain.com/v1/audio/transcriptions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@audio.mp3" \
  -F "model=whisper-1" \
  -F "response_format=json"
```

### 4. Text to Speech
```bash
curl https://api.your-domain.com/v1/audio/speech \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1",
    "input": "Hello, welcome to New API!",
    "voice": "alloy",
    "response_format": "mp3"
  }' --output speech.mp3
```

### 5. Embeddings
```bash
curl https://api.your-domain.com/v1/embeddings \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-ada-002",
    "input": "The weather is nice today",
    "encoding_format": "float"
  }'
```

### 6. Rerank
```bash
curl https://api.your-domain.com/v1/rerank \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "rerank-english-v2.0",
    "query": "What is artificial intelligence?",
    "documents": [
      "Artificial intelligence is a branch of computer science...",
      "Machine learning is an implementation of artificial intelligence...",
      "Deep learning is a subset of machine learning..."
    ],
    "top_n": 3
  }'
```

## 🎨 Claude Messages Interface

### Basic Messages Interface
```bash
curl https://api.your-domain.com/v1/messages \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Write a short story about friendship."}
    ]
  }'
```

### Streaming Response
```bash
curl https://api.your-domain.com/v1/messages \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Introduce yourself."}
    ],
    "stream": true
  }'
```

### Tool Usage (Tools)
```bash
curl https://api.your-domain.com/v1/messages \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Check the weather in London"}
    ],
    "tools": [
      {
        "name": "get_weather",
        "description": "Get city weather information",
        "input_schema": {
          "type": "object",
          "properties": {
            "city": {"type": "string", "description": "City name"}
          },
          "required": ["city"]
        }
      }
    ]
  }'
```

## 🌐 Google Gemini Interface

### Basic Chat Interface
```bash
curl https://api.your-domain.com/v1beta/gemini \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.0-flash",
    "contents": [
      {
        "role": "user",
        "parts": [
          {"text": "Explain the basic principles of quantum computing."}
        ]
      }
    ]
  }'
```

### Streaming Response
```bash
curl https://api.your-domain.com/v1beta/gemini \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.0-flash",
    "contents": [
      {
        "role": "user",
        "parts": [
          {"text": "Tell a joke."}
        ]
      }
    ],
    "stream": true
  }'
```

### Multimodal Input (Image + Text)
```bash
curl https://api.your-domain.com/v1beta/gemini \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.0-flash",
    "contents": [
      {
        "role": "user",
        "parts": [
          {"text": "Describe the content of this image:"},
          {
            "inline_data": {
              "mime_type": "image/jpeg",
              "data": "base64_encoded_image_data_here"
            }
          }
        ]
      }
    ]
  }'
```

## 🔄 Format Conversion

New API supports automatic conversion between different formats:

### OpenAI → Claude
```bash
# Use OpenAI format request, backend automatically converts to Claude format
curl https://api.your-domain.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-3-sonnet-20240229",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

### Claude → OpenAI
```bash
# Use Claude format request, return OpenAI format response
curl https://api.your-domain.com/v1/messages \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

## 🛠️ SDK Usage Examples

### Python
```python
import openai

# Configure client
client = openai.OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.your-domain.com/v1"
)

# Chat completions
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)
print(response.choices[0].message.content)

# Image generation
image_response = client.images.generate(
    model="dall-e-3",
    prompt="A cute cat",
    size="1024x1024",
    quality="standard",
    n=1
)
print(image_response.data[0].url)

# Embeddings
embedding_response = client.embeddings.create(
    model="text-embedding-ada-002",
    input="The weather is nice today"
)
print(embedding_response.data[0].embedding)
```

### JavaScript/Node.js
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://api.your-domain.com/v1',
});

const response = await client.chat.completions.create({
  model: 'gpt-4',
  messages: [{ role: 'user', content: 'Hello!' }],
});

console.log(response.choices[0].message.content);
```

### Go
```go
package main

import (
    "context"
    "fmt"
    openai "github.com/sashabaranov/go-openai"
)

func main() {
    config := openai.DefaultConfig("YOUR_API_KEY")
    config.BaseURL = "https://api.your-domain.com/v1"

    client := openai.NewClientWithConfig(config)

    resp, err := client.CreateChatCompletion(
        context.Background(),
        openai.ChatCompletionRequest{
            Model: openai.GPT4,
            Messages: []openai.ChatCompletionMessage{
                {
                    Role:    openai.ChatMessageRoleUser,
                    Content: "Hello",
                },
            },
        },
    )

    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }

    fmt.Println(resp.Choices[0].Message.Content)
}
```

## ⚡ Advanced Features

### Intelligent Routing
New API automatically selects the optimal AI provider channel:
- **Weighted Random**: Distribute requests according to channel weights
- **Failover**: Automatically switch to backup channel when a channel fails
- **Performance Optimization**: Dynamically adjust based on response time and success rate

### Cache Billing
For models supporting caching (OpenAI, Azure, DeepSeek, Claude, Qwen, etc.):
- Same prompt requests use cached results
- Reduce actual API call count
- Lower usage costs

### Rate Limiting
- **User-level limits**: Maximum request frequency per user
- **Token-level limits**: Usage quota per token
- **Model-level limits**: Concurrent request count per model

### Usage Statistics
Each API call records detailed statistical information:
- Call time, user, token, model
- Request and response content (optional)
- Token count and quota consumed

## 📊 Error Handling

### Common Error Codes
| Status Code | Description | Solution |
|-------------|-------------|----------|
| 401 | Authentication failed | Check if API key is correct |
| 403 | Insufficient permissions | Confirm token has access to corresponding models |
| 429 | Rate limit exceeded | Reduce request frequency or increase quota |
| 500 | Server error | Check service status or contact administrator |

### Error Response Format
```json
{
  "error": {
    "message": "Incorrect API key provided",
    "type": "invalid_request_error",
    "param": null,
    "code": "invalid_api_key"
  }
}
```

### Debugging Suggestions
1. Check Authorization in request Header
2. Confirm requested model is within token permissions
3. View dashboard logs for detailed error information
4. Use curl `-v` parameter to view complete request process

## 🔧 Best Practices

### 1. Connection Management
- Use connection pools to reduce connection establishment overhead
- Set reasonable timeout (recommended 30-60 seconds)
- Implement retry logic to handle temporary failures

### 2. Error Handling
- Implement exponential backoff retry mechanism
- Log errors for troubleshooting
- Set up monitoring alerts to detect anomalies promptly

### 3. Performance Optimization
- Use streaming responses to reduce perceived latency
- Batch process requests to improve efficiency
- Reasonably use caching to reduce redundant calculations

### 4. Cost Control
- Monitor usage to avoid unexpected expenses
- Use cache billing feature
- Choose appropriate models based on requirements

---

**Related Documents**: [Getting Started](./getting-started.md) | [Dashboard Usage](./dashboard.md) | [Back to Home](./index.md)
