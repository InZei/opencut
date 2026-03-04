# OpenCut

<div align="center">

**🎬 用 HTML/CSS/JS 创作视频的编程式框架**

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Remotion 的 Python 版本 | 声明式动画 | 帧级控制 | 可编程视频**

</div>

---

## 🌟 功能亮点

### ✨ 核心特性

- **🎨 HTML/CSS/JS 动画** - 使用现代 Web 技术栈创建视频内容，支持所有 CSS 动画、Canvas、WebGL
- **⚡ 帧级精确控制** - 通过 `window.renderFrame(frame)` 钩子实现逐帧动画控制
- **🎵 音频合成** - 支持多轨道音频混合、音量调节、淡入淡出
- **🎬 Video 占位符机制** - 预留 OpenCV 视频合成接口，支持背景视频叠加
- **🔧 声明式 API** - 受 Remotion 启发的 Composition → Sequence → Clip 三层架构
- **🚀 可编程生成** - 完美适配 AI 生成、数据可视化、批量视频制作场景

### 🎯 适用场景

- 📊 **数据可视化视频** - 动态图表、实时数据展示
- 🤖 **AI 生成内容** - 结合 LLM 批量生成营销视频
- 📱 **社交媒体自动化** - 程序化生成短视频内容
- 🎓 **教育视频制作** - 代码演示、教程动画
- 📈 **营销素材生成** - 个性化广告视频批量生产

### 💡 为什么选择 OpenCut？

> "如果你能用代码描述它，就能用它制作视频"

- **前端友好** - 复用现有 HTML/CSS 技能和组件库
- **Python 生态** - 无缝集成 NumPy、Pandas、AI 模型
- **版本控制** - 视频即代码，支持 Git 管理
- **可测试性** - 单元测试、CI/CD 自动化
- **零学习成本** - Remotion 用户可无缝迁移

---

## 🚀 快速开始

### 1️⃣ 安装依赖

```bash
# 克隆项目
git clone https://github.com/InZei/opencut.git
cd opencut

# 创建虚拟环境（推荐）
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux

# 安装依赖（使用国内镜像加速）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2️⃣ 安装浏览器

```bash
# 使用国内镜像安装 Playwright Chromium
$env:PLAYWRIGHT_DOWNLOAD_HOST="https://npmmirror.com/mirrors/playwright/"
playwright install chromium
```

### 3️⃣ 运行示例

```bash
# Hello World - 基础动画示例
cd examples/hello_world
python main.py
# 输出：output.mp4 (1920x1080, 5 秒)

# Audio Demo - 音频合成示例
cd examples/audio_demo
python main.py

# Video Placeholder - 视频占位符示例
cd examples/video_placeholder
python main.py
```

---

## 📖 核心 API

### Composition - 画布配置

定义视频的基本参数：

```python
from opencut import Composition

comp = Composition(
    fps=30,                    # 帧率
    duration_in_frames=300,    # 总帧数 (300 帧 = 10 秒 @ 30fps)
    width=1920,                # 宽度
    height=1080                # 高度
)
```

### Sequence - 时间轴片段

在时间轴上添加图层：

```python
from opencut import Sequence, HTMLClip

# 添加 HTML 动画层（从第 0 帧开始，持续 300 帧）
comp.add(
    Sequence(
        start_frame=0,
        duration=300,
        component=HTMLClip(src="index.html")
    )
)

# 添加音频层（从第 50 帧开始）
comp.add(
    Sequence(
        start_frame=50,
        duration=250,
        component=AudioClip(src="music.mp3", volume=0.8)
    )
)
```

### Clips - 组件类型

三种核心组件：

```python
from opencut import HTMLClip, VideoClip, AudioClip

# HTML 组件 - 渲染 HTML/CSS/JS 动画
HTMLClip(
    src="index.html",          # HTML 文件路径
    props={"color": "red"}     # 传递给 HTML 的参数
)

# 视频组件 - 占位符机制（待 OpenCV 合成）
VideoClip(
    src="background.mp4",      # 视频文件
    bind_id="main_video"       # 绑定 HTML 中的占位符 ID
)

# 音频组件 - 背景音乐/音效
AudioClip(
    src="music.mp3",           # 音频文件
    volume=1.0,                # 音量 (0.0-1.0)
    start_time=0               # 起始时间（秒）
)
```

### Render - 渲染输出

导出最终视频：

```python
from opencut import render

output_path = render(comp, output="output.mp4")
print(f"视频已生成：{output_path}")
```

---

## 💻 完整示例

### Hello World - 淡入动画

**Python 代码：**
```python
from opencut import Composition, Sequence, HTMLClip, render

