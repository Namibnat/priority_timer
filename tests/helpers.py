"""Helper method for tests"""

import time
from uuid import uuid4
from src.timer import Timer


class Constants:
    """Constants class"""
    RECORD_FILE = 'test_timer_records.csv'
    SLEEP_TIME = 5
    UNIQUE_ID = str(uuid4())[0:8]


def instantiate_timer(activity=None):
    """Instantiate a timer"""
    return Timer(activity=activity, record_file=Constants.RECORD_FILE, logging=False)


def run_timer(activity):
    timer = instantiate_timer(activity)
    timer.start()
    time.sleep(Constants.SLEEP_TIME)
    timer.end()
    timer.record()
    return timer
