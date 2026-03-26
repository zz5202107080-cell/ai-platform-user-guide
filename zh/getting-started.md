# 快速开始

本文档将引导您完成 AI大模型聚合平台 的初次使用流程。

## 🔐 第一步：登录系统

### 网页登录
1. 访问登录页面（通常为首页）
2. 输入用户名/邮箱和密码
3. 点击"登录"
4. 成功登录后进入控制台

### 获取访问令牌（用于 API 认证）
```bash
curl -X POST https://www.sunthycloud.ai/api/user/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```

响应示例：
```json
{
  "code": 200,
  "message": "登录成功",
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

## 🔑 第二步：获取 API 密钥

### 通过控制台创建令牌
1. 登录后，点击左侧菜单"令牌管理"
2. 点击"新建令牌"按钮
3. 配置令牌参数：
   - **令牌名称**：便于识别的名称（如："生产环境API密钥"）
   - **模型权限**：选择该令牌可访问的AI模型
   - **额度限制**：设置使用额度（可选）
   - **过期时间**：设置有效期（可选）
4. 点击"创建"
5. **立即复制生成的 API 密钥**

### 通过 API 创建令牌
```bash
curl -X POST https://www.sunthycloud.ai/api/token \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "生产环境API密钥",
    "models": ["gpt-4", "claude-3"],
    "remain_quota": 1000000
  }'
```

响应中的 `key` 字段即为 API 密钥。

## 🚀 第三步：第一个 API 调用

### OpenAI 兼容接口
```bash
curl https://www.sunthycloud.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {"role": "system", "content": "你是一个有帮助的助手。"},
      {"role": "user", "content": "你好，介绍一下你自己。"}
    ],
    "temperature": 0.7,
    "max_tokens": 500
  }'
```

### Claude Messages 格式
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

### Google Gemini 格式
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

## 📊 第四步：查看使用情况

### 控制台查看
1. 进入"数据看板"页面查看使用图表
2. 在"令牌管理"中查看剩余额度
3. 使用"使用日志"功能查看API调用历史

### API 查询使用量
```bash
curl https://www.sunthycloud.ai/api/token/usage \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 🔧 常见配置

### 1. 环境变量配置（推荐）
```bash
export NEW_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export NEW_API_BASE="https://www.sunthycloud.ai"
```

### 2. Python SDK 使用示例
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

### 3. JavaScript/Node.js 示例
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

## ⚠️ 注意事项

1. **API 密钥安全**
   - 不要将 API 密钥提交到版本控制系统
   - 使用环境变量或密钥管理服务
   - 定期轮换密钥

2. **额度管理**
   - 监控使用量避免超额
   - 设置使用警报
   - 了解计费策略

3. **模型兼容性**
   - 确认令牌有对应模型的访问权限
   - 不同接口格式需要不同的请求结构
   - 查看支持的模型列表

## 🆘 遇到问题？

- 检查网络连接和 API 地址
- 验证 API 密钥是否正确
- 确认令牌有足够的额度和正确的模型权限
- 查看错误日志获取详细信息

---

**下一步**: [控制台使用 →](./dashboard.md) | [返回首页](./index.md)
