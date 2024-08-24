# FROM python:3.12.5-slim
FROM python:3.12.5-slim-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]

EXPOSE 8000