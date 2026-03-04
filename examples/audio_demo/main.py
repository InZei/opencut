"""
Audio Demo 示例 - 音频合成演示

运行此示例前，请确保：
1. 已安装依赖：pip install playwright opencv-python moviepy numpy
2. 已安装 Playwright 浏览器：playwright install chromium
3. 准备一个音频文件 music.mp3（或使用脚本生成的测试音频）

如果没有 audio.mp3，脚本会自动生成一个测试音频。
"""

import sys
import os
import subprocess

# 添加 opencut 到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from opencut import Composition, Sequence, HTMLClip, AudioClip, render


def create_test_audio(output_path: str, duration: float = 10.0) -> None:
    """
    使用 MoviePy 生成测试音频（正弦波）
    
    Args:
        output_path: 输出文件路径
        duration: 音频时长（秒）
    """
    try:
        from moviepy.editor import AudioClip
        import numpy as np
        
        print(f"生成测试音频：{output_path} ({duration}秒)")
        
        # 生成 440Hz 正弦波（A 音）
        sample_rate = 44100
        duration_frames = int(sample_rate * duration)
        t = np.linspace(0, duration, duration_frames)
        
        # 创建音频数据（440Hz + 880Hz 叠加）
        audio_data = (
            0.5 * np.sin(2 * np.pi * 440 * t) +
            0.3 * np.sin(2 * np.pi * 880 * t)
        ).astype(np.float32)
        
        # 创建音频片段
        audio_clip = AudioClip(
            audio_data.tobytes(),
            fps=sample_rate,
            buffersize=audio_data.nbytes
        )
        
        # 导出为 MP3
        audio_clip.write_audiofile(
            output_path,
            fps=sample_rate,
            verbose=False,
            logger=None
        )
        
        print(f"测试音频已生成：{output_path}")
        
    except Exception as e:
        print(f"警告：无法生成测试音频：{e}")
        print("请手动准备一个 audio.mp3 文件")


if __name__ == "__main__":
    # 检查音频文件是否存在
    audio_path = os.path.join(os.path.dirname(__file__), "audio.mp3")
    
    if not os.path.exists(audio_path):
        print("未找到 audio.mp3，正在生成测试音频...")
        create_test_audio(audio_path, duration=10.0)
    
    # 1. 创建 Composition
    comp = Composition(
        fps=30,
        duration_in_frames=300,  # 10 秒
        width=1920,
        height=1080
    )
    
    # 2. 添加 HTML 动画层
    comp.add(
        Sequence(
            start_frame=0,
            duration=300,
            component=HTMLClip(src="index.html")
        )
    )
    
    # 3. 添加音频轨道
    if os.path.exists(audio_path):
        comp.add(
            Sequence(
                start_frame=0,
                duration=300,
                component=AudioClip(src=audio_path, volume=0.8)
            )
        )
        print(f"使用音频文件：{audio_path}")
    else:
        print("警告：未找到音频文件，将生成无音频视频")
    
    # 4. 开始渲染
    output_path = render(comp, output="audio_demo.mp4")
    print(f"\n✅ 渲染完成！输出文件：{output_path}")
