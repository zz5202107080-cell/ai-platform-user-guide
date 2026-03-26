#!/usr/bin/env python3
"""
简易静态文件服务器，用于本地预览 docsify 文档
"""

import http.server
import socketserver
import os
import sys

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # 添加 CORS 头部，方便本地开发
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        # 简化日志输出
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

if __name__ == '__main__':
    os.chdir(DIRECTORY)

    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"\n📚 AI大模型聚合平台 用户指南")
            print(f"🔗 本地预览地址: http://localhost:{PORT}")
            print(f"📁 文档目录: {DIRECTORY}")
            print(f"🛑 按 Ctrl+C 停止服务器\n")
            print("正在启动服务器...")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
    except OSError as e:
        if e.errno == 48:  # 端口被占用
            print(f"错误: 端口 {PORT} 已被占用，请尝试其他端口")
            print(f"使用方法: python serve.py [端口号]")
            sys.exit(1)
        else:
            raise