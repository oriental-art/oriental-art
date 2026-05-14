# OpenClaw 官方文档索引

> 本目录包含 OpenClaw 官方文档的本地副本，分为英文原文 (en) 和中文翻译 (zh-CN) 两个版本。

---

## 📁 目录结构

```
docs/
├── en/          # 英文原文
│   ├── start/       # 入门指南
│   ├── concepts/    # 核心概念
│   ├── channels/    # 渠道配置
│   ├── tools/       # 工具使用
│   ├── gateway/     # Gateway 配置
│   ├── cli/         # CLI 命令
│   └── automation/  # 自动化
└── zh-CN/       # 中文翻译
    ├── start/       # 入门指南
    ├── concepts/    # 核心概念
    ├── channels/    # 渠道配置
    ├── tools/       # 工具使用
    ├── gateway/     # Gateway 配置
    ├── cli/         # CLI 命令
    └── automation/  # 自动化
```

---

## 📚 文档分类

### 1. 入门指南 (start/)

| 英文文档 | 中文文档 | 说明 |
|---------|---------|------|
| [quickstart.md](en/start/quickstart.md) | [quickstart.md](zh-CN/start/quickstart.md) | 快速开始 |
| [getting-started.md](en/start/getting-started.md) | [getting-started.md](zh-CN/start/getting-started.md) | 入门指南 |
| [setup.md](en/start/setup.md) | [setup.md](zh-CN/start/setup.md) | 安装设置 |
| [onboarding.md](en/start/onboarding.md) | [onboarding.md](zh-CN/start/onboarding.md) | 新用户引导 |
| [bootstrapping.md](en/start/bootstrapping.md) | [bootstrapping.md](zh-CN/start/bootstrapping.md) | 启动配置 |
| [openclaw.md](en/start/openclaw.md) | [openclaw.md](zh-CN/start/openclaw.md) | OpenClaw 介绍 |
| [showcase.md](en/start/showcase.md) | [showcase.md](zh-CN/start/showcase.md) | 功能展示 |
| [hubs.md](en/start/hubs.md) | [hubs.md](zh-CN/start/hubs.md) | Hub 系统 |
| [lore.md](en/start/lore.md) | [lore.md](zh-CN/start/lore.md) | 背景故事 |
| [wizard.md](en/start/wizard.md) | [wizard.md](zh-CN/start/wizard.md) | 配置向导 |

### 2. 核心概念 (concepts/)

| 英文文档 | 中文文档 | 说明 |
|---------|---------|------|
| [agent.md](en/concepts/agent.md) | [agent.md](zh-CN/concepts/agent.md) | Agent 概念 |
| [agent-loop.md](en/concepts/agent-loop.md) | [agent-loop.md](zh-CN/concepts/agent-loop.md) | Agent 循环 |
| [agent-workspace.md](en/concepts/agent-workspace.md) | [agent-workspace.md](zh-CN/concepts/agent-workspace.md) | Agent 工作区 |
| [multi-agent.md](en/concepts/multi-agent.md) | [multi-agent.md](zh-CN/concepts/multi-agent.md) | 多 Agent 系统 |
| [session.md](en/concepts/session.md) | [session.md](zh-CN/concepts/session.md) | 会话管理 |
| [memory.md](en/concepts/memory.md) | [memory.md](zh-CN/concepts/memory.md) | 记忆系统 |
| [context.md](en/concepts/context.md) | [context.md](zh-CN/concepts/context.md) | 上下文管理 |
| [models.md](en/concepts/models.md) | [models.md](zh-CN/concepts/models.md) | 模型系统 |
| [model-providers.md](en/concepts/model-providers.md) | [model-providers.md](zh-CN/concepts/model-providers.md) | 模型提供商 |
| [model-failover.md](en/concepts/model-failover.md) | [model-failover.md](zh-CN/concepts/model-failover.md) | 模型故障转移 |
| [architecture.md](en/concepts/architecture.md) | [architecture.md](zh-CN/concepts/architecture.md) | 系统架构 |
| [features.md](en/concepts/features.md) | [features.md](zh-CN/concepts/features.md) | 功能特性 |
| [messages.md](en/concepts/messages.md) | [messages.md](zh-CN/concepts/messages.md) | 消息系统 |
| [streaming.md](en/concepts/streaming.md) | [streaming.md](zh-CN/concepts/streaming.md) | 流式响应 |
| [queue.md](en/concepts/queue.md) | [queue.md](zh-CN/concepts/queue.md) | 队列系统 |
| [retry.md](en/concepts/retry.md) | [retry.md](zh-CN/concepts/retry.md) | 重试机制 |
| [compaction.md](en/concepts/compaction.md) | [compaction.md](zh-CN/concepts/compaction.md) | 上下文压缩 |
| [session-pruning.md](en/concepts/session-pruning.md) | [session-pruning.md](zh-CN/concepts/session-pruning.md) | 会话修剪 |
| [oauth.md](en/concepts/oauth.md) | [oauth.md](zh-CN/concepts/oauth.md) | OAuth 认证 |
| [presence.md](en/concepts/presence.md) | [presence.md](zh-CN/concepts/presence.md) | 在线状态 |
| [typing-indicators.md](en/concepts/typing-indicators.md) | [typing-indicators.md](zh-CN/concepts/typing-indicators.md) | 输入指示器 |
| [timezone.md](en/concepts/timezone.md) | [timezone.md](zh-CN/concepts/timezone.md) | 时区处理 |
| [usage-tracking.md](en/concepts/usage-tracking.md) | [usage-tracking.md](zh-CN/concepts/usage-tracking.md) | 使用统计 |
| [system-prompt.md](en/concepts/system-prompt.md) | [system-prompt.md](zh-CN/concepts/system-prompt.md) | 系统提示词 |
| [markdown-formatting.md](en/concepts/markdown-formatting.md) | [markdown-formatting.md](zh-CN/concepts/markdown-formatting.md) | Markdown 格式 |
| [typebox.md](en/concepts/typebox.md) | [typebox.md](zh-CN/concepts/typebox.md) | TypeBox 验证 |
| [session-tool.md](en/concepts/session-tool.md) | [session-tool.md](zh-CN/concepts/session-tool.md) | 会话工具 |

### 3. 渠道配置 (channels/)

| 英文文档 | 中文文档 | 说明 |
|---------|---------|------|
| [index.md](en/channels/index.md) | [index.md](zh-CN/channels/index.md) | 渠道总览 |
| [telegram.md](en/channels/telegram.md) | [telegram.md](zh-CN/channels/telegram.md) | Telegram |
| [discord.md](en/channels/discord.md) | [discord.md](zh-CN/channels/discord.md) | Discord |
| [slack.md](en/channels/slack.md) | [slack.md](zh-CN/channels/slack.md) | Slack |
| [whatsapp.md](en/channels/whatsapp.md) | [whatsapp.md](zh-CN/channels/whatsapp.md) | WhatsApp |
| [feishu.md](en/channels/feishu.md) | [feishu.md](zh-CN/channels/feishu.md) | 飞书 |
| [imessage.md](en/channels/imessage.md) | [imessage.md](zh-CN/channels/imessage.md) | iMessage |
| [signal.md](en/channels/signal.md) | [signal.md](zh-CN/channels/signal.md) | Signal |
| [line.md](en/channels/line.md) | [line.md](zh-CN/channels/line.md) | LINE |
| [matrix.md](en/channels/matrix.md) | [matrix.md](zh-CN/channels/matrix.md) | Matrix |
| [msteams.md](en/channels/msteams.md) | [msteams.md](zh-CN/channels/msteams.md) | Microsoft Teams |
| [googlechat.md](en/channels/googlechat.md) | [googlechat.md](zh-CN/channels/googlechat.md) | Google Chat |
| [zalo.md](en/channels/zalo.md) | [zalo.md](zh-CN/channels/zalo.md) | Zalo |
| [nostr.md](en/channels/nostr.md) | [nostr.md](zh-CN/channels/nostr.md) | Nostr |
| [mattermost.md](en/channels/mattermost.md) | [mattermost.md](zh-CN/channels/mattermost.md) | Mattermost |
| [irc.md](en/channels/irc.md) | [irc.md](zh-CN/channels/irc.md) | IRC |
| [twitch.md](en/channels/twitch.md) | [twitch.md](zh-CN/channels/twitch.md) | Twitch |
| [bluebubbles.md](en/channels/bluebubbles.md) | [bluebubbles.md](zh-CN/channels/bluebubbles.md) | BlueBubbles |
| [nextcloud-talk.md](en/channels/nextcloud-talk.md) | [nextcloud-talk.md](zh-CN/channels/nextcloud-talk.md) | Nextcloud Talk |
| [tlon.md](en/channels/tlon.md) | [tlon.md](zh-CN/channels/tlon.md) | Tlon |
| [pairing.md](en/channels/pairing.md) | [pairing.md](zh-CN/channels/pairing.md) | 设备配对 |
| [groups.md](en/channels/groups.md) | [groups.md](zh-CN/channels/groups.md) | 群组管理 |
| [group-messages.md](en/channels/group-messages.md) | [group-messages.md](zh-CN/channels/group-messages.md) | 群组消息 |
| [broadcast-groups.md](en/channels/broadcast-groups.md) | [broadcast-groups.md](zh-CN/channels/broadcast-groups.md) | 广播群组 |
| [channel-routing.md](en/channels/channel-routing.md) | [channel-routing.md](zh-CN/channels/channel-routing.md) | 渠道路由 |
| [location.md](en/channels/location.md) | [location.md](zh-CN/channels/location.md) | 位置信息 |
| [troubleshooting.md](en/channels/troubleshooting.md) | [troubleshooting.md](zh-CN/channels/troubleshooting.md) | 故障排除 |

