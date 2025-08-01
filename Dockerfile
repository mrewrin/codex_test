FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY server ./server
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
