---
name: use-extensions
description: |
  How to use OpenCut extension packages for advanced video features.
  
  Use this skill when the user wants to:
  - Add transitions between scenes (fade, slide, zoom)
  - Use custom fonts or Google Fonts
  - Create 3D animations with Three.js
  - Render SVG graphics and animations
  - Use Tailwind CSS for styling
  - Add subtitles from SRT/VTT files
  
  This skill covers ALL extension packages. Always check if an extension exists
  before implementing custom solutions.
compatibility:
  - python: "3.12+"
  - opencut: "0.2.0+"
---

# OpenCut Extensions Usage Guide

OpenCut provides extension packages for advanced video features. This skill teaches you how to use each extension effectively.

## Extension Overview

Available extensions:
- **Transitions** - CrossFade, Slide, Zoom effects
- **Fonts** - Google Fonts integration
- **Three.js** - 3D graphics and animations
- **SVG** - Vector graphics rendering
- **Tailwind CSS** - Utility-first CSS framework
- **Captions** - SRT/VTT subtitle support

## 1. Transitions Extension

Location: [`opencut/extensions/transitions.py`](../../opencut/extensions/transitions.py)

### Basic Usage

```python
from opencut import Composition, Sequence, HTMLClip
from opencut.extensions import CrossFade, Slide, Zoom

comp = Composition(fps=30, duration_in_frames=300, width=1920, height=1080)

# CrossFade - Smooth fade transition
comp.add(Sequence(
    start_frame=0,
    duration=60,
    component=CrossFade(
        from_scene="scene1.html",
        to_scene="scene2.html",
        duration=30  # 30 frames = 1 second @ 30fps
    )
))

# Slide - Slide in from direction
comp.add(Sequence(
    start_frame=60,
    duration=60,
    component=Slide(
        scene="scene2.html",
        direction="left",  # left, right, top, bottom
        duration=30
    )
))

# Zoom - Zoom in/out transition
comp.add(Sequence(
    start_frame=120,
    duration=60,
    component=Zoom(
        scene="scene3.html",
        type="in",  # "in" or "out"
        duration=30
    )
))
```

### TransitionSequence - Chain Multiple Transitions

```python
from opencut.extensions import TransitionSequence

# Create a sequence of transitions
transition_chain = TransitionSequence([
    CrossFade("scene1.html", "scene2.html", duration=30),
    Slide("scene2.html", "scene3.html", direction="right", duration=30),
    Zoom("scene3.html", "scene4.html", type="out", duration=30)
])

comp.add(Sequence(
    start_frame=0,
    duration=180,  # Total duration of all transitions
    component=transition_chain
))
```

### Custom Transition Parameters

```python
CrossFade(
    from_scene="scene1.html",
    to_scene="scene2.html",
    duration=30,
    easing="ease-in-out"  # ease-in, ease-out, ease-in-out, linear
)

Slide(
    scene="scene2.html",
    direction="left",
    duration=30,
    offset=100  # Slide offset in pixels
)

Zoom(
    scene="scene3.html",
    type="in",
    duration=30,
    scale=2.0  # Zoom scale factor
)
```

## 2. Fonts Extension

Location: [`opencut/extensions/fonts.py`](../../opencut/extensions/fonts.py)

### Load Google Fonts

```python
from opencut import Composition, Sequence, HTMLClip
from opencut.extensions import GoogleFont, load_font, enable_google_fonts

comp = Composition(fps=30, duration_in_frames=300, width=1920, height=1080)

# Method 1: Load individual font
font = GoogleFont.load_google_font(
    family="Roboto",
    weight=400,
    style="normal"
)

# Method 2: Enable multiple fonts
enable_google_fonts([
    {"family": "Roboto", "weight": 400},
    {"family": "Open Sans", "weight": 700},
    {"family": "Lato", "weight": 300}
])

# Use in HTML
comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=HTMLClip(src="index.html")
))
```

### HTML with Google Fonts

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        
        .title {
            font-family: 'Roboto', sans-serif;
            font-size: 72px;
            font-weight: 700;
        }
    </style>
</head>
<body>
    <h1 class="title">Styled with Google Fonts</h1>
</body>
</html>
```

### Preset Fonts

```python
from opencut.extensions import PresetFonts

