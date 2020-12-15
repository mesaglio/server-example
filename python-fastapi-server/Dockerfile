FROM python:3.9-slim

COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT ["python3","src/main.py"]