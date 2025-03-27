import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

app = Celery('library_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-every-30-seconds': {
        'task': 'tasks.check_overdue_loans',
        'schedule': 30.0,
    },
}
app.conf.timezone = 'UTC'
