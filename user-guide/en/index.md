# AI Model Aggregation Platform User Guide

## Welcome to AI Model Aggregation Platform

AI Model Aggregation Platform is a unified AI gateway platform supporting 40+ upstream AI providers (OpenAI, Claude, Gemini, Azure, AWS Bedrock, etc.), providing user management, billing, rate limiting, and admin dashboard functionalities.

## 📚 Documentation Contents

### 1. Basic Usage
- **[Getting Started](./getting-started.md)** - Registration, login, API key acquisition
- **[Dashboard Usage](./dashboard.md)** - Dashboard, token management, model configuration

### 2. API Development
- **[API Usage](./api-usage.md)** - Interface examples and usage guidelines
- Supported formats: OpenAI, Claude Messages, Google Gemini, Azure, etc.

### 3. Advanced Features
- **Intelligent Routing** - Channel weighted random, automatic retry
- **Billing Strategies** - Pay-per-use, cache billing support
- **Multi-tenant Management** - User grouping, permission control

### 4. Operations Support
- **Monitoring & Alerts** - Usage statistics, performance monitoring

## 🚀 Quick Start

```bash
# 1. Get API Key
# Login to dashboard -> Token Management -> Create New Token

# 2. Test API Connection
curl https://www.sunthycloud.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## 📖 Reading Recommendations

### New Users
1. Read **[Getting Started](./getting-started.md)** to complete registration and basic configuration
2. Check **[Dashboard Usage](./dashboard.md)** to understand the management interface
3. Refer to **[API Usage](./api-usage.md)** for development integration

### Developers
1. Directly view **[API Usage](./api-usage.md)** for interface details
2. Focus on format conversion and intelligent routing features
3. Understand billing strategies and rate limiting configurations

### Administrators
1. Familiarize with user management and permission configuration
2. Configure channel and model routing rules
3. Set up monitoring alerts and billing strategies

## 🔗 Related Resources

- **Official Documentation**: [docs.newapi.pro](https://docs.newapi.pro/en/docs)
- **GitHub Repository**: [Calcium-Ion/new-api](https://github.com/Calcium-Ion/new-api)
- **Issue Feedback**: [GitHub Issues](https://github.com/Calcium-Ion/new-api/issues)

## 🌐 Multilingual Support
- [中文文档](../zh/index.md)

---

**Next Step**: [Getting Started →](./getting-started.md)
