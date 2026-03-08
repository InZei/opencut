# OpenCut Skills 使用指南

## 📖 什么是 OpenCut Skills？

OpenCut Skills 是一套专门为 AI 助手（如 Claude Code、Cursor 等）设计的技能说明文件，用于指导 AI 如何正确、规范地使用 OpenCut API 来创建视频。

类似于 [Remotion Skills](https://github.com/remotion-dev/remotion/tree/main/packages/skills)，但针对 Python 和 OpenCut 项目进行了优化。

## 🎯 技能列表

### 1. create-video
**用途：** 学习如何使用 OpenCut 创建视频

**触发场景：**
- 用户想要创建视频
- 需要理解 Composition、Sequence、Clip API
- 想要添加 HTML 动画、音频或视频片段
- 寻找最佳实践和常用模式

**文件位置：** `skills/create-video/SKILL.md`

### 2. use-extensions
**用途：** 掌握 OpenCut 扩展包的使用

**触发场景：**
- 添加场景转场效果（淡入淡出、滑动、缩放）
- 使用 Google Fonts 或自定义字体
- 创建 Three.js 3D 动画
- 渲染 SVG 图形
- 使用 Tailwind CSS 进行样式设计
- 添加 SRT/VTT 字幕

**文件位置：** `skills/use-extensions/SKILL.md`

### 3. debug-rendering
**用途：** 调试和解决渲染问题

**触发场景：**
- 遇到渲染错误或失败
- 输出视频出现黑屏或丢帧
- 音视频同步问题
- 性能问题（渲染缓慢）
- Playwright 浏览器问题
- 视频编解码器或导出错误

**文件位置：** `skills/debug-rendering/SKILL.md`

## 🚀 如何使用

### 对于 AI 助手

1. **自动检测**
   - AI 助手会自动检测 `skills/` 目录
   - 根据用户请求的关键词自动触发相应技能
   - 技能会指导 AI 按照最佳实践完成任务

2. **触发机制**
   - 用户提到"创建视频" → `create-video` 技能激活
   - 用户询问"转场/字体/字幕" → `use-extensions` 技能激活
   - 用户报告"错误/问题" → `debug-rendering` 技能激活

3. **技能执行**
   - AI 读取技能的 SKILL.md 文件
   - 按照技能中的步骤和示例执行
   - 遵循最佳实践和注意事项

### 对于人类用户

这些技能同时也是完整的技术文档：

- **教程** - 每个主题的逐步指南
- **示例** - 可直接使用的代码片段
- **故障排除** - 常见问题和解决方案
- **最佳实践** - 推荐的模式和流程

## 📁 技能结构

```
skills/
├── README.md                 # 技能总览（本文件）
├── skills.json               # 技能索引（供 AI 读取）
├── create-video/
│   └── SKILL.md             # 视频创建技能
├── use-extensions/
│   └── SKILL.md             # 扩展包使用技能
└── debug-rendering/
    └── SKILL.md             # 调试技能
```

### SKILL.md 结构

每个技能的 SKILL.md 包含：

```markdown
---
name: skill-name              # 技能标识符
description: |                # 技能描述（触发机制）
  何时使用此技能
compatibility:                # 兼容性要求
  - python: "3.12+"
---

# 技能内容

## 核心概念
...

## 逐步指南
...

## 示例代码
...

## 最佳实践
...

## 故障排除
...
```

## 💡 使用示例

### 示例 1：创建简单视频

**用户请求：** "我想创建一个带 HTML 动画的视频"

**AI 响应流程：**
1. 触发 `create-video` 技能
2. 读取技能文档
3. 按照技能指导创建视频：

```python
from opencut import Composition, Sequence, HTMLClip, render

# 创建 Composition
comp = Composition(
    fps=30,
    duration_in_frames=300,  # 10 秒
    width=1920,
    height=1080
)

# 添加 HTML 层
comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=HTMLClip(src="index.html")
))

# 渲染视频
render(comp, output="output.mp4")
```

### 示例 2：添加转场效果

**用户请求：** "如何在场景之间添加淡入淡出转场？"

**AI 响应流程：**
1. 触发 `use-extensions` 技能
2. 查找转场相关章节
3. 提供 CrossFade 使用示例：

```python
from opencut import Composition, Sequence
from opencut.extensions import CrossFade

comp = Composition(fps=30, duration_in_frames=330, width=1920, height=1080)

# 场景 1
comp.add(Sequence(
    start_frame=0,
    duration=150,
    component=HTMLClip(src="scene1.html")
))

# 转场
comp.add(Sequence(
    start_frame=150,
    duration=30,
    component=CrossFade(
        from_scene="scene1.html",
        to_scene="scene2.html",
        duration=30
    )
))

# 场景 2
comp.add(Sequence(
    start_frame=180,
    duration=150,
    component=HTMLClip(src="scene2.html")
))
```

### 示例 3：调试黑屏问题

**用户请求：** "我的视频完全是黑的，怎么回事？"

**AI 响应流程：**
1. 触发 `debug-rendering` 技能
2. 按照调试流程排查
3. 提供诊断步骤：

```python
# 1. 检查 HTML 文件是否存在
import os
html_path = os.path.abspath("index.html")
print(f"HTML 存在：{os.path.exists(html_path)}")

# 2. 验证 window.renderFrame 是否定义
# 检查 HTML 中是否包含 window.renderFrame 函数

# 3. 在浏览器中测试
# 打开 HTML 文件并检查控制台错误

# 4. 使用绝对路径
comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=HTMLClip(src=html_path)
))
```

## 🔧 创建新技能

如果你想添加新技能：

### 步骤 1：创建目录

```bash
mkdir skills/your-skill-name
```

### 步骤 2：编写 SKILL.md

```markdown
---
name: your-skill-name
description: |
  技能描述 - 何时使用、做什么
compatibility:
  - python: "3.12+"
---

# 技能标题

## 概述
简要说明技能用途

## 核心概念
解释相关概念

## 逐步指南
提供 step-by-step 指导

## 示例代码
包含完整的代码示例

## 最佳实践
列出最佳实践和注意事项

## 常见问题
FAQ 和故障排除
```

### 步骤 3：更新 skills.json

```json
{
  "name": "your-skill-name",
  "path": "your-skill-name/SKILL.md",
  "description": "技能描述",
  "triggers": ["关键词 1", "关键词 2"],
  "compatibility": {
    "python": "3.12+"
  }
}
```

### 步骤 4：测试技能

- 让 AI 助手执行相关任务
- 验证技能是否正确触发
- 检查输出是否符合预期

## 📊 技能覆盖范围

这些技能覆盖了 OpenCut 的完整工作流：

```
视频创建流程
    ↓
1. create-video       → 基础视频创建
    ↓
2. use-extensions     → 高级功能
    ↓
3. debug-rendering    → 问题排查（如需要）
```

### 功能覆盖矩阵

| 功能 | create-video | use-extensions | debug-rendering |
|------|--------------|----------------|-----------------|
| Composition 设置 | ✅ | | ✅ |
| HTML 动画 | ✅ | ✅ (Tailwind) | ✅ |
| 音频 | ✅ | | ✅ |
| 视频占位符 | ✅ | | ✅ |
| 转场 | | ✅ | |
| 字体 | | ✅ | |
| Three.js | | ✅ | |
| SVG | | ✅ | |
| 字幕 | | ✅ | |
| 性能优化 | | | ✅ |
| 错误处理 | | | ✅ |

## 🎓 学习路径

### 初学者
1. 从 `create-video` 开始
2. 学习基本概念和 API
3. 创建第一个视频

### 进阶用户
1. 学习 `use-extensions`
2. 掌握扩展包使用
3. 创建复杂效果

### 遇到问题
1. 查阅 `debug-rendering`
2. 按照流程排查
3. 解决问题

## 🤝 贡献指南

想要改进或添加新技能？

1. **Fork 仓库**
2. **编辑技能** - 更新或创建 SKILL.md
3. **测试** - 用实际用例验证
4. **提交 PR** - 分享你的改进

### 贡献要求

- 技能聚焦于单一主题
- 使用清晰简洁的语言
- 包含可运行的代码示例
- 记录常见陷阱
- 链接到相关技能
- API 变更时更新示例

## 📚 其他资源

- **主文档：** [README.md](../README.md)
- **示例项目：** [examples/](../examples)
- **API 参考：** [opencut/](../opencut)
- **扩展包：** [opencut/extensions/](../opencut/extensions)

## 📬 支持

- **GitHub Issues:** https://github.com/InZei/opencut/issues
- **讨论区:** https://github.com/InZei/opencut/discussions

---

<div align="center">

**OpenCut Skills - 让视频创作像写代码一样简单**

由 InZei 用 ❤️ 创建

</div>
