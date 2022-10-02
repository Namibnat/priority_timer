"""Helper method for tests"""

import datetime
from uuid import uuid4
from src.timer import Timer


class Constants:
    """Constants class"""
    RECORD_FILE = 'test_timer_records.csv'
    ACTIVITY_DURATION = 5
    UNIQUE_ID = str(uuid4())[0:8]


def instantiate_timer(activity=None):
    """Instantiate a timer"""
    return Timer(activity=activity, record_file=Constants.RECORD_FILE, logging=False)


def run_timer(activity, set_duration=Constants.ACTIVITY_DURATION):
    """Run a timer for tests"""
    timer = instantiate_timer(activity)
    timer.start()
    # Override timer.end() to save time, otherwise we have to wait a few seconds
    timer.defines.STOP = timer.defines.START + datetime.timedelta(seconds=set_duration)
    timer.defines.DURATION = (timer.defines.STOP - timer.defines.START).seconds
    timer.record()
    return timer
