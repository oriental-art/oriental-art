# OpenClaw 官方文档深度解读与关系图谱

本文档对 OpenClaw 387 个官方文档进行系统性解读、分类和关系梳理，帮助快速理解和使用。

---

## 📊 文档全景图

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           OpenClaw 文档体系                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   入门层    │───▶│   概念层    │───▶│   配置层    │───▶│   进阶层    │  │
│  │  (Start)    │    │ (Concepts)  │    │   (Setup)   │    │ (Advanced)  │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│         │                  │                  │                  │          │
│         ▼                  ▼                  ▼                  ▼          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │ 快速开始    │    │ 架构原理    │    │ 渠道配置    │    │ 自动化      │  │
│  │ 安装向导    │    │ 核心机制    │    │ 工具使用    │    │ 多Agent     │  │
│  │ 第一条消息  │    │ 数据流      │    │ Gateway     │    │ 开发集成    │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 文档分类体系

### 第一层：入门引导（Getting Started）

**目标用户**：完全的新手，从零开始

| 文档 | 作用 | 阅读顺序 |
|------|------|----------|
| `index.md` | 项目总览，什么是 OpenClaw | ⭐ 第1个 |
| `start/getting-started.md` | 最快上手路径，零到第一条消息 | ⭐ 第2个 |
| `start/wizard.md` | 配置向导详解 | 第3个 |
| `start/setup.md` | 详细安装和配置说明 | 第4个 |
| `start/onboarding.md` | 新手引导流程 | 第5个 |
| `start/quickstart.md` | 快速参考卡片 | 随时查阅 |

**关系图谱**：
```
index.md (了解是什么)
    ↓
getting-started.md (跟着做)
    ↓
wizard.md (理解向导)
    ↓
setup.md (深入配置)
    ↓
onboarding.md (完整流程)
```

---

### 第二层：核心概念（Core Concepts）

**目标用户**：已安装完成，想深入理解原理

#### 2.1 架构与协议

| 文档 | 核心内容 | 关联文档 |
|------|----------|----------|
| `concepts/architecture.md` | Gateway 架构、WebSocket 协议、组件关系 | gateway/protocol.md, gateway/configuration.md |
| `concepts/session.md` | 会话生命周期、隔离机制、状态管理 | tools/subagents.md, concepts/session-tool.md |
| `concepts/agent.md` | Agent 概念、工作区、运行时 | concepts/agent-loop.md, concepts/agent-workspace.md |
| `concepts/multi-agent.md` | 多 Agent 路由、隔离策略 | routing 配置, tools/subagents.md |

**架构理解路径**：
```
architecture.md (整体架构)
    ├── session.md (会话如何工作)
    ├── agent.md (Agent 是什么)
    ├── multi-agent.md (多 Agent 如何协作)
    └── memory.md (记忆系统)
```

#### 2.2 数据与状态

| 文档 | 作用 | 使用场景 |
|------|------|----------|
| `concepts/memory.md` | 记忆系统、文件存储、检索 | 需要长期记忆时 |
| `concepts/context.md` | 上下文管理、消息传递 | 理解对话流程 |
| `concepts/queue.md` | 消息队列、并发处理 | 高并发场景 |
| `concepts/streaming.md` | 流式响应机制 | 实时交互 |

#### 2.3 模型与AI

