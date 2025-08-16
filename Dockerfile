# 极简Docker配置 - 体验容器化的魔力
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY app.py .

# 暴露端口
EXPOSE 5000

# 使用gunicorn运行（生产环境）
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]