### 4. 工具使用 (tools/)

| 英文文档 | 中文文档 | 说明 |
|---------|---------|------|
| [index.md](en/tools/index.md) | [index.md](zh-CN/tools/index.md) | 工具总览 |
| [browser.md](en/tools/browser.md) | [browser.md](zh-CN/tools/browser.md) | 浏览器自动化 |
| [browser-login.md](en/tools/browser-login.md) | [browser-login.md](zh-CN/tools/browser-login.md) | 浏览器登录 |
| [exec.md](en/tools/exec.md) | [exec.md](zh-CN/tools/exec.md) | 执行命令 |
| [exec-approvals.md](en/tools/exec-approvals.md) | [exec-approvals.md](zh-CN/tools/exec-approvals.md) | 执行审批 |
| [elevated.md](en/tools/elevated.md) | [elevated.md](zh-CN/tools/elevated.md) | 提升权限 |
| [web.md](en/tools/web.md) | [web.md](zh-CN/tools/web.md) | Web 搜索 |
| [skills.md](en/tools/skills.md) | [skills.md](zh-CN/tools/skills.md) | Skill 系统 |
| [skills-config.md](en/tools/skills-config.md) | [skills-config.md](zh-CN/tools/skills-config.md) | Skill 配置 |
| [creating-skills.md](en/tools/creating-skills.md) | [creating-skills.md](zh-CN/tools/creating-skills.md) | 创建 Skill |
| [clawhub.md](en/tools/clawhub.md) | [clawhub.md](zh-CN/tools/clawhub.md) | ClawHub |
| [subagents.md](en/tools/subagents.md) | [subagents.md](zh-CN/tools/subagents.md) | 子 Agent |
| [agent-send.md](en/tools/agent-send.md) | [agent-send.md](zh-CN/tools/agent-send.md) | Agent 发送 |
| [slash-commands.md](en/tools/slash-commands.md) | [slash-commands.md](zh-CN/tools/slash-commands.md) | 斜杠命令 |
| [reactions.md](en/tools/reactions.md) | [reactions.md](zh-CN/tools/reactions.md) | 消息反应 |
| [thinking.md](en/tools/thinking.md) | [thinking.md](zh-CN/tools/thinking.md) | 思考模式 |
| [lobster.md](en/tools/lobster.md) | [lobster.md](zh-CN/tools/lobster.md) | Lobster 工具 |
| [firecrawl.md](en/tools/firecrawl.md) | [firecrawl.md](zh-CN/tools/firecrawl.md) | Firecrawl |
| [apply-patch.md](en/tools/apply-patch.md) | [apply-patch.md](zh-CN/tools/apply-patch.md) | 应用补丁 |
| [diffs.md](en/tools/diffs.md) | - | 差异处理 |
| [plugin.md](en/tools/plugin.md) | [plugin.md](zh-CN/tools/plugin.md) | 插件系统 |
| [chrome-extension.md](en/tools/chrome-extension.md) | [chrome-extension.md](zh-CN/tools/chrome-extension.md) | Chrome 扩展 |
| [llm-task.md](en/tools/llm-task.md) | [llm-task.md](zh-CN/tools/llm-task.md) | LLM 任务 |
| [multi-agent-sandbox-tools.md](en/tools/multi-agent-sandbox-tools.md) | [multi-agent-sandbox-tools.md](zh-CN/tools/multi-agent-sandbox-tools.md) | 多 Agent 沙盒 |
| [browser-linux-troubleshooting.md](en/tools/browser-linux-troubleshooting.md) | [browser-linux-troubleshooting.md](zh-CN/tools/browser-linux-troubleshooting.md) | Linux 浏览器故障 |
| [browser-wsl2-windows-remote-cdp-troubleshooting.md](en/tools/browser-wsl2-windows-remote-cdp-troubleshooting.md) | [browser-wsl2-windows-remote-cdp-troubleshooting.md](zh-CN/tools/browser-wsl2-windows-remote-cdp-troubleshooting.md) | WSL2 浏览器故障 |
| [pdf.md](en/tools/pdf.md) | - | PDF 工具 |
| [acp-agents.md](en/tools/acp-agents.md) | - | ACP Agents |
| [loop-detection.md](en/tools/loop-detection.md) | - | 循环检测 |

