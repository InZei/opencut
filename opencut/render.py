"""主渲染流程"""

import os
import shutil
import tempfile
import asyncio
from typing import Optional
from .core import Composition, Sequence, HTMLClip, VideoClip, AudioClip
from .renderer import HTMLRenderer, CVCompositor, Exporter


def render(composition: Composition, output: str) -> str:
    """
    渲染视频。
    
    Args:
        composition (Composition): 视频构图定义
        output (str): 输出文件路径
        
    Returns:
        str: 输出文件路径
        
    渲染流程：
    1. 初始化 Playwright 渲染器（直接加载本地 HTML 文件）
    2. 逐帧渲染（HTML → PNG）
    3. 使用 MoviePy 合成音频
    4. 导出最终视频
    5. 清理临时文件
    """
    print("=" * 60)
    print("OpenCut 渲染引擎 v0.1.0")
    print("=" * 60)
    
    # 1. 准备临时目录
    temp_dir = tempfile.mkdtemp(prefix="opencut_")
    frames_dir = os.path.join(temp_dir, "frames")
    os.makedirs(frames_dir)
    
    print(f"临时目录：{temp_dir}")
    print(f"输出文件：{output}")
    print(f"视频规格：{composition.width}x{composition.height} @ {composition.fps}fps, {composition.duration_in_frames}帧")
    
    # 2. 查找 HTML 文件路径
    html_clip = None
    html_path = None
    
    for seq in composition.sequences:
        if isinstance(seq.component, HTMLClip):
            html_clip = seq.component
            html_path = os.path.abspath(html_clip.src)
            break
    
    if not html_clip:
        raise ValueError("未找到 HTMLClip，至少需要一个 HTML 组件")
    
    if not os.path.exists(html_path):
        raise FileNotFoundError(f"HTML 文件不存在：{html_clip.src}")
    
    print(f"HTML 文件：{html_path}")
    
    # 3. 收集音频轨道
    audio_clips = []
    for seq in composition.sequences:
        if isinstance(seq.component, AudioClip):
            audio_clips.append(seq.component)
    
    # 4. 初始化渲染器
    renderer = HTMLRenderer(html_path, composition.width, composition.height)
    compositor = CVCompositor()
    
    # 5. 异步渲染循环
    async def render_frames():
        try:
            await renderer.initialize()
            
            print(f"开始渲染 {composition.duration_in_frames} 帧...")
            
            for frame_idx in range(composition.duration_in_frames):
                # 渲染单帧
                png_bytes, video_placeholders = await renderer.get_frame(frame_idx)
                
                # MVP 阶段：直接使用 HTML 渲染结果（不合成视频）
                # 后续：使用 compositor.compose_frame() 合成视频帧
                
                # 保存帧到临时目录
                frame_path = os.path.join(frames_dir, f"{frame_idx:05d}.png")
                with open(frame_path, "wb") as f:
                    f.write(png_bytes)
                
                # 进度显示
                if (frame_idx + 1) % 30 == 0 or frame_idx == composition.duration_in_frames - 1:
                    progress = (frame_idx + 1) / composition.duration_in_frames * 100
                    print(f"渲染进度：{frame_idx + 1}/{composition.duration_in_frames} ({progress:.1f}%)")
            
            print("帧渲染完成！")
            
        finally:
            await renderer.close()
    
    # 6. 执行异步渲染
    asyncio.run(render_frames())
    
    # 7. 导出视频
    try:
        Exporter.export_video(
            frames_dir=frames_dir,
            audio_clips=audio_clips,
            fps=composition.fps,
            output_path=output
        )
    except Exception as e:
        print(f"导出失败：{e}")
        raise
    finally:
        # 8. 清理资源
        # 清理临时目录
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"临时目录已清理：{temp_dir}")
    
    print("=" * 60)
    print("渲染完成！")
    print("=" * 60)
    
    return output
