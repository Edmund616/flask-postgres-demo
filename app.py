from flask import Flask
import psycopg2
import os
import time
from psycopg2 import OperationalError

app = Flask(__name__)

def wait_for_db():
    max_retries = 5
    retry_delay = 2
    for _ in range(max_retries):
        try:
            conn = psycopg2.connect(
                host="db",
                database=os.getenv('POSTGRES_DB'),
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD'))
            conn.close()
            return True
        except OperationalError:
            time.sleep(retry_delay)
    return False

@app.route('/')
def index():
    if not wait_for_db():
        return "Database connection failed", 500

    return 'Hello, world!'  # ✅ This is the missing return
    # ... rest of your route code ...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)