# Dashboard Usage Guide

The AI Model Aggregation Platform dashboard provides a complete management interface for configuring and managing AI services.

## 📊 Dashboard Overview

After login, you will see the following main functional areas:

### Left Navigation Menu
- **Conversation** - Playground for testing models and chatting
- **Dashboard** - Data dashboard, token management and usage logs
  - **Data Dashboard** - System overview and key metrics
  - **Token Management** - API key creation and management
  - **Usage Logs** - API call record query
- **Personal Center** - Wallet management and personal settings

## 🏠 Data Dashboard

The data dashboard provides an overview view of key system metrics.

### 1. Statistics Cards
- **Account Data** - Account current balance and historical consumption
- **Usage Statistics**
  - Request Count: Total request count for the account
  - Statistical Count: Request count within current query time range
- **Resource Consumption**
  - Statistical Quota: Quota consumed within current query time range
  - Statistical Tokens: Token count consumed within current query time range
- **Performance Metrics**
  - Average RPM: Requests Per Minute
  - Average TPM: Tokens Per Minute

### 2. Model Data Analysis
- **Consumption Distribution** - Model usage consumption distribution
- **Consumption Trend** - Recent model call volume changes
- **Call Count Distribution** - Usage proportion of each AI model
- **Call Count Ranking** - Most frequently used AI models ranking

## 🔑 Token Management

### Token List View
- Display all created API tokens
- Each row shows: token name, token status, remaining quota/total quota, key (partially hidden), available models, IP restrictions, creation time, expiration time
- Support search by name, search by key

### Create New Token
Click the "Add Token" button and fill out the form:

| Field | Description | Required |
|-------|-------------|----------|
| Token Name | Easy-to-identify name | Yes |
| Expiration Time | Set token validity period | Yes |
| New Quantity | Set token quantity | Yes |
| Quota Settings | Set token available quota | No |
| Access Permissions | Select AI models accessible by this token | No |

### Token Operations
- **Edit** - Modify token configuration (name, model permissions, etc.)
- **Copy Key** - Copy complete API key
- **Disable/Enable** - Temporarily deactivate or re-enable token
- **Delete** - Permanently delete token (use with caution)

## 📝 Usage Logs

### Log Query
- **Time Filter** - Query logs by time range
- **Condition Filter** - Filter by user, token, model, status, etc.

### Log Details
Each log record contains:
- **Timestamp** - Time when request occurred
- **User/Token** - User or token that initiated the request
- **Model** - Requested AI model
- **Channel** - Actually used AI provider channel
- **Status Code** - HTTP status code and error message
- **Duration** - Request processing time
- **Input/Output** - Request and response content (expandable)

## ⚙️ Personal Center

### Wallet Management
- **Global Configuration** -

### Personal Settings
- **Account Binding** - Bind, modify email
- **Security Settings**
  - System Access Token: Generate authentication tokens for API calls
  - Password Management: Change account login password
  - Passkey Login (Passwordless Authentication): Modern passwordless authentication based on WebAuthn standard
  - Two-Step Verification Setup: Complete TOTP (Time-based One-time Password) two-step verification system
  - Delete Account: Permanently delete user account
- **Notification Settings** - Configure notification types to receive

## 🆘 Frequently Asked Questions

### Q: Token remaining quota inaccurate?
A: Check if there are pending asynchronous requests, or wait for the statistics system to update (usually a few minutes delay).

### Q: Cannot see certain menus?
A: Some functions require admin permissions, please contact system administrator.

### Q: Statistical chart data delayed?
A: Statistical data usually has a 5-15 minute delay to ensure data accuracy.

### Q: Log query too slow?
A: Try narrowing the time range or adding more filter conditions.

---

**Related Documents**: [Getting Started](./getting-started.md) | [API Usage](./api-usage.md) | [Back to Home](./index.md)