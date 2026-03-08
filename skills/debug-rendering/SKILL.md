---
name: debug-rendering
description: |
  How to debug and troubleshoot OpenCut video rendering issues.
  
  Use this skill when the user encounters:
  - Rendering errors or failures
  - Missing frames or black screens
  - Audio/video synchronization issues
  - Performance problems (slow rendering)
  - HTML/CSS not rendering correctly
  - Playwright browser issues
  - Video codec or export problems
  
  This skill provides systematic debugging approaches and common solutions.
  Always follow the debugging workflow before trying random fixes.
compatibility:
  - python: "3.12+"
  - playwright: "chromium"
  - moviepy: "2.x"
---

# OpenCut Debugging & Troubleshooting Guide

This skill provides systematic approaches to debug and fix common rendering issues.

## Debugging Workflow

Follow this step-by-step workflow when encountering issues:

```
1. Identify the symptom
   ↓
2. Check error messages
   ↓
3. Isolate the component
   ↓
4. Apply targeted fix
   ↓
5. Verify the solution
```

## Common Issues & Solutions

### Issue 1: HTML Not Rendering (Black Screen)

**Symptoms:**
- Output video is completely black
- No error messages
- Rendering completes but no content

**Debugging Steps:**

**Step 1: Check HTML file path**
```python
import os

# Verify file exists
html_path = "index.html"
if not os.path.exists(html_path):
    print(f"❌ HTML file not found: {html_path}")
    print(f"   Current directory: {os.getcwd()}")
else:
    print(f"✅ HTML file exists: {os.path.abspath(html_path)}")
```

**Step 2: Verify window.renderFrame**
```javascript
// Check that renderFrame is defined
console.log('renderFrame exists:', typeof window.renderFrame === 'function');

// Test manual call
if (window.renderFrame) {
    window.renderFrame(0);
    console.log('renderFrame(0) executed successfully');
}
```

**Step 3: Check HTML size**
```javascript
// Ensure HTML matches composition size
console.log('Window size:', window.innerWidth, window.innerHeight);
// Should be 1920x1080 (or your composition size)
```

**Step 4: Test in browser**
```bash
# Open HTML file directly in browser
# Check browser console for errors
# Verify animation works
```

**Common Fixes:**

1. **Use absolute paths:**
```python
import os
html_path = os.path.abspath("index.html")
comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=HTMLClip(src=html_path)
))
```

2. **Add error handling in HTML:**
```javascript
window.renderFrame = function(frame) {
    try {
        // Your animation code
        const element = document.getElementById('myElement');
        if (element) {
            element.style.opacity = frame / 30;
        } else {
            console.error('Element not found!');
        }
    } catch (error) {
        console.error('renderFrame error:', error);
    }
}
```

3. **Ensure CSS is loaded:**
```html
<head>
    <style>
        /* Inline CSS to avoid loading issues */
        #container {
            width: 1920px;
            height: 1080px;
        }
    </style>
</head>
```

### Issue 2: Audio Not Playing

**Symptoms:**
- Video renders but no audio
- Audio out of sync with video
- Audio cuts off early

**Debugging Steps:**

**Step 1: Check audio file**
```python
import os
from moviepy.editor import AudioFileClip

audio_path = "audio/music.mp3"

# Verify file exists
if not os.path.exists(audio_path):
    print(f"❌ Audio file not found: {audio_path}")
    
# Check audio duration
try:
    audio = AudioFileClip(audio_path)
    print(f"Audio duration: {audio.duration} seconds")
    audio.close()
except Exception as e:
    print(f"❌ Cannot read audio file: {e}")
```

**Step 2: Verify composition duration**
```python
# Ensure composition duration matches audio
comp = Composition(
    fps=30,
    duration_in_frames=300,  # 10 seconds
    width=1920,
    height=1080
)

# Audio should be same duration
# 10 seconds @ 30fps = 300 frames
```

**Step 3: Check audio parameters**
```python
from opencut import AudioClip

comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=AudioClip(
        src="music.mp3",
        volume=1.0,      # Ensure volume is not 0
        start_time=0     # Start from beginning
    )
))
```

**Common Fixes:**

1. **Adjust audio timing:**
```python
AudioClip(
    src="music.mp3",
    start_time=0.5,    # Delay start by 0.5 seconds
    end_time=9.5       # End at 9.5 seconds
)
```

2. **Convert audio format:**
```bash
# Convert to WAV (more reliable)
ffmpeg -i music.mp3 -ar 44100 -ac 2 music.wav
```

3. **Check audio codec:**
```python
# Use moviepy to inspect
from moviepy.editor import AudioFileClip
audio = AudioFileClip("music.mp3")
print(f"Codec: {audio.codec}")
print(f"Sample rate: {audio.fps}")
audio.close()
```

### Issue 3: Video Placeholder Not Showing

**Symptoms:**
- Background video not appearing
- Video layer missing from output
- Z-index issues (video covered by HTML)

**Debugging Steps:**

