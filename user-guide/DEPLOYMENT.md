# 文档部署指南

本文档介绍如何将用户指南部署为静态网站，以便负责人方便查看。

## 方案一：使用 docsify（推荐）

### 1. 安装 docsify-cli（仅需一次）

```bash
# 使用 npm
npm install docsify-cli -g

# 或使用 yarn
yarn global add docsify-cli

# 或使用 bun（如已安装）
bun add -g docsify-cli
```

### 2. 本地预览

进入 `docs/user-guide` 目录，运行：

```bash
docsify serve .
```

或使用 Python 内置服务器：

```bash
python serve.py
```

访问 `http://localhost:3000` 查看效果。

### 3. 配置说明

- `index.html` - docsify 主页面配置
- `_sidebar.md` - 导航侧边栏配置
- `README.md` - 文档首页内容

## 方案二：使用 Python 静态服务器（无需安装）

如果未安装 Node.js，可以使用 Python 内置服务器：

```bash
# Python 3
python -m http.server 3000

# 或使用提供的脚本
python serve.py
```

## 方案三：部署到 GitHub Pages

### 步骤一：创建 GitHub 仓库

1. 在 GitHub 创建新仓库，如 `ai-platform-user-guide`
2. 将 `docs/user-guide` 目录内容推送到仓库

### 步骤二：配置 GitHub Pages

1. 进入仓库 Settings → Pages
2. Source 选择 "Deploy from a branch"
3. Branch 选择 `main`，文件夹选择 `/`（根目录）
4. 点击 Save

### 步骤三：访问在线文档

等待几分钟后，访问：`https://[用户名].github.io/[仓库名]`

## 方案四：部署到内部服务器

将 `docs/user-guide` 目录复制到任何 Web 服务器（如 Nginx、Apache）的网站根目录即可。

## 自定义配置

### 修改网站标题

编辑 `index.html`，修改以下配置：

```javascript
window.$docsify = {
  name: 'AI大模型聚合平台 用户指南',
  // ... 其他配置
}
```

### 添加搜索功能

搜索功能已默认启用，如需调整搜索范围：

```javascript
search: {
  placeholder: '搜索文档...',
  noData: '未找到相关结果',
  depth: 3  // 搜索标题层级深度
}
```

### 修改主题样式

编辑 `index.html` 中的 CSS 样式部分，或更换 docsify 主题：

```html
<!-- 浅色主题 -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">

<!-- 深色主题 -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/dark.css">
```

## 维护说明

### 更新文档内容

1. 直接修改对应的 Markdown 文件（`zh/` 或 `en/` 目录）
2. 如需添加新文档，请在 `_sidebar.md` 中添加导航链接
3. 刷新浏览器查看更新

### 添加图片

将图片放入 `images/` 目录，在 Markdown 中使用：

```markdown
![图片说明](./images/example.png)
```

## 常见问题

### 1. 侧边栏不显示

确保 `_sidebar.md` 文件存在，且 `index.html` 中配置了 `loadSidebar: true`

### 2. 链接跳转错误

检查 `_sidebar.md` 中的相对路径是否正确，确保路径相对于 `docs/user-guide` 目录

### 3. 搜索功能无效

确保已加载 search.js 插件，且在 `window.$docsify` 配置中启用了 `search`

---

**快速开始命令汇总：**

```bash
# 进入文档目录
cd docs/user-guide

# 方法1：使用 docsify（需先安装）
docsify serve .

# 方法2：使用 Python（无需安装）
python serve.py

# 方法3：使用 Python 内置模块
python -m http.server 3000
```

部署完成后，将生成的 URL（本地或在线）发送给负责人即可。