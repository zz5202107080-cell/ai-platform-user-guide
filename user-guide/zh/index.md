# AI大模型聚合平台 用户指南

## 欢迎使用 AI大模型聚合平台

AI大模型聚合平台 是一个统一的 AI 网关平台，支持 40+ 个上游 AI 提供商（OpenAI、Claude、Gemini等），提供用户管理、计费、速率限制和管理仪表板等功能。

## 📚 文档目录

### 1. 基础使用
- **[快速开始](./getting-started.md)** - 注册、登录、获取API密钥
- **[控制台使用](./dashboard.md)** - 仪表板、令牌管理、模型配置

### 2. API 开发
- **[API调用](./api-usage.md)** - 各接口示例和使用指南
- 支持格式：OpenAI、Claude Messages、Google Gemini、Azure等

### 3. 高级功能
- **智能路由** - 通道加权随机、自动重试
- **计费策略** - 按使用量计费、缓存计费支持
- **多租户管理** - 用户分组、权限控制

## 🚀 快速入门

```bash
# 1. 获取API密钥
# 登录控制台 -> 令牌管理 -> 创建新令牌

# 2. 测试API连接
curl https://www.sunthycloud.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## 📖 阅读建议

### 新用户
1. 阅读 **[快速开始](./getting-started.md)** 完成注册和基础配置
2. 查看 **[控制台使用](./dashboard.md)** 了解管理界面
3. 参考 **[API调用](./api-usage.md)** 进行开发集成

## 🌐 多语言支持
- [English Documentation](../en/index.md)

---

**下一步**: [快速开始 →](./getting-started.md)
