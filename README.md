# 东方艺术 | Oriental Art

一个展示东方传统艺术的静态网站，采用现代极简设计风格，体现东方美学的意境与韵味。

## 在线预览

🌐 **https://oriental-art.github.io/oriental-art**

## 设计特点

- **东方色彩系统**：墨色、宣纸、朱砂、玉绿，营造典雅氛围
- ** typography**：思源宋体 + 思源黑体，中西文完美搭配
- **留白艺术**：大量呼吸空间，体现东方美学中的"空"
- **微妙动效**：克制优雅的过渡动画，不喧宾夺主

## 技术栈

- 纯 HTML + CSS + JavaScript
- 响应式设计，适配各种设备
- GitHub Actions 自动部署

## 本地预览

```bash
# 直接在浏览器打开
open index.html

# 或使用本地服务器
python -m http.server 8000
# 然后访问 http://localhost:8000
```

## 项目结构

```
.
├── index.html          # 主页面
├── .github/
│   └── workflows/
│       └── deploy.yml  # GitHub Pages 部署配置
└── README.md
```

## 部署

项目使用 GitHub Actions 自动部署到 GitHub Pages：

1. 推送代码到 `main` 分支
2. Actions 自动运行部署
3. 访问 `https://oriental-art.github.io/oriental-art`

## License

MIT