### 5. Gateway 配置 (gateway/)

| 英文文档 | 中文文档 | 说明 |
|---------|---------|------|
| [index.md](en/gateway/index.md) | [index.md](zh-CN/gateway/index.md) | Gateway 总览 |
| [configuration.md](en/gateway/configuration.md) | [configuration.md](zh-CN/gateway/configuration.md) | 配置指南 |
| [configuration-reference.md](en/gateway/configuration-reference.md) | - | 配置参考 |
| [configuration-examples.md](en/gateway/configuration-examples.md) | [configuration-examples.md](zh-CN/gateway/configuration-examples.md) | 配置示例 |
| [authentication.md](en/gateway/authentication.md) | [authentication.md](zh-CN/gateway/authentication.md) | 认证 |
| [pairing.md](en/gateway/pairing.md) | [pairing.md](zh-CN/gateway/pairing.md) | 设备配对 |
| [remote.md](en/gateway/remote.md) | [remote.md](zh-CN/gateway/remote.md) | 远程访问 |
| [tailscale.md](en/gateway/tailscale.md) | [tailscale.md](zh-CN/gateway/tailscale.md) | Tailscale |
| [discovery.md](en/gateway/discovery.md) | [discovery.md](zh-CN/gateway/discovery.md) | 服务发现 |
| [bonjour.md](en/gateway/bonjour.md) | [bonjour.md](zh-CN/gateway/bonjour.md) | Bonjour |
| [protocol.md](en/gateway/protocol.md) | [protocol.md](zh-CN/gateway/protocol.md) | 协议 |
| [bridge-protocol.md](en/gateway/bridge-protocol.md) | [bridge-protocol.md](zh-CN/gateway/bridge-protocol.md) | 桥接协议 |
| [network-model.md](en/gateway/network-model.md) | [network-model.md](zh-CN/gateway/network-model.md) | 网络模型 |
| [heartbeat.md](en/gateway/heartbeat.md) | [heartbeat.md](zh-CN/gateway/heartbeat.md) | 心跳机制 |
| [health.md](en/gateway/health.md) | [health.md](zh-CN/gateway/health.md) | 健康检查 |
| [logging.md](en/gateway/logging.md) | [logging.md](zh-CN/gateway/logging.md) | 日志 |
| [sandboxing.md](en/gateway/sandboxing.md) | [sandboxing.md](zh-CN/gateway/sandboxing.md) | 沙箱 |
| [sandbox-vs-tool-policy-vs-elevated.md](en/gateway/sandbox-vs-tool-policy-vs-elevated.md) | [sandbox-vs-tool-policy-vs-elevated.md](zh-CN/gateway/sandbox-vs-tool-policy-vs-elevated.md) | 沙箱对比 |
| [secrets.md](en/gateway/secrets.md) | - | 密钥管理 |
| [secrets-plan-contract.md](en/gateway/secrets-plan-contract.md) | - | 密钥计划 |
| [local-models.md](en/gateway/local-models.md) | [local-models.md](zh-CN/gateway/local-models.md) | 本地模型 |
| [openai-http-api.md](en/gateway/openai-http-api.md) | [openai-http-api.md](zh-CN/gateway/openai-http-api.md) | OpenAI HTTP API |
| [openresponses-http-api.md](en/gateway/openresponses-http-api.md) | [openresponses-http-api.md](zh-CN/gateway/openresponses-http-api.md) | OpenResponses API |
| [tools-invoke-http-api.md](en/gateway/tools-invoke-http-api.md) | [tools-invoke-http-api.md](zh-CN/gateway/tools-invoke-http-api.md) | 工具调用 API |
| [cli-backends.md](en/gateway/cli-backends.md) | [cli-backends.md](zh-CN/gateway/cli-backends.md) | CLI 后端 |
| [background-process.md](en/gateway/background-process.md) | [background-process.md](zh-CN/gateway/background-process.md) | 后台进程 |
| [multiple-gateways.md](en/gateway/multiple-gateways.md) | [multiple-gateways.md](zh-CN/gateway/multiple-gateways.md) | 多 Gateway |
| [gateway-lock.md](en/gateway/gateway-lock.md) | [gateway-lock.md](zh-CN/gateway/gateway-lock.md) | Gateway 锁定 |
| [doctor.md](en/gateway/doctor.md) | [doctor.md](zh-CN/gateway/doctor.md) | 诊断工具 |
| [troubleshooting.md](en/gateway/troubleshooting.md) | [troubleshooting.md](zh-CN/gateway/troubleshooting.md) | 故障排除 |
| [trusted-proxy-auth.md](en/gateway/trusted-proxy-auth.md) | - | 可信代理认证 |
| [remote-gateway-readme.md](en/gateway/remote-gateway-readme.md) | [remote-gateway-readme.md](zh-CN/gateway/remote-gateway-readme.md) | 远程 Gateway |
| [security/index.md](en/gateway/security/index.md) | [security/index.md](zh-CN/gateway/security/index.md) | 安全指南 |

