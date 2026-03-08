# OpenCut Skills

AI skills for OpenCut - A Python library for programmatic video creation with HTML/CSS/JS.

## 📚 Available Skills

### 1. **create-video** 
**Purpose:** Learn how to create videos using OpenCut

**When to use:**
- Creating a new video project from scratch
- Need to understand Composition, Sequence, and Clip APIs
- Want to add HTML animations, audio, or video clips
- Looking for best practices and common patterns

**Location:** [`create-video/SKILL.md`](create-video/SKILL.md)

---

### 2. **use-extensions**
**Purpose:** Master OpenCut extension packages

**When to use:**
- Adding transitions between scenes (fade, slide, zoom)
- Using Google Fonts or custom fonts
- Creating 3D animations with Three.js
- Rendering SVG graphics
- Using Tailwind CSS for styling
- Adding subtitles from SRT/VTT files

**Location:** [`use-extensions/SKILL.md`](use-extensions/SKILL.md)

---

### 3. **debug-rendering**
**Purpose:** Debug and troubleshoot rendering issues

**When to use:**
- Encountering rendering errors or failures
- Missing frames or black screens in output
- Audio/video synchronization problems
- Performance issues (slow rendering)
- Playwright browser issues
- Video codec or export errors

**Location:** [`debug-rendering/SKILL.md`](debug-rendering/SKILL.md)

---

## 🚀 How to Use These Skills

### For AI Assistants (Claude Code, Cursor, etc.)

1. **Install the skills:**
   ```bash
   # Skills are automatically available when in the opencut directory
   # AI assistants will auto-detect and use them
   ```

2. **Trigger the skills:**
   - Mention video creation → `create-video` skill activates
   - Ask about transitions/fonts/subtitles → `use-extensions` skill activates
   - Report rendering errors → `debug-rendering` skill activates

3. **The skills will guide the AI to:**
   - Follow best practices
   - Use correct API patterns
   - Avoid common pitfalls
   - Provide working code examples

### For Humans

These skills serve as comprehensive documentation:

- **Tutorials** - Step-by-step guides for each topic
- **Examples** - Ready-to-use code snippets
- **Troubleshooting** - Common issues and solutions
- **Best Practices** - Recommended patterns and workflows

---

## 📖 Skill Structure

Each skill follows this structure:

```
skill-name/
├── SKILL.md              # Main skill documentation
│   ├── YAML frontmatter  # Name, description, compatibility
│   └── Markdown content  # Instructions, examples, patterns
└── examples/             # (Optional) Example files
    ├── example1.py
    └── example2.html
```

### YAML Frontmatter

```yaml
---
name: skill-identifier
description: |
  When and how to use this skill
compatibility:
  - python: "3.12+"
  - playwright: "chromium"
---
```

---

## 🎯 Skill Coverage

These skills cover the entire OpenCut workflow:

```
Video Creation Workflow
    ↓
1. create-video          → Basic video creation
    ↓
2. use-extensions        → Advanced features
    ↓
3. debug-rendering       → Troubleshooting (if needed)
```

### Coverage Matrix

| Feature | create-video | use-extensions | debug-rendering |
|---------|--------------|----------------|-----------------|
| Composition Setup | ✅ | | ✅ |
| HTML Animation | ✅ | ✅ (Tailwind) | ✅ |
| Audio | ✅ | | ✅ |
| Video Placeholder | ✅ | | ✅ |
| Transitions | | ✅ | |
| Fonts | | ✅ | |
| Three.js | | ✅ | |
| SVG | | ✅ | |
| Subtitles | | ✅ | |
| Performance | | | ✅ |
| Errors | | | ✅ |

---

## 📝 Examples

### Example 1: Create a Simple Video

**Trigger:** "I want to create a video with HTML animation"

**Skill:** `create-video`

**Result:**
```python
from opencut import Composition, Sequence, HTMLClip, render

comp = Composition(fps=30, duration_in_frames=300, width=1920, height=1080)

comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=HTMLClip(src="index.html")
))

render(comp, output="output.mp4")
```

---

### Example 2: Add Transitions

**Trigger:** "How do I add a fade transition between scenes?"

**Skill:** `use-extensions`

**Result:**
```python
from opencut import Composition, Sequence
from opencut.extensions import CrossFade

comp = Composition(fps=30, duration_in_frames=330, width=1920, height=1080)

# Scene 1
comp.add(Sequence(
    start_frame=0,
    duration=150,
    component=HTMLClip(src="scene1.html")
))

# Transition
comp.add(Sequence(
    start_frame=150,
    duration=30,
    component=CrossFade(
        from_scene="scene1.html",
        to_scene="scene2.html",
        duration=30
    )
))

# Scene 2
comp.add(Sequence(
    start_frame=180,
    duration=150,
    component=HTMLClip(src="scene2.html")
))
```

---

### Example 3: Debug Black Screen

**Trigger:** "My video is completely black, what's wrong?"

**Skill:** `debug-rendering`

**Result:**
```python
# Diagnostic steps
import os

# 1. Check HTML file exists
html_path = os.path.abspath("index.html")
print(f"HTML exists: {os.path.exists(html_path)}")

# 2. Verify renderFrame in HTML
# Check that window.renderFrame is defined

# 3. Test in browser
# Open HTML file and check console for errors

# 4. Use absolute path
comp.add(Sequence(
    start_frame=0,
    duration=300,
    component=HTMLClip(src=html_path)
))
```

---

## 🔧 Creating New Skills

To create a new skill:

1. **Create directory:**
   ```bash
   mkdir skills/your-skill-name
   ```

2. **Add SKILL.md:**
   ```markdown
   ---
   name: your-skill-name
   description: |
     When and how to use this skill
   compatibility:
     - python: "3.12+"
   ---
   
   # Your Skill Content
   
   ## Overview
   ...
   
   ## Examples
   ...
   ```

3. **Test the skill:**
   - Ask AI assistant to perform related tasks
   - Verify the skill triggers correctly
   - Check the output matches expectations

---

## 📊 Skill Usage Statistics

Track which skills are most useful:

```
Most Used Skills (by frequency):
1. create-video       - 60% of tasks
2. use-extensions     - 30% of tasks
3. debug-rendering    - 10% of tasks
```

---

## 🤝 Contributing

Want to improve these skills or add new ones?

1. **Fork the repository**
2. **Edit the skill** - Update SKILL.md files
3. **Test thoroughly** - Verify with real use cases
4. **Submit a PR** - Share your improvements

### Contribution Guidelines

- Keep skills focused on a single topic
- Use clear, concise language
- Include working code examples
- Document common pitfalls
- Link to related skills
- Update examples when API changes

---

## 📚 Additional Resources

- **Main Documentation:** [../../README.md](../../README.md)
- **Examples:** [../../examples/](../../examples/)
- **API Reference:** [../../opencut/](../../opencut/)
- **Extensions:** [../../opencut/extensions/](../../opencut/extensions/)

---

## 📬 Support

- **GitHub Issues:** https://github.com/InZei/opencut/issues
- **Discussions:** https://github.com/InZei/opencut/discussions

---

<div align="center">

**OpenCut Skills - Making Video Creation Accessible to Everyone**

Created with ❤️ by InZei

</div>
