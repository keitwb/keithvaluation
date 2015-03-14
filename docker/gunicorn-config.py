import os

workers = os.environ.get('GUNICORN_WORKERS', 3)
bind = '0.0.0.0:8000'