# Use preset font configurations
fonts = PresetFonts.MODERN  # Modern sans-serif combination
# or
fonts = PresetFonts.CLASSIC  # Classic serif combination
# or
fonts = PresetFonts.CODE  # Monospace for code
```

## 3. Three.js Extension

Location: [`opencut/extensions/three.py`](../../opencut/extensions/three.py)

### Basic Three.js Scene

```python
from opencut import Composition, Sequence
from opencut.extensions import ThreeClip, create_three_template

comp = Composition(fps=30, duration_in_frames=300, width=1920, height=1080)

# Create Three.js template
template = create_three_template()

# Add 3D scene
comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=ThreeClip(
        src="scene.js",
        template=template
    )
))
```

### Three.js Scene File (scene.js)

```javascript
// scene.js
import * as THREE from 'three';

export function init(scene, camera, renderer) {
    // Create cube
    const geometry = new THREE.BoxGeometry();
    const material = new THREE.MeshNormalMaterial();
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);
    
    camera.position.z = 5;
    
    return { cube };
}

export function renderFrame(frame, objects) {
    const { cube } = objects;
    
    // Rotate cube
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    
    // Change color based on frame
    const hue = (frame % 360) / 360;
    cube.material.color.setHSL(hue, 1, 0.5);
}
```

### Advanced Three.js

```javascript
// Advanced scene with lighting and animation
import * as THREE from 'three';

export function init(scene, camera, renderer) {
    // Add lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);
    
    const pointLight = new THREE.PointLight(0xffffff, 1);
    pointLight.position.set(5, 5, 5);
    scene.add(pointLight);
    
    // Create sphere
    const geometry = new THREE.SphereGeometry(1, 32, 32);
    const material = new THREE.MeshStandardMaterial({ 
        color: 0x00ff00,
        metalness: 0.5,
        roughness: 0.5
    });
    const sphere = new THREE.Mesh(geometry, material);
    scene.add(sphere);
    
    camera.position.z = 5;
    
    return { sphere, pointLight };
}

export function renderFrame(frame, objects) {
    const { sphere, pointLight } = objects;
    
    // Animate sphere
    sphere.rotation.y = frame * 0.02;
    
    // Orbit light
    const time = frame * 0.05;
    pointLight.position.x = Math.sin(time) * 5;
    pointLight.position.y = Math.cos(time) * 5;
}
```

## 4. SVG Extension

Location: [`opencut/extensions/svg.py`](../../opencut/extensions/svg.py)

### Basic SVG Usage

```python
from opencut import Composition, Sequence
from opencut.extensions import SvgClip, create_svg_template

comp = Composition(fps=30, duration_in_frames=300, width=1920, height=1080)

# Create SVG template
template = create_svg_template()

# Add SVG clip
comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=SvgClip(
        src="animation.svg",
        template=template
    )
))
```

### SVG Animation File (animation.svg)

```xml
<svg width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">
    <circle cx="960" cy="540" r="100" fill="#4ecdc4">
        <animate 
            attributeName="r" 
            from="50" 
            to="150" 
            dur="2s" 
            repeatCount="indefinite"
        />
        <animate 
            attributeName="opacity" 
            from="1" 
            to="0.5" 
            dur="2s" 
            repeatCount="indefinite"
        />
    </circle>
</svg>
```

### Dynamic SVG with JavaScript

```javascript
// svg-animation.js
export function updateSVG(svg, frame) {
    const circle = svg.querySelector('circle');
    
    // Animate radius
    const radius = 100 + Math.sin(frame * 0.1) * 50;
    circle.setAttribute('r', radius);
    
    // Animate color
    const hue = (frame % 360) / 360;
    circle.setAttribute('fill', `hsl(${hue}, 100%, 50%)`);
}
```

## 5. Tailwind CSS Extension

Location: [`opencut/extensions/tailwind.py`](../../opencut/extensions/tailwind.py)

### Enable Tailwind

```python
from opencut import Composition, Sequence, HTMLClip
from opencut.extensions import enable_tailwind, get_tailwind_template

comp = Composition(fps=30, duration_in_frames=300, width=1920, height=1080)

# Method 1: Enable Tailwind globally
enable_tailwind()

# Method 2: Get Tailwind template
template = get_tailwind_template()

comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=HTMLClip(src="index.html")
))
```

### HTML with Tailwind

```html
<!DOCTYPE html>
<html>
<head>
    <!-- Tailwind CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-purple-500 to-pink-500 h-screen flex items-center justify-center">
    <div class="text-center">
        <h1 class="text-6xl font-bold text-white mb-4">
            Styled with Tailwind
        </h1>
        <p class="text-2xl text-white opacity-80">
            Utility-first CSS framework
        </p>
    </div>
    
    <script>
        window.renderFrame = function(frame) {
            const h1 = document.querySelector('h1');
            // Animate opacity
            h1.style.opacity = Math.min(1, frame / 30);
        }
    </script>
