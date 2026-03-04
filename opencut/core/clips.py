"""Clips - HTML、Video、Audio 组件定义"""

from typing import Optional


class HTMLClip:
    """
    HTML 渲染组件。
    
    Attributes:
        src (str): HTML 文件路径或 URL
        props (dict, optional): 传递给 JS 的属性
    """
    
    def __init__(self, src: str, props: Optional[dict] = None) -> None:
        self.src = src
        self.props = props or {}
    
    def __repr__(self) -> str:
        return f"HTMLClip(src={self.src!r}, props={self.props!r})"


class VideoClip:
    """
    视频组件（MVP 阶段为占位符，后续用 OpenCV 填充）。
    
    Attributes:
        src (str): 视频文件路径
        bind_id (str): 绑定到 HTML 中的占位符 data-id
        start_frame (int, optional): 视频起始帧（相对于 Sequence）
    """
    
    def __init__(
        self,
        src: str,
        bind_id: str,
        start_frame: int = 0
    ) -> None:
        self.src = src
        self.bind_id = bind_id
        self.start_frame = start_frame
    
    def __repr__(self) -> str:
        return f"VideoClip(src={self.src!r}, bind_id={self.bind_id!r})"


class AudioClip:
    """
    音频组件。
    
    Attributes:
        src (str): 音频文件路径
        volume (float, optional): 音量 (0.0-1.0)，默认 1.0
    """
    
    def __init__(self, src: str, volume: float = 1.0) -> None:
        self.src = src
        self.volume = max(0.0, min(1.0, volume))
    
    def __repr__(self) -> str:
        return f"AudioClip(src={self.src!r}, volume={self.volume!r})"
