FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY extract_outline.py .

RUN mkdir -p input output

CMD ["python", "extract_outline.py"]
