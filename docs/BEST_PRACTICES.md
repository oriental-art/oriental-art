# OpenClaw 最佳实践指南

本文档总结了 AI Agent 框架和多渠道 Gateway 的市场最佳实践，结合 OpenClaw 的特性提供实用建议。

## 1. 架构设计最佳实践

### 1.1 Gateway 架构模式

**推荐模式：单一 Gateway + 多客户端**
```
┌─────────────────────────────────────────┐
│           OpenClaw Gateway              │
│  ┌─────────┐ ┌─────────┐ ┌──────────┐  │
│  │ WhatsApp│ │Telegram │ │ Discord  │  │
│  └────┬────┘ └────┬────┘ └────┬─────┘  │
│       └───────────┴───────────┘         │
│                  │                      │
│           WebSocket API                 │
└──────────────────┬──────────────────────┘
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
   ┌──────┐   ┌──────┐   ┌──────────┐
   │ CLI  │   │Web UI│   │ macOS App│
   └──────┘   └──────┘   └──────────┘
```

**最佳实践：**
- 每台主机运行一个 Gateway 实例
- 使用 WebSocket 进行实时通信
- 通过设备配对确保安全性
- 使用 Tailscale/VPN 进行远程访问

### 1.2 多 Agent 设计

**场景分离原则：**
| Agent | 用途 | 工作区 |
|-------|------|--------|
| main | 日常对话、通用任务 | ~/.openclaw/workspace |
| coder | 代码开发 | ~/projects |
| research | 研究分析 | ~/research |
| ops | 运维管理 | ~/ops |

**配置示例：**
```json
{
  "routing": {
    "agents": {
      "main": {
        "workspace": "~/.openclaw/workspace",
        "sandbox": { "mode": "off" }
      },
      "coder": {
        "workspace": "~/projects",
        "sandbox": { "mode": "non-main" }
      }
    }
  }
}
```

## 2. 安全最佳实践

### 2.1 认证与授权

**分层安全模型：**
1. **Gateway 级别**: Token 认证 (`gateway.auth.token`)
2. **设备级别**: 设备配对和设备令牌
3. **渠道级别**: 渠道特定的认证（如 WhatsApp QR、Telegram Bot Token）
4. **Agent 级别**: OAuth 或 API Key

**推荐配置：**
```bash
# 设置 Gateway Token
openclaw configure --section gateway --key auth.token --value "your-secure-token"

# 启用自动配对（仅本地）
openclaw configure --section gateway --key pairing.autoApproveLocal --value true

# 定期审计
openclaw security audit --deep
```

### 2.2 沙箱策略

| 场景 | 沙箱模式 | 说明 |
|------|----------|------|
| 日常对话 | `off` | 完全访问 |
| 代码执行 | `non-main` | 隔离非主会话 |
| 不可信输入 | `strict` | 完全沙箱化 |

### 2.3 密钥管理

**推荐做法：**
- 使用 `openclaw configure` 存储敏感配置
- 环境变量覆盖：`OPENCLAW_GATEWAY_TOKEN`
- 定期轮换 API Key
- 使用 OAuth 而非长期 API Key（如果支持）

## 3. 渠道配置最佳实践

### 3.1 渠道选择指南

| 渠道 | 适用场景 | 特点 |
|------|----------|------|
| WhatsApp | 个人使用、国际用户 | 最流行，需手机在线 |
| Telegram | 技术用户、群组 | 机器人友好，功能丰富 |
| Discord | 社区、团队协作 | 线程支持，适合复杂对话 |
| Slack | 企业环境 | 工作集成，审批流程 |
| 飞书 | 国内企业 | 国内合规，功能完整 |
| iMessage | Apple 生态 | 原生体验，隐私好 |

### 3.2 私信安全（配对）

**推荐流程：**
1. 默认启用配对码验证
2. 本地连接自动批准
3. 远程连接手动批准
4. 定期审查已配对设备

```bash
# 查看配对列表
openclaw pairing list whatsapp

# 批准配对
openclaw pairing approve whatsapp <code>

# 撤销配对
openclaw pairing revoke whatsapp <device-id>
```

## 4. 会话管理最佳实践

### 4.1 会话隔离

**隔离策略：**
- 按用户隔离（私信）
- 按群组隔离（群聊）
- 按 Agent 隔离（多 Agent）
- 按工作区隔离（项目）

### 4.2 会话修剪

**自动修剪配置：**
```json
{
  "session": {
    "pruning": {
      "enabled": true,
      "maxAge": "7d",
      "maxMessages": 1000
    }
  }
}
```

### 4.3 上下文管理

**最佳实践：**
- 使用 Memory 文件存储长期记忆
- 定期总结长会话
- 使用 `/compact` 压缩会话
- 关键决策写入 AGENTS.md

