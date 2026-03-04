"""导出器 - 使用 MoviePy 导出最终视频"""

import os
from typing import List, Optional
from ..core.clips import AudioClip


class Exporter:
    """
    使用 MoviePy 导出最终视频。
    """
    
    @staticmethod
    def export_video(
        frames_dir: str,
        audio_clips: List[AudioClip],
        fps: int,
        output_path: str,
        frame_range: Optional[tuple] = None
    ) -> str:
        """
        导出视频。
        
        Args:
            frames_dir: PNG 序列目录
            audio_clips: 音频组件列表
            fps: 帧率
            output_path: 输出文件路径
            frame_range: 帧范围 (start, end)
            
        Returns:
            str: 输出文件路径
        """
        try:
            # MoviePy 2.x 导入路径
            from moviepy import (
                ImageSequenceClip,
                AudioFileClip,
                CompositeAudioClip
            )
        except ImportError:
            try:
                # MoviePy 1.x 导入路径（向后兼容）
                from moviepy.editor import (
                    ImageSequenceClip,
                    AudioFileClip,
                    CompositeAudioClip
                )
            except ImportError:
                raise ImportError(
                    "MoviePy 未安装，请运行：pip install moviepy"
                )
        
        # 1. 获取所有帧文件
        frame_files = sorted([
            os.path.join(frames_dir, f)
            for f in os.listdir(frames_dir)
            if f.endswith('.png')
        ])
        
        if not frame_files:
            raise ValueError(f"帧目录为空：{frames_dir}")
        
        # 2. 应用帧范围过滤
        if frame_range:
            start, end = frame_range
            frame_files = frame_files[start:end]
        
        print(f"加载 {len(frame_files)} 帧图像...")
        
        # 3. 创建视频片段
        video_clip = ImageSequenceClip(frame_files, fps=fps)
        
        # 4. 处理音频轨道
        if audio_clips:
            print(f"合成 {len(audio_clips)} 个音频轨道...")
            audio_file_clips = []
            
            for audio_clip in audio_clips:
                try:
                    clip = AudioFileClip(audio_clip.src)
                    clip = clip.volumex(audio_clip.volume)
                    audio_file_clips.append(clip)
                except Exception as e:
                    print(f"警告：加载音频失败 {audio_clip.src}: {e}")
            
            if audio_file_clips:
                # 合并所有音频轨道
                final_audio = CompositeAudioClip(audio_file_clips)
                video_clip = video_clip.set_audio(final_audio)
        
        # 5. 确保输出目录存在
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # 6. 导出视频
        print(f"导出视频到：{output_path}")
        video_clip.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac",
            fps=fps,
            preset="medium",
            threads=4
        )
        
        # 7. 清理资源
        video_clip.close()
        
        print(f"视频导出完成：{output_path}")
        return output_path
