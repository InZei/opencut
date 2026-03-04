"""本地 HTTP 服务器模块"""

import http.server
import socketserver
import threading
import os
from typing import Optional


class HTTPServer:
    """
    本地 HTTP 服务器，用于提供 HTML 文件访问。
    """
    
    def __init__(self, root_dir: str, port: int = 8000) -> None:
        self.root_dir = os.path.abspath(root_dir)
        self.port = port
        self.server: Optional[socketserver.TCPServer] = None
        self.thread: Optional[threading.Thread] = None
        self.base_url = ""
    
    def start(self) -> str:
        """启动服务器，返回 base_url"""
        os.chdir(self.root_dir)
        
        handler = http.server.SimpleHTTPRequestHandler
        self.server = socketserver.TCPServer(("", self.port), handler)
        
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.daemon = True
        self.thread.start()
        
        self.base_url = f"http://localhost:{self.port}"
        print(f"HTTP 服务器已启动：{self.base_url}")
        return self.base_url
    
    def stop(self) -> None:
        """停止服务器"""
        if self.server:
            self.server.shutdown()
            self.server = None
        if self.thread:
            self.thread.join(timeout=2)
            self.thread = None
        print("HTTP 服务器已停止")


_server_instance: Optional[HTTPServer] = None


def start_server(root_dir: str, port: int = 8000) -> str:
    """启动本地 HTTP 服务器"""
    global _server_instance
    _server_instance = HTTPServer(root_dir, port)
    return _server_instance.start()


def stop_server() -> None:
    """停止本地 HTTP 服务器"""
    global _server_instance
    if _server_instance:
        _server_instance.stop()
        _server_instance = None
