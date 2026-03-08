# OpenCut Skills 快速开始

## 🎯 什么是 OpenCut Skills？

OpenCut Skills 是一套为 AI 助手设计的技能文档，指导 AI 如何正确使用 OpenCut API 创建视频。

**灵感来源：** [Remotion Skills](https://github.com/remotion-dev/remotion/tree/main/packages/skills)

**适用对象：** Claude Code、Cursor 等 AI 编程助手

## 📚 技能列表

### 1. create-video - 创建视频
**文件：** [`create-video/SKILL.md`](create-video/SKILL.md)

**何时触发：**
- 创建新视频项目
- 学习 Composition、Sequence、Clip API
- 添加 HTML 动画、音频、视频
- 寻找最佳实践

**包含内容：**
- ✅ 核心概念（Composition、Sequence、Clip）
- ✅ 逐步工作流程
- ✅ 完整示例代码
- ✅ 高级模式（多场景、AI 生成、社交媒体）
- ✅ 常见问题解决

### 2. use-extensions - 使用扩展包
**文件：** [`use-extensions/SKILL.md`](use-extensions/SKILL.md)

**何时触发：**
- 添加转场效果（淡入淡出、滑动、缩放）
- 使用 Google Fonts 或自定义字体
- 创建 Three.js 3D 动画
- 渲染 SVG 图形
- 使用 Tailwind CSS
- 添加 SRT/VTT 字幕

**包含内容：**
- ✅ 6 个扩展包的完整文档
- ✅ 每个扩展的使用示例
- ✅ 参数说明和配置选项
- ✅ 组合使用多个扩展

### 3. debug-rendering - 调试渲染
**文件：** [`debug-rendering/SKILL.md`](debug-rendering/SKILL.md)

**何时触发：**
- 渲染错误或失败
- 黑屏或丢帧
- 音视频同步问题
- 性能问题（渲染慢）
- Playwright 浏览器问题
- 视频编解码器错误

**包含内容：**
- ✅ 系统化调试流程
- ✅ 6 大类常见问题及解决方案
- ✅ 调试工具（帧检查器、音频可视化、性能分析）
- ✅ 错误消息快速参考表

## 🚀 如何使用

### 对于 AI 助手

1. **自动触发**
   - AI 会自动检测 `skills/` 目录
   - 根据用户请求关键词触发相应技能
   - 按照技能文档指导完成任务

2. **触发关键词示例**

| 用户请求 | 触发技能 |
|---------|---------|
| "创建视频" | create-video |
| "添加转场" | use-extensions |
| "黑屏问题" | debug-rendering |
| "如何使用字体" | use-extensions |
| "渲染很慢" | debug-rendering |

### 对于人类用户

这些技能同时也是完整的技术文档：

- 📖 **教程** - 逐步指南
- 💻 **示例** - 可直接使用的代码
- 🔧 **故障排除** - 常见问题解决方案
- ✨ **最佳实践** - 推荐的做法

## 📁 目录结构

```
skills/
├── README.md              # 技能总览（英文）
├── USAGE.md               # 使用指南（中文）
├── QUICKSTART.md          # 快速开始（本文件）
├── skills.json            # 技能索引
├── create-video/
│   └── SKILL.md          # 视频创建技能
├── use-extensions/
│   └── SKILL.md          # 扩展包使用技能
└── debug-rendering/
    └── SKILL.md          # 调试技能
```

## 💡 使用示例

### 示例 1：创建简单视频

```python
# 触发技能：create-video
from opencut import Composition, Sequence, HTMLClip, render

comp = Composition(
    fps=30,
    duration_in_frames=300,  # 10 秒
    width=1920,
    height=1080
)

comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=HTMLClip(src="index.html")
))

render(comp, output="output.mp4")
```

### 示例 2：添加转场

```python
# 触发技能：use-extensions
from opencut import Composition, Sequence
from opencut.extensions import CrossFade

comp = Composition(fps=30, duration_in_frames=330, width=1920, height=1080)

# 场景 1
comp.add(Sequence(
    start_frame=0,
    duration=150,
    component=HTMLClip(src="scene1.html")
))

# 淡入淡出转场
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

### 示例 3：调试黑屏

```python
# 触发技能：debug-rendering
import os

# 1. 检查 HTML 文件
html_path = os.path.abspath("index.html")
print(f"HTML 存在：{os.path.exists(html_path)}")

# 2. 验证 window.renderFrame
# 确保 HTML 中包含：
# window.renderFrame = function(frame) { ... }

# 3. 使用绝对路径
comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=HTMLClip(src=html_path)
))
```

## 🎓 学习路径

### 初学者
1. 阅读 `create-video/SKILL.md`
2. 学习基本概念和 API
3. 创建第一个视频

### 进阶用户
1. 阅读 `use-extensions/SKILL.md`
2. 掌握扩展包使用
3. 创建复杂效果

### 遇到问题
1. 阅读 `debug-rendering/SKILL.md`
2. 按照调试流程排查
3. 解决问题

## 🔧 创建新技能

想添加新技能？

### 步骤

1. **创建目录**
   ```bash
   mkdir skills/your-skill-name
   ```

2. **编写 SKILL.md**
   ```markdown
   ---
   name: your-skill-name
   description: |
     技能描述 - 何时使用、做什么
   compatibility:
     - python: "3.12+"
   ---
   
   # 技能内容
   ...
   ```

3. **更新 skills.json**
   ```json
   {
     "name": "your-skill-name",
     "path": "your-skill-name/SKILL.md",
     "description": "技能描述",
     "triggers": ["关键词"]
   }
   ```

4. **测试**
   - 让 AI 执行相关任务
   - 验证技能正确触发
   - 检查输出符合预期

## 📊 技能覆盖

```
视频创作完整流程
    ↓
1. create-video       → 基础创建
    ↓
2. use-extensions     → 高级功能
    ↓
3. debug-rendering    → 问题排查
```

### 功能覆盖矩阵

| 功能 | create-video | use-extensions | debug-rendering |
|------|--------------|----------------|-----------------|
| Composition | ✅ | | ✅ |
| HTML 动画 | ✅ | ✅ | ✅ |
| 音频 | ✅ | | ✅ |
| 视频 | ✅ | | ✅ |
| 转场 | | ✅ | |
| 字体 | | ✅ | |
| Three.js | | ✅ | |
| SVG | | ✅ | |
| 字幕 | | ✅ | |
| 性能 | | | ✅ |
| 错误 | | | ✅ |

## 🤝 贡献

欢迎贡献新技能或改进现有技能！

### 贡献指南

- 技能聚焦单一主题
- 语言清晰简洁
- 包含可运行示例
- 记录常见陷阱
- 链接相关技能
- API 变更时更新

### 提交步骤

1. Fork 仓库
2. 编辑/创建 SKILL.md
3. 测试验证
4. 提交 PR

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

**OpenCut Skills - 让 AI 帮你创作视频**

由 InZei 用 ❤️ 创建

</div>