## 5. Skill 开发最佳实践

### 5.1 Skill 设计原则

**单一职责原则：**
每个 Skill 只做一件事，做好一件事。

**命名规范：**
- 使用小写和连字符：`weather-forecast`
- 功能明确：`github-issue-create`
- 避免过于宽泛：`utils`

### 5.2 Skill 结构

```
skills/
└── my-skill/
    ├── SKILL.md          # 使用说明
    ├── scripts/          # 执行脚本
    ├── references/       # 参考文档
    └── .gitignore
```

### 5.3 Skill 文档模板

```markdown
---
name: skill-name
description: 简短描述
---

# Skill 名称

## 何时使用

## 使用方法

## 示例

## 注意事项
```

## 6. 自动化最佳实践

### 6.1 Cron vs Heartbeat

| 特性 | Cron | Heartbeat |
|------|------|-----------|
| 精度 | 高（准时执行） | 低（约30分钟） |
| 持久化 | 是 | 否 |
| 适用场景 | 定时任务 | 周期性检查 |
| 示例 | 每日报告 | 邮件检查 |

### 6.2 Webhook 使用

**推荐场景：**
- GitHub PR 通知
- CI/CD 状态更新
- 外部系统集成

**安全配置：**
```json
{
  "webhooks": {
    "secret": "your-webhook-secret",
    "allowedIPs": ["192.168.1.0/24"]
  }
}
```

## 7. 模型配置最佳实践

### 7.1 模型选择

| 场景 | 推荐模型 | 原因 |
|------|----------|------|
| 代码开发 | Claude 3.5 Sonnet | 代码能力强 |
| 日常对话 | GPT-4o | 通用能力强 |
| 中文任务 | Moonshot Kimi | 中文优化 |
| 本地部署 | Ollama + Llama 3 | 隐私、离线 |
| 成本敏感 | GPT-4o-mini | 性价比高 |

### 7.2 模型故障转移

```json
{
  "models": {
    "default": "openai/gpt-4o",
    "fallback": ["anthropic/claude-3-sonnet", "moonshot/kimi-k2.5"]
  }
}
```

### 7.3 使用跟踪

```bash
# 查看使用情况
openclaw status --usage

# 设置预算警告
openclaw configure --section usage --key budget.monthly --value 100
```

## 8. 监控与运维

### 8.1 健康检查

```bash
# 快速健康检查
openclaw health

# 深度检查
openclaw status --deep

# 查看日志
openclaw logs --follow
```

### 8.2 备份策略

**关键数据：**
- `~/.openclaw/config.json` - 配置
- `~/.openclaw/credentials/` - 凭证
- `~/.openclaw/workspace/` - 工作区
- `~/.openclaw/sessions/` - 会话

**备份命令：**
```bash
openclaw backup create
openclaw backup restore <backup-id>
```

### 8.3 更新策略

```bash
# 检查更新
openclaw update check

# 安全更新
openclaw update apply --safe

# 回滚
openclaw update rollback
```

## 9. 性能优化

### 9.1 Gateway 优化

```json
{
  "gateway": {
    "workers": 4,
    "maxConnections": 100,
    "timeout": 30000
  }
}
```

### 9.2 会话优化

- 启用会话压缩
- 定期清理旧会话
- 使用流式响应

### 9.3 内存管理

```bash
# 查看内存使用
openclaw status --memory

# 强制垃圾回收
openclaw system gc
```

## 10. 故障排除

### 10.1 常见问题

| 问题 | 解决方案 |
|------|----------|
| Gateway 无法启动 | 检查端口占用、查看日志 |
| 渠道连接失败 | 验证凭证、检查网络 |
| Agent 无响应 | 检查认证、查看会话状态 |
| 高内存使用 | 清理会话、重启 Gateway |

### 10.2 调试工具

```bash
# 诊断工具
openclaw doctor

# 详细日志
openclaw gateway --verbose

# 网络测试
openclaw network test
```

## 11. 生态系统集成

### 11.1 开发工作流

**Git 集成：**
```bash
# 自动提交
openclaw hooks install git-post-commit

# PR 审查
openclaw agent --skill github-review
```

### 11.2 CI/CD 集成

```yaml
# .github/workflows/openclaw.yml
name: OpenClaw Notify
on: [push]
jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - uses: openclaw/notify-action@v1
        with:
          message: "New commit pushed"
```

## 12. 社区资源

- 官方文档: https://docs.openclaw.ai
- GitHub: https://github.com/openclaw/openclaw
- Discord: https://discord.com/invite/clawd
- Skill Hub: https://clawhub.com

---

*最后更新: 2026-04-04*
*基于 OpenClaw 官方文档和市场最佳实践整理*