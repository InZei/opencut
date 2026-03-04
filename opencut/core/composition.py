"""Composition - 视频构图定义"""

from typing import List
from .sequence import Sequence


class Composition:
    """
    定义一个视频构图，对应 Remotion 的 Composition。
    
    Attributes:
        width (int): 画布宽度（像素），默认 1920
        height (int): 画布高度（像素），默认 1080
        fps (int): 帧率，默认 30
        duration_in_frames (int): 总帧数
        sequences (List[Sequence]): 时间轴序列列表
    """
    
    def __init__(
        self,
        width: int = 1920,
        height: int = 1080,
        fps: int = 30,
        duration_in_frames: int = 300
    ) -> None:
        self.width = width
        self.height = height
        self.fps = fps
        self.duration_in_frames = duration_in_frames
        self.sequences: List[Sequence] = []
    
    def add(self, sequence: Sequence) -> None:
        """添加一个序列到时间轴"""
        self.sequences.append(sequence)
    
    def get_duration_seconds(self) -> float:
        """获取视频总时长（秒）"""
        return self.duration_in_frames / self.fps
