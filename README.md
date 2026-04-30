<p align="center"><img src= "https://github.com/user-attachments/assets/eca9a9ec-8534-4615-9e0f-96c5ac1d10a3" alt="CowAgent" width="550" /></p>

<p align="center">
  <a href="https://github.com/zhayujie/CowAgent/releases/latest"><img src="https://img.shields.io/github/v/release/zhayujie/CowAgent" alt="Latest release"></a>
  <a href="https://github.com/zhayujie/CowAgent/blob/master/LICENSE"><img src="https://img.shields.io/github/license/zhayujie/CowAgent" alt="License: MIT"></a>
  <a href="https://github.com/zhayujie/CowAgent"><img src="https://img.shields.io/github/stars/zhayujie/CowAgent?style=flat-square" alt="Stars"></a> <br/>
  [中文] | [<a href="docs/en/README.md">English</a>] | [<a href="docs/ja/README.md">日本語</a>]
</p>

**CowAgent** 是基于大模型的超级 AI 助理，能够主动思考和任务规划、操作计算机和外部资源、创造和执行 Skills、拥有长期记忆和知识库并不断成长，比 OpenClaw 更轻量和便捷。CowAgent 支持灵活切换多种模型，能处理文本、语音、图片、文件等多模态消息，可接入微信、飞书、钉钉、企微智能机器人、QQ、企微自建应用、微信公众号、网页中使用，7*24小时运行于你的个人电脑或服务器中。

<p align="center">
  <a href="https://cowagent.ai/">🌐 官网</a> &nbsp;·&nbsp;
  <a href="https://docs.cowagent.ai/">📖 文档中心</a> &nbsp;·&nbsp;
  <a href="https://docs.cowagent.ai/guide/quick-start">🚀 快速开始</a> &nbsp;·&nbsp;
  <a href="https://skills.cowagent.ai/">🧩 技能广场</a> &nbsp;·&nbsp;
  <a href="https://link-ai.tech/cowagent/create">☁️ 在线体验</a>
</p>


# 简介

> 该项目既是一个可以开箱即用的超级 AI 助理，也是一个支持高扩展的 Agent 框架，可以通过为项目扩展大模型接口、接入渠道、内置工具、Skills 系统来灵活实现各种定制需求。核心能力如下：

-  ✅  **自主任务规划**：能够理解复杂任务并自主规划执行，持续思考和调用工具直到完成目标
-  ✅  **长期记忆：** 自动将对话记忆持久化至本地文件和数据库中，包括核心记忆、日级记忆和梦境蒸馏，支持关键词及向量检索
-  ✅  **个人知识库：** 自动整理结构化知识，通过交叉引用构建知识图谱，支持通过对话管理和可视化浏览知识库
-  ✅  **技能系统：** Skills 安装和运行的引擎，支持从 [Skill Hub](https://skills.cowagent.ai/)、GitHub 等一键安装技能，或通过对话创造 Skills
-  ✅  **工具系统：** 内置文件读写、终端执行、浏览器操作、定时任务等工具，Agent 自主调用以完成复杂任务
-  ✅  **CLI系统：** 提供终端命令和对话命令，支持进程管理、技能安装、配置修改等操作
-  ✅  **多模态消息：** 支持对文本、图片、语音、文件等多类型消息进行解析、处理、生成、发送等操作
-  ✅  **多模型支持：** 支持 DeepSeek、MiniMax、Claude、Gemini、OpenAI、GLM、Qwen、Doubao、Kimi 等国内外主流模型厂商
-  ✅  **多通道接入：** 支持运行在本地计算机或服务器，可集成到微信、飞书、钉钉、企业微信、QQ、微信公众号、网页中使用

## 个人使用说明

> 这是我个人学习用的 fork，主要用于研究 Agent 框架的实现原理。如需正式使用，请访问[上游仓库](https://github.com/zhayujie/CowAgent)。

**学习笔记：**
- 重点关注 `agent/` 目录下的任务规划和工具调用逻辑
- 记忆模块的向量检索实现值得深入研究（`memory/` 目录）
- 本地测试主要使用 DeepSeek 模型，成本较低适合实验
- 工具调用链路：`agent/core.py` → `tools/executor.py`，值得跟踪调试一遍

## 声明

1. 本项目遵循 [MIT 开源协议](/LICENSE)，主要用于技术研究和学习，使用本项目时需遵守所在地法律法规、相关政策以及企业章程，禁止用于任何违法或侵犯他人权益的行为。任何个人、团队和企业，无论以何种方式使用该项目、对何对象提供服务，所产生的一切后果，本项目均不承担任何责任。
2. 成本与安全：Agent 模式下 Token 使用量高于普通对话模式，请根据效果及成本综合选择模型。Agent 具有访问所在操作系统的能力，请谨慎选择项目部署环境。同时项目也会持续升级安全机制、并降低模型消耗成本。
3. CowAgent 项目专注于开源技术开发，不会参与、授权或发行任何加密货币。

## 演示

- 使用说明( Agent 模式)：[CowAgent 介绍](https://docs.cowagent.ai/intro/features)

- 免部署在线体验：[CowAgent](https://link-ai.tech/cowagent/create)

- DEMO 视频(对话模式)：https://cdn.link-ai.tech/doc/cow_demo.mp4

## 社区

添加小助手微信加入开源项目交流群：

<img width="140" src="https://img-1317903499.cos.ap-guangzhou.myqcloud.com/docs/open-community.png">

<br/>

# 企业服务

<a href="https://link-ai.tech" target="_blank"><img width="650" src="https://cdn.link-ai.tech/image/link-ai-intro.jpg"></a>

> [LinkAI](https:
