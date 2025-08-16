#!/usr/bin/env python3
"""
测试文件 - 体验自动化测试的重要性
保持简单，只测试核心功能
"""

import pytest
import json
from app import app


@pytest.fixture
def client():
    """创建测试客户端"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    """测试健康检查端点"""
    response = client.get('/health')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['status'] == 'healthy'
    assert 'timestamp' in data
    assert data['service'] == 'todo-api'
    print("✅ 健康检查测试通过")


def test_get_todos_empty(client):
    """测试获取空的TODO列表"""
    response = client.get('/todos')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert 'todos' in data
    assert 'count' in data
    assert data['count'] == 0
    print("✅ 获取空TODO列表测试通过")


def test_add_todo(client):
    """测试添加新TODO"""
    new_todo = {'title': '学习DevOps'}
    response = client.post('/todos', 
                          data=json.dumps(new_todo),
                          content_type='application/json')
    data = json.loads(response.data)
    
    assert response.status_code == 201
    assert data['title'] == '学习DevOps'
    assert 'id' in data
    assert data['completed'] == False
    assert 'created_at' in data
    print("✅ 添加TODO测试通过")


def test_add_todo_without_title(client):
    """测试添加没有标题的TODO（应该失败）"""
    response = client.post('/todos', 
                          data=json.dumps({}),
                          content_type='application/json')
    data = json.loads(response.data)
    
    assert response.status_code == 400
    assert 'error' in data
    print("✅ 验证错误处理测试通过")


def test_get_todos_after_adding(client):
    """测试添加TODO后获取列表"""
    # 先添加一个TODO
    client.post('/todos', 
                data=json.dumps({'title': '写测试'}),
                content_type='application/json')
    
    # 再获取列表
    response = client.get('/todos')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['count'] == 1
    assert len(data['todos']) == 1
    assert data['todos'][0]['title'] == '写测试'
    print("✅ 完整流程测试通过")


def test_index_page(client):
    """测试首页API信息"""
    response = client.get('/')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert 'message' in data
    assert 'endpoints' in data
    print("✅ 首页测试通过")


if __name__ == '__main__':
    # 可以直接运行这个文件来执行测试
    pytest.main([__file__, '-v'])