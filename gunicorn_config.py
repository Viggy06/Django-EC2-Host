import multiprocessing

# Bind to a Unix socket (recommended for Nginx reverse proxy)
#bind = "unix:/home/ubuntu/core_apps/Billing_System/gunicorn.sock"
bind = "0.0.0.0:8000"  # Bind Gunicorn to localhost on port 8000

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Worker class for ASGI (Django async support)
worker_class = "uvicorn.workers.UvicornWorker"

#Logs
accesslog = '/home/ubuntu/Django-EC2-Host/logs/access.log'
errorlog = '/home/ubuntu/Django-EC2-Host/logs/error.log'
loglevel = 'info'