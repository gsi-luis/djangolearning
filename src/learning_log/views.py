from django.shortcuts import render
import logging
import datetime
from collections import deque
from learning_django import settings

# Get an instance of a logger
logger = logging.getLogger('learning_django')


def index(request):
    logger.debug("Example log message type 'debug' " + str(datetime.datetime.now()))
    logger.info("Example log message type 'info' " + str(datetime.datetime.now()))
    logger.warning("Example log message type 'warning' " + str(datetime.datetime.now()))
    logger.error("Example log message type 'error' " + str(datetime.datetime.now()))
    logger.critical("Example log message type 'critical' " + str(datetime.datetime.now()))

    with open(settings.BASE_DIR+'/debug.log') as f:
        last_lines = deque(f, 10)

    context = {'logs': last_lines}
    return render(request, 'learning_log/log_index.html', context)