### 6. CLI 命令 (cli/)

| 英文文档 | 中文文档 | 说明 |
|---------|---------|------|
| [index.md](en/cli/index.md) | [index.md](zh-CN/cli/index.md) | CLI 总览 |
| [setup.md](en/cli/setup.md) | [setup.md](zh-CN/cli/setup.md) | 设置命令 |
| [configure.md](en/cli/configure.md) | [configure.md](zh-CN/cli/configure.md) | 配置命令 |
| [config.md](en/cli/config.md) | [config.md](zh-CN/cli/config.md) | 配置管理 |
| [gateway.md](en/cli/gateway.md) | [gateway.md](zh-CN/cli/gateway.md) | Gateway 命令 |
| [channels.md](en/cli/channels.md) | [channels.md](zh-CN/cli/channels.md) | 渠道命令 |
| [skills.md](en/cli/skills.md) | [skills.md](zh-CN/cli/skills.md) | Skill 命令 |
| [agents.md](en/cli/agents.md) | [agents.md](zh-CN/cli/agents.md) | Agent 命令 |
| [agent.md](en/cli/agent.md) | [agent.md](zh-CN/cli/agent.md) | Agent 管理 |
| [sessions.md](en/cli/sessions.md) | [sessions.md](zh-CN/cli/sessions.md) | 会话命令 |
| [nodes.md](en/cli/nodes.md) | [nodes.md](zh-CN/cli/nodes.md) | 节点命令 |
| [node.md](en/cli/node.md) | [node.md](zh-CN/cli/node.md) | 节点管理 |
| [devices.md](en/cli/devices.md) | [devices.md](zh-CN/cli/devices.md) | 设备命令 |
| [pairing.md](en/cli/pairing.md) | [pairing.md](zh-CN/cli/pairing.md) | 配对命令 |
| [models.md](en/cli/models.md) | [models.md](zh-CN/cli/models.md) | 模型命令 |
| [cron.md](en/cli/cron.md) | [cron.md](zh-CN/cli/cron.md) | 定时任务 |
| [hooks.md](en/cli/hooks.md) | [hooks.md](zh-CN/cli/hooks.md) | Hook 命令 |
| [logs.md](en/cli/logs.md) | [logs.md](zh-CN/cli/logs.md) | 日志命令 |
| [status.md](en/cli/status.md) | [status.md](zh-CN/cli/status.md) | 状态命令 |
| [health.md](en/cli/health.md) | [health.md](zh-CN/cli/health.md) | 健康检查 |
| [doctor.md](en/cli/doctor.md) | [doctor.md](zh-CN/cli/doctor.md) | 诊断命令 |
| [update.md](en/cli/update.md) | [update.md](zh-CN/cli/update.md) | 更新命令 |
| [backup.md](en/cli/backup.md) | - | 备份命令 |
| [sandbox.md](en/cli/sandbox.md) | [sandbox.md](zh-CN/cli/sandbox.md) | 沙箱命令 |
| [security.md](en/cli/security.md) | [security.md](zh-CN/cli/security.md) | 安全命令 |
| [memory.md](en/cli/memory.md) | [memory.md](zh-CN/cli/memory.md) | 内存命令 |
| [message.md](en/cli/message.md) | [message.md](zh-CN/cli/message.md) | 消息命令 |
| [browser.md](en/cli/browser.md) | [browser.md](zh-CN/cli/browser.md) | 浏览器命令 |
| [dashboard.md](en/cli/dashboard.md) | [dashboard.md](zh-CN/cli/dashboard.md) | 仪表板 |
| [tui.md](en/cli/tui.md) | [tui.md](zh-CN/cli/tui.md) | TUI 界面 |
| [docs.md](en/cli/docs.md) | [docs.md](zh-CN/cli/docs.md) | 文档命令 |
| [directory.md](en/cli/directory.md) | [directory.md](zh-CN/cli/directory.md) | 目录命令 |
| [plugins.md](en/cli/plugins.md) | [plugins.md](zh-CN/cli/plugins.md) | 插件命令 |
| [dns.md](en/cli/dns.md) | [dns.md](zh-CN/cli/dns.md) | DNS 命令 |
| [system.md](en/cli/system.md) | [system.md](zh-CN/cli/system.md) | 系统命令 |
| [onboard.md](en/cli/onboard.md) | [onboard.md](zh-CN/cli/onboard.md) | 引导命令 |
| [qr.md](en/cli/qr.md) | [qr.md](zh-CN/cli/qr.md) | QR 码命令 |
| [reset.md](en/cli/reset.md) | [reset.md](zh-CN/cli/reset.md) | 重置命令 |
| [uninstall.md](en/cli/uninstall.md) | [uninstall.md](zh-CN/cli/uninstall.md) | 卸载命令 |
| [voicecall.md](en/cli/voicecall.md) | [voicecall.md](zh-CN/cli/voicecall.md) | 语音通话 |
| [webhooks.md](en/cli/webhooks.md) | [webhooks.md](zh-CN/cli/webhooks.md) | Webhook 命令 |
| [clawbot.md](en/cli/clawbot.md) | - | ClawBot |
| [acp.md](en/cli/acp.md) | [acp.md](zh-CN/cli/acp.md) | ACP 命令 |
| [approvals.md](en/cli/approvals.md) | - | 审批命令 |
| [daemon.md](en/cli/daemon.md) | - | 守护进程 |
| [completion.md](en/cli/completion.md) | - | 自动补全 |

