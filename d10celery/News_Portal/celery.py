import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News_Portal.settings')

app = Celery('News_Portal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'DB_app.tasks.send_weekly_mail',
        'schedule': crontab(minute='0', hour='5', day_of_week='monday'),
    },
}
app.conf.timezone = 'UTC'
app.autodiscover_tasks()
