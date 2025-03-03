FROM python:3.10-slim

WORKDIR /app

# Install SQLite development libraries
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "app.main"]
