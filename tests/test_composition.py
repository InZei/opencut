"""测试 Composition 和 Sequence API"""

import sys
import os

# 添加 opencut 到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from opencut import Composition, Sequence, HTMLClip, VideoClip, AudioClip


def test_composition_creation():
    """测试 Composition 创建"""
    print("测试 1: 创建 Composition...")
    
    comp = Composition(
        fps=30,
        duration_in_frames=150,
        width=1920,
        height=1080
    )
    
    assert comp.fps == 30
    assert comp.duration_in_frames == 150
    assert comp.width == 1920
    assert comp.height == 1080
    assert len(comp.sequences) == 0
    
    print("✅ Composition 创建成功")


def test_sequence_creation():
    """测试 Sequence 创建"""
    print("\n测试 2: 创建 Sequence...")
    
    html_clip = HTMLClip(src="test.html")
    seq = Sequence(
        start_frame=0,
        duration=150,
        component=html_clip
    )
    
    assert seq.start_frame == 0
    assert seq.duration == 150
    assert seq.component == html_clip
    assert seq.get_end_frame() == 150
    
    print("✅ Sequence 创建成功")


def test_clips_creation():
    """测试各种 Clip 创建"""
    print("\n测试 3: 创建 Clips...")
    
    # HTMLClip
    html_clip = HTMLClip(src="index.html", props={"title": "Test"})
    assert html_clip.src == "index.html"
    assert html_clip.props == {"title": "Test"}
    print("  - HTMLClip ✓")
    
    # VideoClip
    video_clip = VideoClip(src="video.mp4", bind_id="main_video")
    assert video_clip.src == "video.mp4"
    assert video_clip.bind_id == "main_video"
    print("  - VideoClip ✓")
    
    # AudioClip
    audio_clip = AudioClip(src="audio.mp3", volume=0.8)
    assert audio_clip.src == "audio.mp3"
    assert audio_clip.volume == 0.8
    print("  - AudioClip ✓")
    
    print("✅ 所有 Clips 创建成功")


def test_composition_add_sequence():
    """测试 Composition 添加 Sequence"""
    print("\n测试 4: Composition 添加 Sequence...")
    
    comp = Composition(fps=30, duration_in_frames=300)
    
    # 添加 HTML Sequence
    html_seq = Sequence(
        start_frame=0,
        duration=300,
        component=HTMLClip(src="index.html")
    )
    comp.add(html_seq)
    assert len(comp.sequences) == 1
    
    # 添加 Audio Sequence
    audio_seq = Sequence(
        start_frame=0,
        duration=300,
        component=AudioClip(src="audio.mp3")
    )
    comp.add(audio_seq)
    assert len(comp.sequences) == 2
    
    # 添加 Video Sequence
    video_seq = Sequence(
        start_frame=0,
        duration=300,
        component=VideoClip(src="video.mp4", bind_id="main")
    )
    comp.add(video_seq)
    assert len(comp.sequences) == 3
    
    print("✅ Composition 添加 Sequence 成功")


def test_composition_duration():
    """测试 Composition 时长计算"""
    print("\n测试 5: Composition 时长计算...")
    
    comp = Composition(fps=30, duration_in_frames=300)
    assert comp.get_duration_seconds() == 10.0
    
    comp2 = Composition(fps=60, duration_in_frames=180)
    assert comp2.get_duration_seconds() == 3.0
    
    print("✅ Composition 时长计算正确")


if __name__ == "__main__":
    print("=" * 60)
    print("OpenCut 单元测试")
    print("=" * 60)
    
    test_composition_creation()
    test_sequence_creation()
    test_clips_creation()
    test_composition_add_sequence()
    test_composition_duration()
    
    print("\n" + "=" * 60)
    print("✅ 所有测试通过！")
    print("=" * 60)