### 7. 自动化 (automation/)

| 英文文档 | 中文文档 | 说明 |
|---------|---------|------|
| [cron-jobs.md](en/automation/cron-jobs.md) | [cron-jobs.md](zh-CN/automation/cron-jobs.md) | 定时任务 |
| [cron-vs-heartbeat.md](en/automation/cron-vs-heartbeat.md) | [cron-vs-heartbeat.md](zh-CN/automation/cron-vs-heartbeat.md) | Cron vs 心跳 |
| [webhook.md](en/automation/webhook.md) | [webhook.md](zh-CN/automation/webhook.md) | Webhook |
| [hooks.md](en/automation/hooks.md) | [hooks.md](zh-CN/automation/hooks.md) | Hooks |
| [poll.md](en/automation/poll.md) | [poll.md](zh-CN/automation/poll.md) | 轮询 |
| [gmail-pubsub.md](en/automation/gmail-pubsub.md) | [gmail-pubsub.md](zh-CN/automation/gmail-pubsub.md) | Gmail Pub/Sub |
| [auth-monitoring.md](en/automation/auth-monitoring.md) | [auth-monitoring.md](zh-CN/automation/auth-monitoring.md) | 认证监控 |
| [troubleshooting.md](en/automation/troubleshooting.md) | [troubleshooting.md](zh-CN/automation/troubleshooting.md) | 故障排除 |

