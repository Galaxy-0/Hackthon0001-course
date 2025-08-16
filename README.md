# 🚀 DevOps入门实战 - 极简TODO API

> 用最简单的项目，体验完整的DevOps流程！2小时从零到部署。

## 📖 项目简介

这是一个为Hackathon新手设计的DevOps入门项目。通过构建一个超简单的TODO API，你将学习：

- ✅ **版本控制** - Git基础操作
- ✅ **自动测试** - 用pytest写测试
- ✅ **容器化** - Docker打包应用
- ✅ **CI/CD** - GitHub Actions自动化
- ✅ **持续集成** - 推代码自动运行测试

## 🎯 学习目标

完成这个项目后，你将理解：
1. 代码提交后发生了什么
2. 测试为什么重要
3. Docker解决了什么问题
4. CI/CD如何提高效率

## 🏗️ 项目结构

```
.
├── app.py              # Flask应用（100行代码）
├── test_app.py         # 测试文件（50行代码）
├── requirements.txt    # Python依赖
├── Dockerfile          # 容器配置（10行）
└── .github/
    └── workflows/
        └── ci.yml      # 自动化流程（30行）
```

## 🚦 快速开始

### 1. 本地运行

```bash
# 使用 uv 创建虚拟环境并安装依赖
uv sync

# 运行应用
uv run python app.py

# 访问 http://localhost:8000
```

### 2. 运行测试

```bash
# 执行所有测试
uv run pytest test_app.py -v
```

### 3. Docker运行

```bash
# 构建镜像
docker build -t todo-app .

# 运行容器
docker run -p 8000:5000 todo-app

# 访问 http://localhost:8000
```

## 📚 API文档

### 健康检查
```
GET /health
Response: {"status": "healthy", "timestamp": "...", "service": "todo-api", "version": "1.0.0"}
```

### 获取所有任务
```
GET /todos
Response: {"todos": [...], "count": 0}
```

### 添加新任务
```
POST /todos
Body: {"title": "学习DevOps"}
Response: {"id": "...", "title": "学习DevOps", "completed": false, "created_at": "..."}
```

## 🔄 DevOps工作流

1. **编写代码** → 修改 `app.py`
2. **编写测试** → 更新 `test_app.py`
3. **本地测试** → 运行 `pytest`
4. **提交代码** → `git add . && git commit -m "message"`
5. **推送代码** → `git push`
6. **自动CI** → GitHub Actions自动运行测试和构建
7. **查看结果** → 在GitHub查看绿色✅或红色❌

## 💡 核心概念

### 什么是DevOps？
DevOps = Development（开发）+ Operations（运维）
目标：让软件交付更快、更可靠、更自动化。

### 为什么要容器化？
- **一致性**：开发环境 = 测试环境 = 生产环境
- **可移植**：在任何地方都能运行
- **隔离性**：应用之间互不影响

### CI/CD是什么？
- **CI（持续集成）**：代码提交后自动测试
- **CD（持续交付）**：测试通过后自动部署

## 🎓 学习路径

### 已完成 ✅
- [x] 基础Web API
- [x] 自动化测试
- [x] Docker容器化
- [x] GitHub Actions CI

### 下一步 📈
- [ ] 添加数据库（SQLite → PostgreSQL）
- [ ] 用户认证（JWT）
- [ ] 部署到云（Heroku/Railway）
- [ ] 监控和日志（Prometheus/Grafana）
- [ ] Kubernetes编排

## 🤝 贡献

欢迎提交Issue和Pull Request！这是练习Git协作的好机会。

## 📝 许可

MIT License - 随意使用和修改！

---

**记住：最好的学习方式是动手实践！** 🚀

