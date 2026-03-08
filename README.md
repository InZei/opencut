# OpenCut

<div align="center">

**🎬 Programmatic Video Creation with HTML/CSS/JS**

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**The Python Version of Remotion | Declarative Animation | Frame-Accurate Control**

</div>

---

## 🌟 Features

### ✨ Core Capabilities

- **🎨 HTML/CSS/JS Animation** - Create video content using modern web technologies with full support for CSS animations, Canvas, and WebGL
- **⚡ Frame-Accurate Control** - Precise per-frame animation control via `window.renderFrame(frame)` hook
- **🎵 Audio Composition** - Multi-track audio mixing with volume control and fade in/out effects
- **🎬 Video Placeholder** - Reserved OpenCV interface for background video overlay and compositing
- **🔧 Declarative API** - Composition → Sequence → Clip architecture inspired by Remotion
- **🚀 Programmable Generation** - Perfect for AI-generated content, data visualization, and batch video production

### 🎯 Use Cases

- 📊 **Data Visualization Videos** - Dynamic charts and real-time data displays
- 🤖 **AI-Generated Content** - Batch marketing videos powered by LLMs
- 📱 **Social Media Automation** - Programmatic short video generation at scale
- 🎓 **Educational Video Production** - Code demonstrations and tutorial animations
- 📈 **Marketing Asset Generation** - Personalized ad video batch production

### 💡 Why OpenCut?

> **"If you can code it, you can video it"**

- **Frontend-Friendly** - Reuse your existing HTML/CSS skills and component libraries
- **Python Ecosystem** - Seamless integration with NumPy, Pandas, and AI/ML models
- **Version Control** - Video as Code - fully manageable with Git
- **Testability** - Built-in support for unit tests and CI/CD automation
- **Zero Learning Curve** - Remotion users can migrate seamlessly

---

## 🚀 Quick Start

### 1️⃣ Install Dependencies

```bash
# Clone the repository
git clone https://github.com/InZei/opencut.git
cd opencut

# Create a virtual environment (recommended)
python -m venv venv

# Activate the environment
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

> **💡 Tip for users in China**: Use Tsinghua mirror for faster downloads:
> ```bash
> pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
> ```

### 2️⃣ Install Playwright Browser

```bash
# Install Chromium browser for Playwright
playwright install chromium
```

> **💡 Tip for users in China**: Use npmmirror for faster browser download:
> ```bash
> $env:PLAYWRIGHT_DOWNLOAD_HOST="https://npmmirror.com/mirrors/playwright/"
> playwright install chromium
> ```

### 3️⃣ Run Examples

```bash
# Hello World - Basic animation example
cd examples/hello_world
python main.py
# Output: output.mp4 (1920x1080, 5 seconds)

# Audio Demo - Audio composition example
cd examples/audio_demo
python main.py

# Video Placeholder - Video placeholder mechanism example
cd examples/video_placeholder
python main.py
```

---

## 📖 Core API

### Composition - Canvas Configuration

Define the basic parameters of your video:

```python
from opencut import Composition

comp = Composition(
    fps=30,                    # Frame rate
    duration_in_frames=300,    # Total frames (300 frames = 10s @ 30fps)
    width=1920,                # Width in pixels
    height=1080                # Height in pixels
)
```

### Sequence - Timeline Segments

Add layers on the timeline:

```python
from opencut import Sequence, HTMLClip

# Add HTML animation layer (starts at frame 0, lasts 300 frames)
comp.add(
    Sequence(
        start_frame=0,
        duration=300,
        component=HTMLClip(src="index.html")
    )
)

# Add audio layer (starts at frame 50)
comp.add(
    Sequence(
        start_frame=50,
        duration=250,
        component=AudioClip(src="music.mp3", volume=0.8)
    )
)
```

### Clips - Component Types

Three core component types:

```python
from opencut import HTMLClip, VideoClip, AudioClip

# HTML Component - Renders HTML/CSS/JS animation
HTMLClip(
    src="index.html",          # Path to HTML file
    props={"color": "red"}     # Props passed to the HTML
)

# Video Component - Placeholder mechanism (OpenCV compositing pending)
VideoClip(
    src="background.mp4",      # Path to video file
    bind_id="main_video"       # Binds to placeholder ID in HTML
)

# Audio Component - Background music or sound effects
AudioClip(
    src="music.mp3",           # Path to audio file
    volume=1.0,                # Volume (0.0 to 1.0)
    start_time=0               # Start time in seconds
)
```

### Render - Export Video

Export the final video:

```python
from opencut import render

output_path = render(comp, output="output.mp4")
print(f"Video generated: {output_path}")
```

---

## 💻 Complete Example

### Hello World - Fade-in Animation

**Python Code:**
```python
from opencut import Composition, Sequence, HTMLClip, render

