from tasks import add_log, heroku_request

add_log.delay()
heroku_request.delay()
