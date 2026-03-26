# API 调用指南

本文档详细介绍 AI大模型聚合平台 支持的各种 API 接口格式和调用方法。

## 📋 API 基础

### 认证方式
所有 API 请求都需要在 Header 中携带认证信息：

```bash
Authorization: Bearer YOUR_API_KEY
```

### 基础 URL
- **OpenAI 兼容接口**: `https://www.sunthycloud.ai/v1/`
- **Claude Messages 接口**: `https://www.sunthycloud.ai/v1/messages`
- **Google Gemini 接口**: `https://www.sunthycloud.ai/v1beta/gemini`

### 响应格式
默认返回 JSON 格式数据，包含以下字段：
```json
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-4",
  "choices": ["..."],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
```

## 🤖 OpenAI 兼容接口

AI大模型聚合平台 完全兼容 OpenAI API 规范，支持以下接口：

### 1. 聊天补全（Chat Completions）
```bash
curl https://www.sunthycloud.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {"role": "system", "content": "你是一个有帮助的助手。"},
      {"role": "user", "content": "写一首关于春天的诗。"}
    ],
    "temperature": 0.7,
    "max_tokens": 500,
    "stream": false
  }'
```

#### 流式响应（Streaming）
```bash
curl https://www.sunthycloud.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "你好"}],
    "stream": true
  }'
```

#### 函数调用（Function Calling）
```bash
curl https://www.sunthycloud.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "今天北京的天气怎么样？"}],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "获取城市天气信息",
          "parameters": {
            "type": "object",
            "properties": {
              "city": {"type": "string", "description": "城市名称"}
            },
            "required": ["city"]
          }
        }
      }
    ],
    "tool_choice": "auto"
  }'
```

### 2. 图像生成（Image Generation）
```bash
curl https://www.sunthycloud.ai/v1/images/generations \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "dall-e-3",
    "prompt": "一只可爱的猫咪在花园里玩耍",
    "n": 1,
    "size": "1024x1024",
    "quality": "standard"
  }'
```

### 3. 语音转文本（Speech to Text）
```bash
# 上传音频文件进行转录
curl https://www.sunthycloud.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@audio.mp3" \
  -F "model=whisper-1" \
  -F "response_format=json"
```

### 4. 文本转语音（Text to Speech）
```bash
curl https://www.sunthycloud.ai/v1/audio/speech \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1",
    "input": "你好，欢迎使用 New API！",
    "voice": "alloy",
    "response_format": "mp3"
  }' --output speech.mp3
```

### 5. 嵌入向量（Embeddings）
```bash
curl https://www.sunthycloud.ai/v1/embeddings \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-ada-002",
    "input": "今天天气真好",
    "encoding_format": "float"
  }'
```

### 6. 重排序（Rerank）
```bash
curl https://www.sunthycloud.ai/v1/rerank \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "rerank-english-v2.0",
    "query": "什么是人工智能？",
    "documents": [
      "人工智能是计算机科学的一个分支...",
      "机器学习是人工智能的一种实现方式...",
      "深度学习是机器学习的一个子集..."
    ],
    "top_n": 3
  }'
```

## 🎨 Claude Messages 接口

### 基础消息接口
```bash
curl https://www.sunthycloud.ai/v1/messages \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "写一个关于友谊的短故事。"}
    ]
  }'
```

### 流式响应
```bash
curl https://www.sunthycloud.ai/v1/messages \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "介绍一下你自己。"}
    ],
    "stream": true
  }'
```

### 工具使用（Tools）
```bash
curl https://www.sunthycloud.ai/v1/messages \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "查询伦敦的天气"}
    ],
    "tools": [
      {
        "name": "get_weather",
        "description": "获取城市天气信息",
        "input_schema": {
          "type": "object",
          "properties": {
            "city": {"type": "string", "description": "城市名称"}
          },
          "required": ["city"]
        }
      }
    ]
  }'
```

## 🌐 Google Gemini 接口

### 基础聊天接口
```bash
curl https://www.sunthycloud.ai/v1beta/gemini \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.0-flash",
    "contents": [
      {
        "role": "user",
        "parts": [
          {"text": "解释一下量子计算的基本原理。"}
        ]
      }
    ]
  }'
```

### 流式响应
```bash
curl https://www.sunthycloud.ai/v1beta/gemini \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.0-flash",
    "contents": [
      {
        "role": "user",
        "parts": [
          {"text": "讲一个笑话。"}
        ]
      }
    ],
    "stream": true
  }'
```