# Create Composition
comp = Composition(
    fps=30,
    duration_in_frames=150,  # 5 seconds
    width=1920,
    height=1080
)

# Add HTML animation
comp.add(Sequence(
    start_frame=0,
    duration=150,
    component=HTMLClip(src="index.html")
))

# Render
render(comp, output="output.mp4")
```

**HTML Animation (index.html):**
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
        // Frame render hook required by OpenCut
        window.renderFrame = function(frame) {
            const box = document.getElementById('box');
            // Fade-in: opacity 0→1 in frames 0-30
            box.style.opacity = Math.min(1, frame / 30);
            // Rotation: continuous spin
            box.style.transform = `translate(-50%, -50%) rotate(${frame * 2}deg)`;
        }
    </script>
</body>
</html>
```

---

## 🏗️ Architecture

### Rendering Pipeline

```
User calls render()
    ↓
1. Start local HTTP server (localhost:8000)
    ↓
2. Playwright loads HTML and renders frames
    ↓
3. Call window.renderFrame(frame) for each frame
    ↓
4. Capture transparent PNG sequence
    ↓
5. Extract Video placeholder coordinates
    ↓
6. MoviePy composites audio → MP4 output
    ↓
7. (Future) OpenCV composites video layer
```

### Tech Stack

| Component | Technology | Description |
|-----------|------------|-------------|
| **HTML Rendering** | Playwright | Headless browser renders HTML/CSS/JS |
| **Video Compositing** | MoviePy | Image sequence + audio synthesis |
| **Video Processing** | OpenCV (Reserved) | Video frame compositing and transitions |
| **HTTP Server** | http.server | Local static file serving |

### Comparison with Remotion

| Feature | Remotion | OpenCut |
|---------|----------|---------|
| Language | TypeScript/React | Python |
| Rendering Engine | Puppeteer | Playwright |
| Video Compositing | FFmpeg | MoviePy + OpenCV |
| Audio Processing | FFmpeg | MoviePy |
| Primary Use Case | Frontend Development | AI/Automation/Data Science |
| Learning Curve | Requires React | Zero Learning Curve |

---

## 📁 Project Structure

```
opencut/
├── opencut/                    # Python package
│   ├── __init__.py             # Public API exports
│   ├── core/                   # Core data structures
│   │   ├── composition.py      # Composition class
│   │   ├── sequence.py         # Sequence class
│   │   └── clips.py            # HTMLClip, VideoClip, AudioClip
│   ├── renderer/               # Rendering engine
│   │   ├── html_renderer.py    # Playwright renderer
│   │   ├── exporter.py         # MoviePy exporter
│   │   └── cv_compositor.py    # OpenCV compositor (TODO)
│   ├── server/                 # HTTP server
│   ├── utils/                  # Utility functions
│   └── render.py               # Main render pipeline
├── examples/                   # Example projects
│   ├── hello_world/            # Basic animation
│   ├── audio_demo/             # Audio composition
│   └── video_placeholder/      # Video placeholder
├── tests/                      # Unit tests
│   └── test_composition.py
├── requirements.txt            # Dependencies
└── README.md                   # Documentation
```

---

## 🗺️ Roadmap

- ✅ **MVP (v0.1.0)**
  - ✅ HTML rendering + Audio composition
  - ✅ Video placeholder mechanism
  - ✅ Composition/Sequence API

- ⏳ **P1 (v0.2.0)**
  - ⏳ OpenCV video frame compositing
  - ⏳ Video transitions (fade, wipe)
  - ⏳ Subtitle generation & styling

- ⏳ **P2 (v0.3.0)**
  - ⏳ Multi-track video compositing
  - ⏳ Filter effects (blur, sharpen, color grading)
  - ⏳ GPU-accelerated rendering

- ⏳ **P3 (v1.0.0)**
  - ⏳ CLI command-line tool
  - ⏳ Real-time preview
  - ⏳ Performance profiling tools

---

## 🤝 Contributing

Issues and Pull Requests are welcome!

```bash
# Fork the repository
git clone https://github.com/InZei/opencut.git

# Create a feature branch
git checkout -b feature/amazing-feature

# Commit your changes
git commit -m "Add amazing feature"

# Push to the branch
git push origin feature/amazing-feature
```

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

---

## 📬 Contact

- **GitHub**: https://github.com/InZei/opencut
- **Issues**: https://github.com/InZei/opencut/issues
- **Remotion Official Docs**: https://www.remotion.dev/

---

<div align="center">

**🎬 OpenCut - Make Video Creation as Simple as Writing Code**

Made with ❤️ by InZei

</div>