</body>
</html>
```

### Custom Tailwind Config

```python
from opencut.extensions import enable_tailwind

# Enable with custom configuration
enable_tailwind(config={
    "theme": {
        "extend": {
            "colors": {
                "brand": "#ff6b6b"
            },
            "fontFamily": {
                "sans": ["Inter", "sans-serif"]
            }
        }
    }
})
```

## 6. Captions Extension

Location: [`opencut/extensions/captions.py`](../../opencut/extensions/captions.py)

### Load SRT Subtitles

```python
from opencut import Composition, Sequence
from opencut.extensions import SubtitleClip, load_subtitles

comp = Composition(fps=30, duration_in_frames=900, width=1920, height=1080)

# Create subtitle clip
subtitle_clip = SubtitleClip(
    srt_path="subtitles.srt",
    font_size=40,
    font_color="#FFFFFF",
    background_color="rgba(0, 0, 0, 0.7)",
    position="bottom"  # top, center, bottom
)

# Add to composition (covers entire video)
comp.add(Sequence(
    start_frame=0,
    duration=900,
    component=subtitle_clip
))
```

### SRT File Format (subtitles.srt)

```
1
00:00:00,500 --> 00:00:04,500
什么是大模型？

2
00:00:05,500 --> 00:00:07,500
大模型 = 超大规模神经网络

3
00:00:08,500 --> 00:00:12,500
可以理解为非常非常聪明的 AI
```

### Load VTT Subtitles

```python
from opencut.extensions import VTTLoader

# Load VTT format
loader = VTTLoader("subtitles.vtt")
subtitles = loader.load()
```

### Custom Subtitle Styling

```python
SubtitleClip(
    srt_path="subtitles.srt",
    font_size=48,
    font_color="#FFFF00",  # Yellow
    background_color="rgba(0, 0, 0, 0.8)",
    position="bottom",
    encoding="utf-8"
)
```

## Combining Extensions

You can combine multiple extensions in a single video:

```python
from opencut import Composition, Sequence, HTMLClip, render
from opencut.extensions import (
    CrossFade, 
    GoogleFont, 
    enable_tailwind,
    SubtitleClip
)

# Create composition
comp = Composition(fps=30, duration_in_frames=600, width=1920, height=1080)

# Enable extensions
enable_tailwind()
GoogleFont.load_google_font("Roboto", weight=400)

# Scene 1
comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=HTMLClip(src="scene1.html")
))

# Transition
comp.add(Sequence(
    start_frame=300,
    duration=30,
    component=CrossFade(
        from_scene="scene1.html",
        to_scene="scene2.html",
        duration=30
    )
))

# Scene 2
comp.add(Sequence(
    start_frame=330,
    duration=270,
    component=HTMLClip(src="scene2.html")
))

# Subtitles (entire video)
comp.add(Sequence(
    start_frame=0,
    duration=600,
    component=SubtitleClip(
        srt_path="subtitles.srt",
        font_size=40,
        position="bottom"
    )
))

# Render
render(comp, output="output.mp4")
```

## Best Practices

1. **Import only what you need** - Don't import all extensions if you only need one
2. **Check compatibility** - Some extensions require additional dependencies
3. **Test transitions** - Preview transitions to ensure smooth timing
4. **Use SRT for subtitles** - More widely supported than VTT
5. **Optimize Three.js** - Keep polygon count reasonable for real-time rendering
6. **Cache fonts** - Load fonts once at the beginning

## Troubleshooting

### Issue: Extension Not Found

**Solution:**
```python
# Ensure you're importing from opencut.extensions
from opencut.extensions import CrossFade  # ✅ Correct
# from opencut import CrossFade  # ❌ Wrong
```

### Issue: Three.js Not Loading

**Solution:**
- Check that Three.js is included in your template
- Verify the scene.js file path is correct
- Ensure init() and renderFrame() functions are exported

### Issue: Subtitles Not Showing

**Solution:**
- Verify SRT file encoding (UTF-8)
- Check timestamp format in SRT
- Ensure SubtitleClip duration covers the video

## Next Steps

- Check individual extension files for advanced options
- Create custom extensions for reusable components
- Combine extensions for complex effects
- Contribute new extensions to the project
