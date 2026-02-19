FROM python:3.10-slim

WORKDIR /app

COPY app/web/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/web .

EXPOSE 5000

CMD ["python", "app.py"]
