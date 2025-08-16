#!/usr/bin/env python3
"""
极简TODO应用 - DevOps入门示例
只包含最核心的功能，代码保持在100行以内
"""

from flask import Flask, jsonify, request
from datetime import datetime
import uuid

app = Flask(__name__)

# 使用内存存储TODO任务（重启后会丢失，但对学习足够了）
todos = []


@app.route('/health')
def health():
    """健康检查端点 - DevOps监控的基础"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'todo-api',
        'version': '1.0.0'
    })


@app.route('/todos', methods=['GET'])
def get_todos():
    """获取所有TODO任务"""
    return jsonify({
        'todos': todos,
        'count': len(todos)
    })


@app.route('/todos', methods=['POST'])
def add_todo():
    """添加新的TODO任务"""
    data = request.get_json()
    
    # 简单的数据验证
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    # 创建新任务
    todo = {
        'id': str(uuid.uuid4()),
        'title': data['title'],
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    
    todos.append(todo)
    
    return jsonify(todo), 201


@app.route('/')
def index():
    """首页 - 显示API信息"""
    return jsonify({
        'message': 'Welcome to Simple TODO API',
        'endpoints': {
            'GET /health': '健康检查',
            'GET /todos': '获取所有任务',
            'POST /todos': '添加新任务'
        },
        'example': {
            'add_todo': {
                'method': 'POST',
                'url': '/todos',
                'body': {'title': '学习DevOps'}
            }
        }
    })


@app.errorhandler(404)
def not_found(error):
    """处理404错误"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """处理500错误"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    # 开发模式运行
    import os
    port = int(os.environ.get('PORT', 8000))  # 默认使用8000端口
    print("🚀 TODO API 启动中...")
    print(f"📍 访问 http://localhost:{port} 查看API信息")
    print("🔧 这是开发模式，生产环境请使用 gunicorn")
    app.run(host='0.0.0.0', port=port, debug=True)