# CoWorkConnect/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# ustawienie domyślnych ustawień Django dla Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CoWorkConnect.settings')

app = Celery('CoWorkConnect')

# używamy ustawień Django jako konfiguracji dla Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# automatyczne wykrywanie zadań w aplikacjach Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
