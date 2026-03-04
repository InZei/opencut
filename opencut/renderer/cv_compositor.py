"""CV 合成器 - OpenCV 视频合成（MVP 预留接口）"""

import numpy as np
from typing import List, Tuple, Optional


class CVCompositor:
    """
    使用 OpenCV 合成视频帧（MVP 阶段预留接口）。
    
    后续实现：
    1. 读取 VideoClip 对应的视频帧
    2. 缩放到占位符尺寸
    3. Alpha Blending 到画布
    """
    
    def __init__(self) -> None:
        pass
    
    def compose_frame(
        self,
        bg_color: Tuple[int, int, int] = (0, 0, 0),
        width: int = 1920,
        height: int = 1080,
        video_frames_data: Optional[List[dict]] = None,
        html_png_bytes: Optional[bytes] = None
    ) -> np.ndarray:
        """
        合成单帧。
        
        Args:
            bg_color: 背景颜色 (R, G, B)，默认黑色
            width: 画布宽度
            height: 画布高度
            video_frames_data: 视频帧数据（MVP 阶段未使用）
            html_png_bytes: HTML 层 PNG 字节流
            
        Returns:
            np.ndarray: 合成后的帧 (H, W, 3)
            
        MVP 实现：
        - 如果有 html_png_bytes，解码并返回
        - 否则返回纯色背景
        """
        # 创建背景画布
        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        canvas[:] = bg_color
        
        # MVP 阶段：如果有 HTML 层，简单叠加（暂不处理 Alpha 通道）
        if html_png_bytes:
            try:
                import cv2
                html_np = np.frombuffer(html_png_bytes, np.uint8)
                html_img = cv2.imdecode(html_np, cv2.IMREAD_UNCHANGED)
                
                if html_img is not None:
                    # 如果有 Alpha 通道，进行 Alpha Blending
                    if html_img.shape[2] == 4:
                        canvas = self._alpha_blend(canvas, html_img)
                    else:
                        # 直接覆盖
                        h, w = html_img.shape[:2]
                        canvas[0:h, 0:w] = html_img[:, :, :3]
            except ImportError:
                print("警告：OpenCV 未安装，跳过 HTML 层合成")
            except Exception as e:
                print(f"警告：HTML 层合成失败：{e}")
        
        return canvas
    
    def _alpha_blend(
        self,
        bg: np.ndarray,
        fg: np.ndarray
    ) -> np.ndarray:
        """
        高效的 Alpha 通道合并算法（Numpy）
        
        Args:
            bg: 底图 (H, W, 3)
            fg: 带有透明通道的前景图 (h, w, 4)
            
        Returns:
            np.ndarray: 合成后的图像
        """
        h, w = fg.shape[:2]
        
        # 确保前景图不超过背景图
        if h > bg.shape[0] or w > bg.shape[1]:
            return bg
        
        fg_rgb = fg[:, :, :3].astype(np.float32)
        alpha = fg[:, :, 3].astype(np.float32) / 255.0
        alpha = np.expand_dims(alpha, axis=2)
        
        # 提取底图对应的 ROI
        roi = bg[0:h, 0:w].astype(np.float32)
        
        # 公式：result = fg * alpha + bg * (1 - alpha)
        blended = (fg_rgb * alpha + roi * (1 - alpha)).astype(np.uint8)
        bg[0:h, 0:w] = blended
        
        return bg
