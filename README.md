# OpenCut

<div align="center">

**🎬 Programmatic Video Creation with HTML/CSS/JS**  
**🎬 用 HTML/CSS/JS 创作视频的编程式框架**

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Python Version of Remotion | Declarative Animation | Frame-Accurate Control | Programmable Video**  
**Remotion 的 Python 版本 | 声明式动画 | 帧级控制 | 可编程视频**

[📖 English Docs](#-features) · [📖 中文文档](#-功能亮点)

</div>

---

## 🌟 Features | 功能亮点

### ✨ Core Features | 核心特性

| English | 中文 |
|---------|------|
| **🎨 HTML/CSS/JS Animation** - Create video content using modern web technologies, full support for CSS animations, Canvas, WebGL | **🎨 HTML/CSS/JS 动画** - 使用现代 Web 技术栈创建视频内容，支持所有 CSS 动画、Canvas、WebGL |
| **⚡ Frame-Accurate Control** - Per-frame animation control via `window.renderFrame(frame)` hook | **⚡ 帧级精确控制** - 通过 `window.renderFrame(frame)` 钩子实现逐帧动画控制 |
| **🎵 Audio Composition** - Multi-track audio mixing, volume control, fade in/out | **🎵 音频合成** - 支持多轨道音频混合、音量调节、淡入淡出 |
| **🎬 Video Placeholder** - Reserved OpenCV video compositing interface for background video overlay | **🎬 Video 占位符机制** - 预留 OpenCV 视频合成接口，支持背景视频叠加 |
| **🔧 Declarative API** - Composition → Sequence → Clip architecture inspired by Remotion | **🔧 声明式 API** - 受 Remotion 启发的 Composition → Sequence → Clip 三层架构 |
| **🚀 Programmable Generation** - Perfect for AI generation, data visualization, batch video production | **🚀 可编程生成** - 完美适配 AI 生成、数据可视化、批量视频制作场景 |

### 🎯 Use Cases | 适用场景

- 📊 **Data Visualization Videos** - Dynamic charts, real-time data display | **数据可视化视频** - 动态图表、实时数据展示
- 🤖 **AI-Generated Content** - Batch marketing videos with LLM | **AI 生成内容** - 结合 LLM 批量生成营销视频
- 📱 **Social Media Automation** - Programmatic short video generation | **社交媒体自动化** - 程序化生成短视频内容
- 🎓 **Educational Video Production** - Code demos, tutorial animations | **教育视频制作** - 代码演示、教程动画
- 📈 **Marketing Asset Generation** - Personalized ad video batch production | **营销素材生成** - 个性化广告视频批量生产

### 💡 Why OpenCut? | 为什么选择 OpenCut？

> **"If you can code it, you can video it"**  
> **"如果你能用代码描述它，就能用它制作视频"**

- **Frontend-Friendly** - Reuse existing HTML/CSS skills and component libraries  
  **前端友好** - 复用现有 HTML/CSS 技能和组件库
- **Python Ecosystem** - Seamless integration with NumPy, Pandas, AI models  
  **Python 生态** - 无缝集成 NumPy、Pandas、AI 模型
- **Version Control** - Video as Code, Git-manageable  
  **版本控制** - 视频即代码，支持 Git 管理
- **Testability** - Unit tests, CI/CD automation  
  **可测试性** - 单元测试、CI/CD 自动化
- **Zero Learning Curve** - Remotion users can migrate seamlessly  
  **零学习成本** - Remotion 用户可无缝迁移

---

## 🚀 Quick Start | 快速开始

### 1️⃣ Install Dependencies | 安装依赖

```bash
# Clone repository | 克隆项目
git clone https://github.com/InZei/opencut.git
cd opencut

# Create virtual environment (recommended) | 创建虚拟环境（推荐）
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux

# Install dependencies (use Chinese mirror for faster download) | 安装依赖（使用国内镜像加速）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2️⃣ Install Browser | 安装浏览器

```bash
# Install Playwright Chromium with Chinese mirror | 使用国内镜像安装 Playwright Chromium
$env:PLAYWRIGHT_DOWNLOAD_HOST="https://npmmirror.com/mirrors/playwright/"
playwright install chromium
```

### 3️⃣ Run Examples | 运行示例

```bash
# Hello World - Basic animation | 基础动画示例
cd examples/hello_world
python main.py
# Output: output.mp4 (1920x1080, 5 seconds)

# Audio Demo - Audio composition | 音频合成示例
cd examples/audio_demo
python main.py

# Video Placeholder - Video placeholder example | 视频占位符示例
cd examples/video_placeholder
python main.py
```

---

## 📖 Core API | 核心 API

### Composition - Canvas Configuration | 画布配置

Define video basic parameters | 定义视频的基本参数：

```python
from opencut import Composition

comp = Composition(
    fps=30,                    # Frame rate | 帧率
    duration_in_frames=300,    # Total frames (300 frames = 10s @ 30fps) | 总帧数
    width=1920,                # Width | 宽度
    height=1080                # Height | 高度
)
```

### Sequence - Timeline Segments | 时间轴片段

Add layers on timeline | 在时间轴上添加图层：

```python
from opencut import Sequence, HTMLClip

# Add HTML animation layer (start from frame 0, duration 300 frames)
# 添加 HTML 动画层（从第 0 帧开始，持续 300 帧）
comp.add(
    Sequence(
        start_frame=0,
        duration=300,
        component=HTMLClip(src="index.html")
    )
)

# Add audio layer (start from frame 50)
# 添加音频层（从第 50 帧开始）
comp.add(
    Sequence(
        start_frame=50,
        duration=250,
        component=AudioClip(src="music.mp3", volume=0.8)
    )
)
```

### Clips - Component Types | 组件类型

Three core components | 三种核心组件：

```python
from opencut import HTMLClip, VideoClip, AudioClip

# HTML Component - Render HTML/CSS/JS animation
# HTML 组件 - 渲染 HTML/CSS/JS 动画
HTMLClip(
    src="index.html",          # HTML file path | HTML 文件路径
    props={"color": "red"}     # Props passed to HTML | 传递给 HTML 的参数
)

# Video Component - Placeholder mechanism (OpenCV compositing pending)
# 视频组件 - 占位符机制（待 OpenCV 合成）
VideoClip(
    src="background.mp4",      # Video file | 视频文件
    bind_id="main_video"       # Bind to placeholder ID in HTML | 绑定 HTML 中的占位符 ID
)

# Audio Component - Background music / Sound effects
# 音频组件 - 背景音乐/音效
AudioClip(
    src="music.mp3",           # Audio file | 音频文件
    volume=1.0,                # Volume (0.0-1.0) | 音量
    start_time=0               # Start time in seconds | 起始时间（秒）
)
```

### Render - Export Video | 渲染输出

Export final video | 导出最终视频：

```python
from opencut import render

output_path = render(comp, output="output.mp4")
print(f"Video generated: {output_path} | 视频已生成：{output_path}")
```

---

## 💻 Complete Example | 完整示例

### Hello World - Fade-in Animation | 淡入动画

**Python Code | Python 代码：**
```python
from opencut import Composition, Sequence, HTMLClip, render

# Create Composition | 创建 Composition
comp = Composition(
    fps=30,
    duration_in_frames=150,  # 5 seconds | 5 秒
    width=1920,
    height=1080
)

# Add HTML animation | 添加 HTML 动画
comp.add(Sequence(
    start_frame=0,
    duration=150,
    component=HTMLClip(src="index.html")
))

# Render | 渲染
render(comp, output="output.mp4")
```

**HTML Animation | HTML 动画 (index.html)：**
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        #box {
            width: 200px;
            height: 200px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
    </style>
</head>
<body>
    <div id="box"></div>
    <script>
        // Frame render hook | 帧渲染钩子
        window.renderFrame = function(frame) {
            const box = document.getElementById('box');
            // Fade-in: opacity 0→1 in frames 0-30 | 淡入效果：0-30 帧从透明到不透明
            box.style.opacity = Math.min(1, frame / 30);
            // Rotation: continuous spin | 旋转效果：持续旋转
            box.style.transform = `translate(-50%, -50%) rotate(${frame * 2}deg)`;
        }
    </script>
</body>
</html>
```

---

## 🏗️ Architecture | 架构设计

### Rendering Pipeline | 渲染流程

```
User calls render() | 用户调用 render()
    ↓
1. Start local HTTP server (localhost:8000) | 启动本地 HTTP 服务器
    ↓
2. Playwright loads HTML and renders frames | Playwright 加载 HTML 并逐帧渲染
    ↓
3. Call window.renderFrame(frame) per frame | 每帧调用 window.renderFrame(frame)
    ↓
4. Capture transparent PNG sequence | 捕获透明背景 PNG 序列
    ↓
5. Extract Video placeholder coordinates | 提取 Video 占位符坐标信息
    ↓
6. MoviePy composites audio → MP4 output | MoviePy 合成音频 → MP4 输出
    ↓
7. (Future) OpenCV composites video layer | (未来) OpenCV 合成视频层
```

### Tech Stack | 技术栈

| Component | Technology | Description |
|-----------|------------|-------------|
| **HTML Rendering** | Playwright | Headless browser renders HTML/CSS/JS |
| **Video Compositing** | MoviePy | Image sequence + audio |
| **Video Processing** | OpenCV (Reserved) | Video frame compositing, transitions |
| **HTTP Server** | http.server | Local static file serving |

### Comparison with Remotion | 与 Remotion 对比

| Feature | Remotion | OpenCut |
|---------|----------|---------|
| Language | TypeScript/React | Python |
| Rendering Engine | Puppeteer | Playwright |
| Video Compositing | FFmpeg | MoviePy + OpenCV |
| Audio Processing | FFmpeg | MoviePy |
| Use Case | Frontend Development | AI/Automation/Data Science |
| Learning Curve | Requires React | Zero Learning Curve |

---

## 📁 Project Structure | 项目结构

```
opencut/
├── opencut/                    # Python package | Python 包
│   ├── __init__.py             # Public API exports | 公共 API 导出
│   ├── core/                   # Core data structures | 核心数据结构
│   │   ├── composition.py      # Composition class
│   │   ├── sequence.py         # Sequence class
│   │   └── clips.py            # HTMLClip, VideoClip, AudioClip
│   ├── renderer/               # Rendering engine | 渲染引擎
│   │   ├── html_renderer.py    # Playwright renderer
│   │   ├── exporter.py         # MoviePy exporter
│   │   └── cv_compositor.py    # OpenCV compositor (TODO)
│   ├── server/                 # HTTP server | HTTP 服务器
│   ├── utils/                  # Utility functions | 工具函数
│   └── render.py               # Main render pipeline | 主渲染流程
├── examples/                   # Example projects | 示例项目
│   ├── hello_world/            # Basic animation | 基础动画
│   ├── audio_demo/             # Audio composition | 音频合成
│   └── video_placeholder/      # Video placeholder | 视频占位符
├── tests/                      # Unit tests | 单元测试
│   └── test_composition.py
├── requirements.txt            # Dependencies | 依赖列表
└── README.md                   # Documentation | 项目说明
```

---

## 🗺️ Roadmap | 开发路线图

- ✅ **MVP (v0.1.0)**
  - ✅ HTML rendering + Audio composition | HTML 渲染 + 音频合成
  - ✅ Video placeholder mechanism | Video 占位符机制
  - ✅ Composition/Sequence API

- ⏳ **P1 (v0.2.0)**
  - ⏳ OpenCV video frame compositing | OpenCV 视频帧合成
  - ⏳ Video transitions (fade, wipe) | 视频转场效果（淡入淡出、擦除）
  - ⏳ Subtitle generation & styling | 字幕生成与样式

- ⏳ **P2 (v0.3.0)**
  - ⏳ Multi-track video compositing | 多轨道视频合成
  - ⏳ Filter effects (blur, sharpen, color grading) | 滤镜效果（模糊、锐化、调色）
  - ⏳ GPU-accelerated rendering | GPU 加速渲染

- ⏳ **P3 (v1.0.0)**
  - ⏳ CLI command-line tool | CLI 命令行工具
  - ⏳ Real-time preview | 实时预览
  - ⏳ Performance profiling tools | 性能分析工具

---

## 🤝 Contributing | 贡献指南

Issues and Pull Requests are welcome! | 欢迎提交 Issue 和 Pull Request！

```bash
# Fork repository | Fork 项目
git clone https://github.com/InZei/opencut.git

# Create feature branch | 创建功能分支
git checkout -b feature/amazing-feature

# Commit changes | 提交更改
git commit -m "Add amazing feature"

# Push to branch | 推送到分支
git push origin feature/amazing-feature
```

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details | 详见 [LICENSE](LICENSE) 文件

---

## 📬 Contact | 联系方式

- **GitHub**: https://github.com/InZei/opencut
- **Issues**: https://github.com/InZei/opencut/issues
- **Remotion Official Docs**: https://www.remotion.dev/

---

<div align="center">

**🎬 OpenCut - Make Video Creation as Simple as Writing Code**  
**🎬 OpenCut - 让视频创作像写代码一样简单**

Made with ❤️ by InZei

</div>
