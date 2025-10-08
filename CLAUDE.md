# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DevOps入门教学项目 - 一个极简的TODO API，用于学习DevOps核心概念。
技术栈：Python Flask + Docker + GitHub Actions

## Common Commands

### Development
```bash
# Install dependencies with uv
uv sync

# Run application locally
uv run python app.py

# Run tests
uv run pytest test_app.py -v

# Run specific test
uv run pytest test_app.py::test_health_check -v
```

### Docker
```bash
# Build Docker image
docker build -t todo-app .

# Run container
docker run -p 8000:5000 todo-app

# Run container in background
docker run -d -p 8000:5000 --name todo-app todo-app

# Stop container
docker stop todo-app

# View logs
docker logs todo-app
```

### API Testing
```bash
# Health check
curl http://localhost:8000/health

# Get todos
curl http://localhost:8000/todos

# Add todo
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn DevOps"}'
```

## Project Structure

- `app.py` - Flask application with TODO API endpoints (100 lines)
- `test_app.py` - pytest test suite with 6 test cases
- `pyproject.toml` - Project configuration with uv dependency management
- `requirements.txt` - Production dependencies (Flask, gunicorn)
- `requirements-dev.txt` - Development dependencies (includes pytest)
- `Dockerfile` - Container configuration for production
- `.github/workflows/ci.yml` - GitHub Actions CI pipeline with Docker testing

## Key Features

1. **REST API Endpoints**:
   - `GET /` - API information
   - `GET /health` - Health check for monitoring
   - `GET /todos` - Retrieve all todos
   - `POST /todos` - Create new todo

2. **Testing**: Full test coverage with pytest
3. **Containerization**: Docker support with gunicorn
4. **CI/CD**: Automated testing and building via GitHub Actions

## Development Workflow

1. Make changes to code
2. Run tests locally: `uv run pytest test_app.py -v`
3. Build and test Docker image locally
4. Commit and push changes
5. GitHub Actions will automatically run tests and build Docker image
6. CI pipeline tests Docker container health endpoint

## Architecture Notes

- **In-memory storage**: Uses Python list for todos (intentionally simple for learning)
- **Single-file Flask app**: All endpoints in `app.py` with error handling
- **Test coverage**: 6 test cases covering all endpoints and error scenarios
- **Container ready**: Runs with gunicorn in production mode via Docker
- **CI/CD validation**: GitHub Actions tests both Python and Docker environments

## Important Notes

- The app uses in-memory storage (todos list) - data is lost on restart
- This is intentional for learning purposes - keeps things simple
- Production deployment would require persistent storage (database)