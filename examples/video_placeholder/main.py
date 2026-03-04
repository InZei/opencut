"""
Video Placeholder 示例 - Video 占位符机制演示

此示例展示 Opencut 的分离渲染架构：
1. HTML 层使用 Playwright 渲染（带透明背景）
2. Video 占位符提取坐标信息
3. MVP 阶段暂不合成视频帧（预留 OpenCV 接口）

运行此示例前，请确保：
1. 已安装依赖：pip install playwright opencv-python moviepy numpy
2. 已安装 Playwright 浏览器：playwright install chromium

可选：准备 background.mp4 文件用于后续 OpenCV 合成测试
"""

import sys
import os

# 添加 opencut 到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from opencut import Composition, Sequence, HTMLClip, VideoClip, render


def create_test_video(output_path: str, duration: float = 5.0) -> None:
    """
    使用 MoviePy 生成测试视频（彩色渐变）
    
    Args:
        output_path: 输出文件路径
        duration: 视频时长（秒）
    """
    try:
        from moviepy.editor import VideoClip
        import numpy as np
        
        print(f"生成测试视频：{output_path} ({duration}秒)")
        
        def make_frame(t):
            # 创建渐变背景
            h, w = 1080, 1920
            y, x = np.ogrid[:h, :w]
            
            # 随时间变化的颜色
            r = (np.sin(t * 0.5) * 0.5 + 0.5) * 255
            g = (np.cos(t * 0.3) * 0.5 + 0.5) * 255
            b = 128
            
            frame = np.zeros((h, w, 3), dtype=np.uint8)
            frame[:, :, 0] = r.astype(np.uint8)
            frame[:, :, 1] = g.astype(np.uint8)
            frame[:, :, 2] = b
            
            return frame
        
        video = VideoClip(make_frame, duration=duration)
        video.write_videofile(
            output_path,
            fps=30,
            verbose=False,
            logger=None
        )
        
        print(f"测试视频已生成：{output_path}")
        
    except Exception as e:
        print(f"警告：无法生成测试视频：{e}")
        print("请手动准备一个 background.mp4 文件")


if __name__ == "__main__":
    # 检查视频文件是否存在
    video_path = os.path.join(os.path.dirname(__file__), "background.mp4")
    
    if not os.path.exists(video_path):
        print("未找到 background.mp4，正在生成测试视频...")
        create_test_video(video_path, duration=5.0)
    
    # 1. 创建 Composition
    comp = Composition(
        fps=30,
        duration_in_frames=150,  # 5 秒
        width=1920,
        height=1080
    )
    
    # 2. 添加 HTML 动画层
    comp.add(
        Sequence(
            start_frame=0,
            duration=150,
            component=HTMLClip(src="index.html")
        )
    )
    
    # 3. 添加 Video（MVP 阶段仅提取占位符坐标）
    if os.path.exists(video_path):
        comp.add(
            Sequence(
                start_frame=0,
                duration=150,
                component=VideoClip(
                    src=video_path,
                    bind_id="main_video"
                )
            )
        )
        print(f"使用视频文件：{video_path}")
        print("注意：MVP 阶段 VideoClip 仅提取占位符坐标，不进行视频合成")
    else:
        print("警告：未找到视频文件，将生成无视频版本")
    
    # 4. 开始渲染
    output_path = render(comp, output="video_placeholder.mp4")
    print(f"\n✅ 渲染完成！输出文件：{output_path}")
    print("\n💡 提示：后续版本将实现 OpenCV 视频帧合成功能")