| 文档 | 内容 | 关联 |
|------|------|------|
| `concepts/models.md` | 模型配置、别名系统 | providers/ 目录 |
| `concepts/model-failover.md` | 故障转移机制 | models.md, gateway/health.md |
| `concepts/model-providers.md` | 提供商架构 | providers/*.md |
| `concepts/system-prompt.md` | 系统提示词 | agent 行为控制 |

---

### 第三层：渠道集成（Channels）

**目标用户**：需要连接特定聊天平台

#### 3.1 主流渠道

| 渠道 | 文档 | 特点 | 难度 |
|------|------|------|------|
| WhatsApp | `channels/whatsapp.md` | 最流行，需QR码登录 | ⭐⭐ |
| Telegram | `channels/telegram.md` | Bot友好，功能丰富 | ⭐ |
| Discord | `channels/discord.md` | 社区支持，线程功能 | ⭐⭐ |
| Slack | `channels/slack.md` | 企业环境，审批流程 | ⭐⭐⭐ |
| 飞书 | `channels/feishu.md` | 国内合规，功能完整 | ⭐⭐ |
| iMessage | `channels/imessage.md` | Apple生态，隐私好 | ⭐⭐⭐ |

#### 3.2 渠道通用文档

| 文档 | 作用 | 必读性 |
|------|------|--------|
| `channels/pairing.md` | 私信安全配对机制 | ⭐⭐⭐ 必须 |
| `channels/groups.md` | 群组消息处理 | ⭐⭐⭐ |
| `channels/channel-routing.md` | 渠道路由配置 | ⭐⭐ |
| `channels/troubleshooting.md` | 渠道问题排查 | 遇到问题 |

**渠道配置关系图**：
```
channels/pairing.md (安全基础)
    ↓
channels/[specific].md (具体渠道)
    ↓
    ├── 配置凭证
    ├── 测试连接
    └── 处理消息
```

---

### 第四层：工具系统（Tools）

**目标用户**：需要使用各种工具能力

#### 4.1 核心工具

| 工具 | 文档 | 用途 | 使用频率 |
|------|------|------|----------|
| **Skills** | `tools/skills.md` | 技能系统总览 | ⭐⭐⭐ 每天 |
| **Browser** | `tools/browser.md` | 浏览器自动化 | ⭐⭐⭐ 高频 |
| **Exec** | `tools/exec.md` | 命令执行 | ⭐⭐⭐ 高频 |
| **Web** | `tools/web.md` | 网页搜索 | ⭐⭐⭐ 高频 |
| **Subagents** | `tools/subagents.md` | 子Agent管理 | ⭐⭐ 常用 |
| **PDF** | `tools/pdf.md` | PDF处理 | ⭐⭐ 常用 |

#### 4.2 进阶工具

| 工具 | 文档 | 用途 |
|------|------|------|
| ACP Agents | `tools/acp-agents.md` | ACP协议Agent |
| Chrome Extension | `tools/chrome-extension.md` | 浏览器扩展 |
| Reactions | `tools/reactions.md` | 消息反应 |
| Thinking | `tools/thinking.md` | 思考模式 |

#### 4.3 Skill 开发

| 文档 | 作用 | 目标读者 |
|------|------|----------|
| `tools/creating-skills.md` | 创建Skill教程 | Skill开发者 |
| `tools/skills-config.md` | Skill配置详解 | 高级用户 |
| `clawhub.md` | Skill市场使用 | 所有用户 |

**工具使用路径**：
```
tools/skills.md (理解Skill系统)
    ↓
选择具体工具
    ├── browser.md → 网页操作
    ├── exec.md → 命令执行
    ├── web.md → 搜索信息
    └── subagents.md → 并行任务
```

---

### 第五层：Gateway 配置（Gateway）

**目标用户**：需要配置和管理 Gateway 服务

#### 5.1 基础配置

| 文档 | 核心内容 | 重要程度 |
|------|----------|----------|
| `gateway/configuration.md` | 配置总览和结构 | ⭐⭐⭐ |
| `gateway/protocol.md` | WebSocket协议详情 | ⭐⭐⭐ |
| `gateway/authentication.md` | 认证机制 | ⭐⭐⭐ |
| `gateway/pairing.md` | 设备配对 | ⭐⭐⭐ |

#### 5.2 安全与隔离

| 文档 | 内容 | 场景 |
|------|------|------|
| `gateway/sandboxing.md` | 沙箱机制 | 安全执行 |
| `gateway/security/index.md` | 安全指南 | 生产环境 |
| `gateway/secrets.md` | 密钥管理 | 凭证存储 |

#### 5.3 网络与访问

| 文档 | 用途 | 关联 |
|------|------|------|
| `gateway/remote.md` | 远程访问配置 | Tailscale, SSH |
| `gateway/tailscale.md` | Tailscale集成 | 推荐方案 |
| `gateway/network-model.md` | 网络架构 | 理解原理 |

#### 5.4 运维管理

| 文档 | 用途 | 频率 |
|------|------|------|
| `gateway/health.md` | 健康检查 | 日常 |
| `gateway/logging.md` | 日志管理 | 调试 |
| `gateway/troubleshooting.md` | 问题排查 | 故障时 |
| `gateway/doctor.md` | 诊断工具 | 有问题时 |

**Gateway 配置流程**：
```
gateway/configuration.md (基础配置)
    ├── authentication.md (设置认证)
    ├── pairing.md (设备配对)
    ├── sandboxing.md (配置沙箱)
    └── remote.md (远程访问)
```

---

### 第六层：CLI 命令（CLI）

**目标用户**：命令行用户

#### 6.1 核心命令

| 命令 | 文档 | 用途 | 频率 |
|------|------|------|------|
| `openclaw` | `cli/index.md` | CLI总览 | 参考 |
| `status` | `cli/status.md` | 查看状态 | ⭐⭐⭐ |
| `gateway` | `cli/gateway.md` | Gateway管理 | ⭐⭐⭐ |
| `message` | `cli/message.md` | 发送消息 | ⭐⭐ |
| `agent` | `cli/agent.md` | Agent操作 | ⭐⭐⭐ |
| `sessions` | `cli/sessions.md` | 会话管理 | ⭐⭐ |

#### 6.2 配置命令

| 命令 | 文档 | 用途 |
|------|------|------|
| `configure` | `cli/config.md` | 配置管理 |
| `skills` | `cli/skills.md` | Skill管理 |
| `models` | `cli/models.md` | 模型配置 |
| `memory` | `cli/memory.md` | 记忆管理 |

#### 6.3 系统命令

| 命令 | 文档 | 用途 |
|------|------|------|
| `health` | `cli/health.md` | 健康检查 |
| `doctor` | `cli/doctor.md` | 诊断修复 |
| `logs` | `cli/logs.md` | 日志查看 |
| `update` | `cli/update.md` | 更新管理 |

---

### 第七层：自动化（Automation）

**目标用户**：需要自动化工作流

| 文档 | 机制 | 适用场景 | 精度 |
|------|------|----------|------|
| `automation/cron-jobs.md` | 定时任务 | 定期执行 | 高 |
| `automation/heartbeat.md` | 心跳检查 | 周期性检查 | 低 |
| `automation/webhook.md` | Webhook | 事件驱动 | 即时 |
| `automation/hooks.md` | 钩子 | 生命周期事件 | 即时 |
| `automation/poll.md` | 轮询 | 状态监控 | 中 |

**自动化选择指南**：
```
需要精确时间？ ──▶ cron-jobs.md
需要事件触发？ ──▶ webhook.md / hooks.md
需要状态检查？ ──▶ heartbeat.md / poll.md
```

---

### 第八层：模型提供商（Providers）

**目标用户**：配置AI模型

| 提供商 | 文档 | 特点 |
|--------|------|------|
| OpenAI | `providers/openai.md` | GPT-4, GPT-4o |
| Anthropic | `providers/anthropic.md` | Claude 系列 |
| Moonshot | `providers/moonshot.md` | Kimi，中文优化 |
| Qwen | `providers/qwen.md` | 通义千问 |
| Ollama | `providers/ollama.md` | 本地部署 |
| OpenRouter | `providers/openrouter.md` | 统一接口 |

---

### 第九层：平台支持（Platforms）

**目标用户**：特定平台部署

| 平台 | 文档 | 场景 |
|------|------|------|
| macOS | `platforms/macos.md` | Mac应用 |
| Linux | `platforms/linux.md` | 服务器 |
| Windows | `platforms/windows.md` | WSL2 |
| iOS | `platforms/ios.md` | 移动节点 |
| Android | `platforms/android.md` | 移动节点 |
| Raspberry Pi | `platforms/raspberry-pi.md` | 边缘设备 |

---

### 第十层：参考模板（Reference）

**目标用户**：配置工作区

| 模板 | 文档 | 用途 |
|------|------|------|
| AGENTS.md | `reference/templates/AGENTS.md` | Agent行为规范 |
| TOOLS.md | `reference/templates/TOOLS.md` | 工具配置 |
| SOUL.md | `reference/templates/SOUL.md` | Agent人格 |
| USER.md | `reference/templates/USER.md` | 用户信息 |
| IDENTITY.md | `reference/templates/IDENTITY.md` | Agent身份 |
| BOOTSTRAP.md | `reference/templates/BOOTSTRAP.md` | 首次引导 |
| HEARTBEAT.md | `reference/templates/HEARTBEAT.md` | 心跳任务 |

---

## 🔗 文档依赖关系图

### 核心依赖链

```
┌─────────────────────────────────────────────────────────────────┐
│                        核心依赖链                                │
└─────────────────────────────────────────────────────────────────┘

1. 入门链：
   index → getting-started → wizard → setup → [具体配置]

2. 架构链：
   architecture → session → agent → multi-agent → memory

3. 配置链：
   configuration → authentication → pairing → sandboxing → security

4. 渠道链：
   pairing → [specific-channel] → channel-routing → groups

5. 工具链：
   skills → [specific-tool] → creating-skills → clawhub

6. 运维链：
   gateway → health → logging → troubleshooting → doctor
```

### 横向关联

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Channels  │◄───►│   Gateway   │◄───►│   Tools     │
└─────────────┘     └─────────────┘     └─────────────┘
       ▲                   ▲                   ▲
       │                   │                   │
       └───────────────────┴───────────────────┘
                   │
            ┌─────────────┐
            │   Session   │
            │   & Agent   │
            └─────────────┘
```

---

## 📖 推荐阅读路径

### 路径1：完全新手（零基础）

```
Day 1:
  ├─ index.md (30分钟) - 了解是什么
  └─ getting-started.md (1小时) - 跟着安装

Day 2:
  ├─ wizard.md (30分钟) - 理解向导
  ├─ channels/pairing.md (20分钟) - 安全基础
  └─ [选择一个渠道].md (30分钟) - 连接第一个渠道

Day 3:
  ├─ tools/skills.md (20分钟) - 了解Skill系统
  ├─ tools/browser.md (30分钟) - 浏览器自动化
  └─ tools/exec.md (20分钟) - 命令执行
```

### 路径2：开发者（想开发Skill）

```
Week 1:
  ├─ concepts/architecture.md - 理解架构
  ├─ concepts/session.md - 会话机制
  ├─ concepts/agent.md - Agent概念
  └─ tools/creating-skills.md - Skill开发

Week 2:
  ├─ tools/skills-config.md - 高级配置
  ├─ clawhub.md - 发布Skill
  └─ reference/templates/*.md - 工作区模板
```

### 路径3：运维工程师（生产部署）

```
Priority 1:
  ├─ gateway/configuration.md - 配置详解
  ├─ gateway/authentication.md - 认证安全
  ├─ gateway/sandboxing.md - 沙箱机制
  └─ gateway/security/index.md - 安全指南

Priority 2:
  ├─ gateway/remote.md - 远程访问
  ├─ gateway/tailscale.md - 网络方案
  ├─ automation/cron-jobs.md - 自动化
  └─ cli/health.md, cli/doctor.md - 运维工具
```

### 路径4：多Agent架构师

```
Core:
  ├─ concepts/multi-agent.md - 多Agent设计
  ├─ concepts/agent-workspace.md - 工作区隔离
  ├─ tools/subagents.md - 子Agent管理
  └─ routing 配置 - 路由规则

Advanced:
  ├─ concepts/queue.md - 消息队列
  ├─ concepts/streaming.md - 流式处理
  └─ gateway/protocol.md - 协议细节
```

---

## 🎯 文档使用速查

### 遇到问题时的查阅顺序

```
1. 功能不会用？
   → tools/[功能].md

2. 配置出错？
   → gateway/configuration.md
   → gateway/troubleshooting.md

3. 渠道连不上？
   → channels/[渠道].md
   → channels/troubleshooting.md
   → gateway/doctor.md

4. Agent不响应？
   → cli/status.md
   → cli/health.md
   → gateway/health.md

5. 安全问题？
   → gateway/security/index.md
   → channels/pairing.md

6. 性能问题？
   → concepts/session-pruning.md
   → gateway/logging.md
```

---

## 📚 文档质量评估

| 类别 | 完整度 | 准确性 | 实用性 | 维护状态 |
|------|--------|--------|--------|----------|
| 入门文档 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 活跃 |
| 概念文档 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 活跃 |
| 渠道文档 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 活跃 |
| 工具文档 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 活跃 |
| Gateway文档 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 活跃 |
| CLI文档 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 活跃 |
| 自动化文档 | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 一般 |
| 提供商文档 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 活跃 |

---

## 🔍 关键概念索引

| 概念 | 定义 | 主要文档 | 相关文档 |
|------|------|----------|----------|
| **Gateway** | 核心网关服务，连接所有渠道和客户端 | gateway/index.md | architecture.md, configuration.md |
| **Session** | 对话会话，隔离不同用户和上下文 | concepts/session.md | session-tool.md, cli/sessions.md |
| **Agent** | AI智能体，执行任务的实体 | concepts/agent.md | agent-loop.md, agent-workspace.md |
| **Skill** | 功能模块，扩展Agent能力 | tools/skills.md | creating-skills.md, skills-config.md |
| **Channel** | 消息渠道，如WhatsApp、Telegram | channels/index.md | [specific-channel].md, pairing.md |
| **Pairing** | 设备配对，安全认证机制 | channels/pairing.md | gateway/pairing.md, authentication.md |
| **Sandbox** | 沙箱环境，安全执行隔离 | gateway/sandboxing.md | exec.md, security/index.md |
| **Memory** | 记忆系统，长期存储 | concepts/memory.md | memory.md (cli) |

---

## 📝 版本信息

- **文档版本**: 基于 OpenClaw 官方文档 2026-04-04
- **文档总数**: 387 个 (英文203 + 中文184)
- **最后更新**: 2026-04-04
- **解读作者**: AI Assistant

---

## 💡 使用建议

1. **新手**: 按"推荐阅读路径"顺序阅读，不要跳跃
2. **开发者**: 重点理解 concepts/ 和 tools/creating-skills.md
3. **运维**: 重点掌握 gateway/ 和 cli/ 文档
4. **遇到问题**: 使用"问题查阅顺序"快速定位
5. **定期回顾**: 概念文档值得反复阅读，加深理解