---

## 📊 统计

| 分类 | 英文文档数 | 中文文档数 |
|-----|-----------|-----------|
| 入门指南 (start) | 12 | 11 |
| 核心概念 (concepts) | 27 | 27 |
| 渠道配置 (channels) | 27 | 26 |
| 工具使用 (tools) | 28 | 25 |
| Gateway 配置 (gateway) | 33 | 29 |
| CLI 命令 (cli) | 42 | 38 |
| 自动化 (automation) | 8 | 8 |
| **总计** | **177** | **164** |

---

## 📝 说明

- 英文文档源位置：`~/.nvm/versions/node/v24.14.0/lib/node_modules/openclaw/docs/`
- 中文文档源位置：`~/.nvm/versions/node/v24.14.0/lib/node_modules/openclaw/docs/zh-CN/`
- 部分文档可能没有中文翻译版本
- 建议优先查看中文文档，如有疑问可参考英文原文

---

*最后更新：2026-04-04*

---

## 📚 新增解读文档

### 文档指南
- [DOCUMENT_GUIDE.md](DOCUMENT_GUIDE.md) - 官方文档深度解读与分类
  - 10层文档分类体系
  - 推荐阅读路径
  - 问题排查指南
  - 关键概念索引

### 知识图谱
- [KNOWLEDGE_GRAPH.md](KNOWLEDGE_GRAPH.md) - 组件关系与架构图谱
  - 整体架构图
  - 数据流图谱
  - 组件依赖矩阵
  - 状态流转图
  - 部署拓扑图

### 最佳实践
- [BEST_PRACTICES.md](BEST_PRACTICES.md) - 市场最佳实践汇总
  - 架构设计模式
  - 安全配置指南
  - 性能优化策略
  - 运维管理方案

---

## 🎯 如何使用这些文档

### 新手入门
1. 阅读 `README.md` 了解文档结构
2. 按 `DOCUMENT_GUIDE.md` 的"路径1"阅读核心文档
3. 遇到问题查阅 `DOCUMENT_GUIDE.md` 的"问题排查"章节

### 开发者
1. 查看 `KNOWLEDGE_GRAPH.md` 理解架构
2. 阅读 `DOCUMENT_GUIDE.md` 的"路径2"
3. 参考 `BEST_PRACTICES.md` 进行开发

### 运维工程师
1. 查看 `KNOWLEDGE_GRAPH.md` 的部署拓扑
2. 阅读 `DOCUMENT_GUIDE.md` 的"路径3"
3. 遵循 `BEST_PRACTICES.md` 的运维建议

### 架构师
1. 深度阅读 `KNOWLEDGE_GRAPH.md`
2. 参考 `DOCUMENT_GUIDE.md` 的"路径4"
3. 结合 `BEST_PRACTICES.md` 设计方案

