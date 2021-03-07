from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab


app = Celery('celery_conf', broker='pyamqp://guest@localhost//')

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
    enable_utc=True,
    timezone='Europe/Warsaw'
)

app.conf.broker_heartbeat = 0

app.conf.beat_schedule = {
    'Add time log every 60 minutes': {
        'task': 'tasks.add_log',
        'schedule': crontab(minute='*/3'),
        'args': (),
    },
    'Request for page': {
        'task': 'tasks.heroku_request',
        'schedule': crontab(minute='*/3'),
        'args': (),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# if __name__ == '__main__':
#     app.start()
