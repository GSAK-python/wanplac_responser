import webbrowser
from celery import shared_task, Celery
import requests
import datetime


app = Celery('tasks', broker='pyamqp://guest@localhost//')


@shared_task
def heroku_request():
    webpage = 'https://wanplac.herokuapp.com/main/'
    print('Starting script...\n')
    response = requests.get(webpage)
    with open("log.txt", "a") as myfile:
        myfile.write('{} Webpage has been pinged'.format(webpage) + "\n")
    print('{} Webpage has been pinged\n'.format(webpage))
    return response


@shared_task
def add_log():
    print('Adding text')
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("log.txt", "a") as myfile:
        myfile.write(time + "\n")
    return "Log has been added"


#  celery -A tasks worker --pool=solo -l info
#  celery -A celery_settings beat