# 创建 Composition
comp = Composition(
    fps=30,
    duration_in_frames=150,  # 5 秒
    width=1920,
    height=1080
)

# 添加 HTML 动画
comp.add(Sequence(
    start_frame=0,
    duration=150,
    component=HTMLClip(src="index.html")
))

# 渲染
render(comp, output="output.mp4")
```

**HTML 动画 (index.html)：**
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
        // 帧渲染钩子
        window.renderFrame = function(frame) {
            const box = document.getElementById('box');
            // 淡入效果：0-30 帧从透明到不透明
            box.style.opacity = Math.min(1, frame / 30);
            // 旋转效果：持续旋转
            box.style.transform = `translate(-50%, -50%) rotate(${frame * 2}deg)`;
        }
    </script>
</body>
</html>
```

---

## 🏗️ 架构设计

### 渲染流程

```
用户调用 render()
    ↓
1. 启动本地 HTTP 服务器 (localhost:8000)
    ↓
2. Playwright 加载 HTML 并逐帧渲染
    ↓
3. 每帧调用 window.renderFrame(frame)
    ↓
4. 捕获透明背景 PNG 序列
    ↓
5. 提取 Video 占位符坐标信息
    ↓
6. MoviePy 合成音频 → MP4 输出
    ↓
7. (未来) OpenCV 合成视频层
```

### 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| **HTML 渲染** | Playwright | 无头浏览器渲染 HTML/CSS/JS |
| **视频合成** | MoviePy | 图像序列 + 音频合成 |
| **视频处理** | OpenCV (预留) | 视频帧合成、转场效果 |
| **HTTP 服务** | http.server | 本地静态文件服务 |

### 与 Remotion 对比

| 特性 | Remotion | OpenCut |
|------|----------|---------|
| 语言 | TypeScript/React | Python |
| 渲染引擎 | Puppeteer | Playwright |
| 视频合成 | FFmpeg | MoviePy + OpenCV |
| 音频处理 | FFmpeg | MoviePy |
| 适用场景 | 前端开发 | AI/自动化/数据科学 |
| 学习曲线 | 需要 React | 零学习成本 |

---

## 📁 项目结构

```
opencut/
├── opencut/                    # Python 包
│   ├── __init__.py             # 公共 API 导出
│   ├── core/                   # 核心数据结构
│   │   ├── composition.py      # Composition 类
│   │   ├── sequence.py         # Sequence 类
│   │   └── clips.py            # HTMLClip, VideoClip, AudioClip
│   ├── renderer/               # 渲染引擎
│   │   ├── html_renderer.py    # Playwright 渲染器
│   │   ├── exporter.py         # MoviePy 导出器
│   │   └── cv_compositor.py    # OpenCV 合成器 (待实现)
│   ├── server/                 # HTTP 服务器
│   ├── utils/                  # 工具函数
│   └── render.py               # 主渲染流程
├── examples/                   # 示例项目
│   ├── hello_world/            # 基础动画
│   ├── audio_demo/             # 音频合成
│   └── video_placeholder/      # 视频占位符
├── tests/                      # 单元测试
│   └── test_composition.py
├── requirements.txt            # 依赖列表
└── README.md                   # 项目说明
```

---

## 🗺️ 开发路线图

- ✅ **MVP (v0.1.0)**
  - ✅ HTML 渲染 + 音频合成
  - ✅ Video 占位符机制
  - ✅ Composition/Sequence API

- ⏳ **P1 (v0.2.0)**
  - ⏳ OpenCV 视频帧合成
  - ⏳ 视频转场效果（淡入淡出、擦除）
  - ⏳ 字幕生成与样式

- ⏳ **P2 (v0.3.0)**
  - ⏳ 多轨道视频合成
  - ⏳ 滤镜效果（模糊、锐化、调色）
  - ⏳ GPU 加速渲染

- ⏳ **P3 (v1.0.0)**
  - ⏳ CLI 命令行工具
  - ⏳ 实时预览
  - ⏳ 性能分析工具

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

```bash
# Fork 项目
git clone https://github.com/InZei/opencut.git

# 创建功能分支
git checkout -b feature/amazing-feature

# 提交更改
git commit -m "Add amazing feature"

# 推送到分支
git push origin feature/amazing-feature
```

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 📬 联系方式

- **GitHub**: https://github.com/InZei/opencut
- **Issues**: https://github.com/InZei/opencut/issues
- **Remotion 官方文档**: https://www.remotion.dev/

---

<div align="center">

**🎬 OpenCut - 让视频创作像写代码一样简单**

Made with ❤️ by InZei

</div>
