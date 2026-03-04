"""HTML 渲染器 - 使用 Playwright 渲染 HTML 帧"""

import asyncio
from typing import List, Tuple, Optional
from playwright.async_api import async_playwright


class HTMLRenderer:
    """
    使用 Playwright 渲染 HTML 帧。
    
    Attributes:
        url (str): HTML 页面 URL
        width (int): 画布宽度
        height (int): 画布高度
        browser: Playwright Browser 实例
        page: Playwright Page 实例
    """
    
    def __init__(self, url: str, width: int, height: int) -> None:
        self.url = url
        self.width = width
        self.height = height
        self.browser = None
        self.page = None
        self._playwright = None
    
    async def initialize(self) -> None:
        """初始化浏览器和页面"""
        self._playwright = await async_playwright().start()
        
        self.browser = await self._playwright.chromium.launch(
            headless=True,
            args=[
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--no-sandbox",
            ]
        )
        
        self.page = await self.browser.new_page(
            viewport={"width": self.width, "height": self.height}
        )
        
        await self.page.goto(self.url)
        print(f"HTML 渲染器已初始化：{self.url}")
    
    async def get_frame(self, frame_index: int) -> Tuple[bytes, List[dict]]:
        """
        渲染指定帧。
        
        Args:
            frame_index (int): 帧索引（从 0 开始）
            
        Returns:
            tuple: (PNG 字节流，Video 占位符坐标列表)
            
        Video 占位符坐标格式:
        {
            "id": str,       # 占位符 data-id
            "x": float,      # X 坐标
            "y": float,      # Y 坐标
            "w": float,      # 宽度
            "h": float,      # 高度
            "zIndex": str    # CSS z-index
        }
        """
        if not self.page:
            raise RuntimeError("HTMLRenderer 未初始化，请先调用 initialize()")
        
        # 1. 调用页面的 renderFrame 钩子
        await self.page.evaluate(f"window.renderFrame({frame_index})")
        
        # 2. 获取所有 Video 占位符的坐标
        bboxes = await self.page.evaluate("""() => {
            const placeholders = document.querySelectorAll('.opencut-video-placeholder');
            return Array.from(placeholders).map(p => {
                const rect = p.getBoundingClientRect();
                const style = window.getComputedStyle(p);
                return {
                    id: p.dataset.id || 'unknown',
                    x: rect.x,
                    y: rect.y,
                    w: rect.width,
                    h: rect.height,
                    zIndex: style.zIndex
                };
            });
        }""")
        
        # 3. 截取透明背景的 PNG
        png_bytes = await self.page.screenshot(
            type="png",
            omit_background=True
        )
        
        return png_bytes, bboxes
    
    async def close(self) -> None:
        """关闭浏览器"""
        if self.browser:
            await self.browser.close()
            self.browser = None
        
        if self._playwright:
            await self._playwright.stop()
            self._playwright = None
        
        print("HTML 渲染器已关闭")