**Step 1: Verify video file**
```python
import cv2

video_path = "assets/video/background.mp4"

# Check if OpenCV can read the video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"❌ Cannot open video: {video_path}")
else:
    print(f"✅ Video opened successfully")
    print(f"   FPS: {cap.get(cv2.CAP_PROP_FPS)}")
    print(f"   Width: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}")
    print(f"   Height: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
    print(f"   Frame count: {int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}")
cap.release()
```

**Step 2: Check bind_id**
```html
<!-- Ensure HTML has matching placeholder -->
<div id="video-placeholder" data-bind="main_video"></div>

<script>
// Verify placeholder exists
console.log('Placeholder exists:', document.querySelector('[data-bind="main_video"]'));
</script>
```

**Step 3: Verify VideoClip configuration**
```python
from opencut import VideoClip

comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=VideoClip(
        src="background.mp4",
        bind_id="main_video"  # Must match HTML data-bind
    )
))
```

**Common Fixes:**

1. **Fix z-index:**
```html
<style>
    #video-placeholder {
        position: absolute;
        top: 0;
        left: 0;
        z-index: 0;  /* Background layer */
    }
    
    .content {
        position: relative;
        z-index: 1;  /* Foreground layer */
    }
</style>
```

2. **Use absolute video path:**
```python
import os
video_path = os.path.abspath("assets/video/background.mp4")

VideoClip(
    src=video_path,
    bind_id="main_video"
)
```

3. **Check video codec compatibility:**
```bash
# Re-encode to H.264 (most compatible)
ffmpeg -i input.mp4 -c:v libx264 -c:a aac output.mp4
```

### Issue 4: Slow Rendering Performance

**Symptoms:**
- Rendering takes very long
- High memory usage
- Browser hangs during rendering

**Debugging Steps:**

**Step 1: Profile rendering time**
```python
import time
from opencut import render

start = time.time()
render(comp, output="output.mp4")
end = time.time()

print(f"Total render time: {end - start:.2f} seconds")
print(f"Frames per second: {comp.duration_in_frames / (end - start):.2f}")
```

**Step 2: Check frame complexity**
```javascript
// Add performance monitoring to HTML
window.renderFrame = function(frame) {
    const start = performance.now();
    
    // Your animation code
    
    const end = performance.now();
    if (frame % 30 === 0) {  // Log every 30 frames
        console.log(`Frame ${frame}: ${(end - start).toFixed(2)}ms`);
    }
}
```

**Step 3: Monitor memory usage**
```python
import psutil
import os

process = psutil.Process(os.getpid())
print(f"Memory usage: {process.memory_info().rss / 1024 / 1024:.2f} MB")
```

**Common Fixes:**

1. **Reduce resolution for testing:**
```python
comp = Composition(
    fps=30,
    duration_in_frames=90,   # Shorter duration (3 seconds)
    width=1280,              # Lower resolution
    height=720
)
```

2. **Optimize HTML/CSS:**
```javascript
// Avoid expensive operations in renderFrame
window.renderFrame = function(frame) {
    // ❌ BAD: Creating new elements every frame
    // const div = document.createElement('div');
    
    // ✅ GOOD: Reuse existing elements
    const element = document.getElementById('myElement');
    element.style.transform = `rotate(${frame}deg)`;
}
```

3. **Use requestIdleCallback for heavy computation:**
```javascript
// Pre-compute expensive operations
const precomputed = [];
for (let i = 0; i < 300; i++) {
    precomputed.push(computeExpensiveValue(i));
}

window.renderFrame = function(frame) {
    // Use precomputed values
    element.value = precomputed[frame];
}
```

4. **Enable caching:**
```python
# Cache rendered frames
import tempfile
import os

temp_dir = tempfile.mkdtemp()
print(f"Caching frames to: {temp_dir}")
```

### Issue 5: Playwright Browser Issues

**Symptoms:**
- Playwright cannot launch browser
- Browser crashes during rendering
- Timeout errors

**Debugging Steps:**

**Step 1: Verify Playwright installation**
```python
from playwright.sync_api import sync_playwright

try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        print("✅ Browser launched successfully")
        browser.close()
except Exception as e:
    print(f"❌ Browser launch failed: {e}")
```

**Step 2: Check browser version**
```bash
# Check installed browsers
playwright show-installed-browsers
```

**Step 3: Reinstall Playwright**
```bash
# Reinstall Chromium
playwright install chromium --force
```

**Common Fixes:**

1. **Launch with options:**
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,           # Run headless
        args=['--no-sandbox']    # Disable sandbox (if needed)
    )
```

2. **Increase timeout:**
```python
# In render.py or your code
page.set_default_timeout(60000)  # 60 seconds
```

3. **Handle page errors:**
```python
page.on('pageerror', lambda error: print(f'Page error: {error}'))
page.on('console', lambda msg: print(f'Console: {msg.text}'))
```

### Issue 6: Video Export Errors

**Symptoms:**
- MoviePy export fails
- Corrupted output file
- Codec errors

**Debugging Steps:**

**Step 1: Check MoviePy installation**
```python
from moviepy.editor import VideoFileClip
import moviepy.version as mpv

