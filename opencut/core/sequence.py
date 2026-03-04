"""Sequence - 时间轴序列定义"""

from typing import Union
from .clips import HTMLClip, VideoClip, AudioClip


class Sequence:
    """
    定义时间轴上的一个片段，对应 Remotion 的 Sequence。
    
    Attributes:
        start_frame (int): 序列开始的帧（相对于 Composition）
        duration (int): 序列持续的帧数
        component (HTMLClip | VideoClip | AudioClip): 组件实例
    """
    
    def __init__(
        self,
        start_frame: int,
        duration: int,
        component: Union[HTMLClip, VideoClip, AudioClip]
    ) -> None:
        self.start_frame = start_frame
        self.duration = duration
        self.component = component
    
    def get_end_frame(self) -> int:
        """获取序列结束帧"""
        return self.start_frame + self.duration