### 多模态输入（图片+文本）
```bash
curl https://www.sunthycloud.ai/v1beta/gemini \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.0-flash",
    "contents": [
      {
        "role": "user",
        "parts": [
          {"text": "描述这张图片的内容："},
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

## 🔄 格式转换

AI大模型聚合平台 支持不同格式之间的自动转换：

### OpenAI → Claude
```bash
# 使用 OpenAI 格式请求，后端自动转换为 Claude 格式
curl https://www.sunthycloud.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-3-sonnet-20240229",
    "messages": [{"role": "user", "content": "你好"}]
  }'
```

### Claude → OpenAI
```bash
# 使用 Claude 格式请求，返回 OpenAI 格式响应
curl https://www.sunthycloud.ai/v1/messages \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "你好"}]
  }'
```

## 🛠️ SDK 使用示例

### Python
```python
import openai

# 配置客户端
client = openai.OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://www.sunthycloud.ai/v1"
)

# 聊天补全
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "你好"}
    ]
)
print(response.choices[0].message.content)

# 图像生成
image_response = client.images.generate(
    model="dall-e-3",
    prompt="一只可爱的猫咪",
    size="1024x1024",
    quality="standard",
    n=1
)
print(image_response.data[0].url)

# 嵌入向量
embedding_response = client.embeddings.create(
    model="text-embedding-ada-002",
    input="今天天气真好"
)
print(embedding_response.data[0].embedding)
```

### JavaScript/Node.js
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
    config.BaseURL = "https://www.sunthycloud.ai/v1"

    client := openai.NewClientWithConfig(config)

    resp, err := client.CreateChatCompletion(
        context.Background(),
        openai.ChatCompletionRequest{
            Model: openai.GPT4,
            Messages: []openai.ChatCompletionMessage{
                {
                    Role:    openai.ChatMessageRoleUser,
                    Content: "你好",
                },
            },
        },
    )

    if err != nil {
        fmt.Printf("错误: %v\n", err)
        return
    }

    fmt.Println(resp.Choices[0].Message.Content)
}
```

## ⚡ 高级功能

### 智能路由
New API 自动选择最优的 AI 提供商通道：
- **加权随机**：根据通道权重分配请求
- **故障转移**：当某个通道失败时自动切换到备用通道
- **性能优化**：根据响应时间和成功率动态调整

### 缓存计费
对于支持缓存的模型（OpenAI、Azure、DeepSeek、Claude、Qwen 等）：
- 相同 prompt 的请求使用缓存结果
- 减少实际 API 调用次数
- 降低使用成本

### 速率限制
- **用户级限制**：每个用户的最大请求频率
- **令牌级限制**：每个令牌的使用额度
- **模型级限制**：每个模型的并发请求数

### 使用统计
每次 API 调用都会记录详细的统计信息：
- 调用时间、用户、令牌、模型
- 请求和响应内容（可选）
- 消耗的令牌数量和额度

## 📊 错误处理

### 常见错误码
| 状态码 | 说明 | 解决方法 |
|--------|------|----------|
| 401 | 认证失败 | 检查 API 密钥是否正确 |
| 403 | 权限不足 | 确认令牌有对应模型的访问权限 |
| 429 | 速率限制 | 降低请求频率或增加额度 |
| 500 | 服务器错误 | 检查服务状态或联系管理员 |

### 错误响应格式
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

### 调试建议
1. 检查请求 Header 中的 Authorization
2. 确认请求的模型在令牌权限范围内
3. 查看控制台日志获取详细错误信息
4. 使用 curl 的 `-v` 参数查看完整请求过程

## 🔧 最佳实践

### 1. 连接管理
- 使用连接池减少建立连接的开销
- 设置合理的超时时间（建议30-60秒）
- 实现重试逻辑处理暂时性故障

### 2. 错误处理
- 实现指数退避重试机制
- 记录错误日志便于排查问题
- 设置监控告警及时发现异常

### 3. 性能优化
- 使用流式响应减少延迟感
- 批量处理请求提高效率
- 合理使用缓存减少重复计算

### 4. 成本控制
- 监控使用量避免意外开销
- 使用缓存计费功能
- 根据需求选择合适的模型

---

**相关文档**: [快速开始](./getting-started.md) | [控制台使用](./dashboard.md) | [返回首页](./index.md)
