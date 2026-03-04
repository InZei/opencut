# OpenCut

Python 版 Remotion - 使用 HTML/CSS/JS 创建视频的编程式框架

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 安装 Playwright 浏览器

```bash
playwright install chromium
```

### 3. 运行示例

```bash
# Hello World 示例
cd examples/hello_world
python main.py

# Audio Demo 示例
cd examples/audio_demo
python main.py

# Video Placeholder 示例
cd examples/video_placeholder
python main.py
```

## 核心 API

### Composition

定义视频的基本参数：

```python
from opencut import Composition

comp = Composition(
    fps=30,
    duration_in_frames=300,  # 10 秒
    width=1920,
    height=1080
)
```

### Sequence

定义时间轴上的片段：

```python
from opencut import Sequence, HTMLClip

comp.add(
    Sequence(
        start_frame=0,
        duration=300,
        component=HTMLClip(src="index.html")
    )
)
```

### Clips

- **HTMLClip**: HTML 渲染组件
- **VideoClip**: 视频组件（MVP 阶段为占位符）
- **AudioClip**: 音频组件

```python
from opencut import HTMLClip, VideoClip, AudioClip

HTMLClip(src="index.html", props={})
VideoClip(src="video.mp4", bind_id="main_video")
AudioClip(src="audio.mp3", volume=0.8)
```

### Render

渲染最终视频：

```python
from opencut import render

render(comp, output="output.mp4")
```

## 完整示例

```python
from opencut import Composition, Sequence, HTMLClip, AudioClip, render

# 1. 创建 Composition
comp = Composition(fps=30, duration_in_frames=150, width=1920, height=1080)

# 2. 添加 HTML 动画层
comp.add(Sequence(
    start_frame=0,
    duration=150,
    component=HTMLClip(src="index.html")
))

# 3. 添加音频
comp.add(Sequence(
    start_frame=0,
    duration=150,
    component=AudioClip(src="music.mp3")
))

# 4. 渲染
render(comp, output="output.mp4")
```

## HTML 模板要求

HTML 文件需要暴露 `window.renderFrame` 钩子：

```html
<script>
    window.renderFrame = function(frame) {
        // 基于帧号更新动画状态
        const element = document.getElementById('myElement');
        element.style.opacity = Math.min(1, frame / 30);
    }
</script>
```

## Video 占位符机制

Opencut 使用分离渲染架构，Video 使用占位符：

```html
<div class="opencut-video-placeholder" data-id="main_video"></div>
```

Python 代码绑定：

```python
VideoClip(src="video.mp4", bind_id="main_video")
```

## 架构设计

```
用户调用 render()
    ↓
1. 启动本地 HTTP 服务器
    ↓
2. Playwright 渲染 HTML 帧（透明 PNG）
    ↓
3. 提取 Video 占位符坐标
    ↓
4. (后续) OpenCV 合成视频帧
    ↓
5. MoviePy 合成音频 → MP4
```

## 与 Remotion 对比

| 特性 | Remotion | Opencut |
|------|----------|---------|
| 语言 | TypeScript/React | Python |
| 渲染引擎 | Puppeteer | Playwright |
| 视频合成 | FFmpeg | OpenCV + MoviePy |
| 适用场景 | 前端开发 | AI/自动化/数据分析 |

## 开发计划

- ✅ MVP: HTML 渲染 + 音频合成
- ✅ MVP: Video 占位符机制
- ⏳ P1: OpenCV 视频帧合成
- ⏳ P2: 转场效果
- ⏳ P2: 字幕生成

## License

MIT
