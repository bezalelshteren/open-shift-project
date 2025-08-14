FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "service_to_sql:app", "--host", "0.0.0.0", "--port","8001"]
