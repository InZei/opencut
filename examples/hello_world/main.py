"""
Hello World 示例 - OpenCut 入门演示

运行此示例前，请确保已安装依赖：
pip install playwright opencv-python moviepy numpy

首次运行需要安装 Playwright 浏览器：
playwright install chromium
"""

import sys
import os

# 添加 opencut 到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from opencut import Composition, Sequence, HTMLClip, render

# 1. 创建 Composition（视频构图）
comp = Composition(
    fps=30,
    duration_in_frames=150,  # 5 秒 (30fps * 5)
    width=1920,
    height=1080
)

# 2. 添加 HTML 动画层（全长 150 帧）
comp.add(
    Sequence(
        start_frame=0,
        duration=150,
        component=HTMLClip(src="index.html")
    )
)

# 3. 开始渲染
if __name__ == "__main__":
    output_path = render(comp, output="output.mp4")
    print(f"\n✅ 渲染完成！输出文件：{output_path}")