print(f"MoviePy version: {mpv.__version__}")
```

**Step 2: Verify frame sequence**
```python
import os
import glob

frames_dir = "temp_frames"
frames = sorted(glob.glob(f"{frames_dir}/*.png"))

print(f"Found {len(frames)} frames")
if frames:
    print(f"First frame: {os.path.getsize(frames[0])} bytes")
    print(f"Last frame: {os.path.getsize(frames[-1])} bytes")
```

**Step 3: Test export with short clip**
```python
from moviepy.editor import ImageSequenceClip

# Test with first 10 frames
test_frames = frames[:10]
clip = ImageSequenceClip(test_frames, fps=30)
clip.write_videofile("test.mp4")
```

**Common Fixes:**

1. **Specify codec explicitly:**
```python
from moviepy.editor import ImageSequenceClip

clip = ImageSequenceClip(frames, fps=30)
clip.write_videofile(
    "output.mp4",
    codec='libx264',      # H.264 codec
    audio_codec='aac',    # AAC audio
    preset='medium'       # Encoding speed
)
```

2. **Use different preset:**
```python
clip.write_videofile(
    "output.mp4",
    preset='ultrafast'    # Faster encoding (larger file)
    # or
    preset='slow'         # Slower encoding (smaller file)
)
```

3. **Handle frame size mismatch:**
```python
# Ensure all frames are same size
from PIL import Image
import cv2

target_size = (1920, 1080)

for frame_path in frames:
    img = cv2.imread(frame_path)
    if img.shape[:2] != (target_size[1], target_size[0]):
        img = cv2.resize(img, target_size)
        cv2.imwrite(frame_path, img)
```

## Debugging Tools

### Tool 1: Frame Inspector

```python
def inspect_frame(frame_path):
    from PIL import Image
    import numpy as np
    
    img = Image.open(frame_path)
    print(f"Size: {img.size}")
    print(f"Mode: {img.mode}")
    print(f"Format: {img.format}")
    
    # Check if frame is black
    img_array = np.array(img)
    if np.mean(img_array) < 10:
        print("⚠️  Frame appears to be black!")
    
    img.close()

# Usage
inspect_frame("temp_frames/00001.png")
```

### Tool 2: Audio Visualizer

```python
def visualize_audio(audio_path):
    from moviepy.editor import AudioFileClip
    import numpy as np
    import matplotlib.pyplot as plt
    
    audio = AudioFileClip(audio_path)
    audio_data = audio.iter_chunks()
    
    # Plot waveform
    plt.figure(figsize=(12, 4))
    plt.plot(audio_data)
    plt.title(f"Audio Waveform: {audio_path}")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.savefig("audio_waveform.png")
    print("Audio waveform saved to: audio_waveform.png")
    
    audio.close()
```

### Tool 3: Performance Profiler

```python
def profile_render(func):
    import time
    import functools
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        
        print(f"Function: {func.__name__}")
        print(f"Duration: {end - start:.2f} seconds")
        print(f"FPS: {300 / (end - start):.2f}")  # Assuming 300 frames
        
        return result
    
    return wrapper

# Usage
@profile_render
def render_video():
    from opencut import render
    render(comp, output="output.mp4")
```

## Best Practices

1. **Test incrementally** - Test each component separately before combining
2. **Use version control** - Commit working versions before making changes
3. **Keep logs** - Save error messages and console output
4. **Start small** - Test with short durations (5-10 seconds)
5. **Validate inputs** - Check file paths, formats, and sizes
6. **Monitor resources** - Watch memory and CPU usage
7. **Clean up temp files** - Remove temporary frame files after rendering

## Quick Reference

### Error Message → Solution

| Error Message | Likely Cause | Solution |
|--------------|--------------|----------|
| "File not found" | Wrong path | Use `os.path.abspath()` |
| "renderFrame is not defined" | Missing hook | Add `window.renderFrame` to HTML |
| "Cannot read audio file" | Corrupt file | Re-encode audio |
| "Browser crashed" | Memory issue | Reduce resolution or duration |
| "Codec not supported" | Wrong codec | Use libx264 for video, aac for audio |
| "Timeout exceeded" | Slow rendering | Optimize HTML/CSS, increase timeout |

### Diagnostic Commands

```bash
# Check Python version
python --version

# Check installed packages
pip list | grep -E "moviepy|playwright|opencv"

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Clear cache
pip cache purge

# Check disk space
df -h  # Linux/macOS
dir    # Windows
```

## Getting Help

If you're still stuck:

1. **Check the logs** - Look for error messages in console output
2. **Isolate the issue** - Create a minimal reproduction case
3. **Search similar issues** - Check GitHub issues
4. **Ask for help** - Provide error messages and code snippets

## Next Steps

After fixing the issue:
- Document what you learned
- Add error handling to prevent recurrence
- Share your solution with the community
