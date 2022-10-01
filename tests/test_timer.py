"""Test our timer module"""

import os
import time

import numpy as np

from src.timer import Timer


class Constants:
    """Constants class"""
    RECORD_FILE = 'timer_records.csv'
    SLEEP_TIME = 5


class TestTimer:
    @classmethod
    def teardown_class(cls):
        timer = TestTimer.instantiate_timer()
        os.remove(os.path.join(timer.home, timer.timer_dir, timer.record_file))

    @staticmethod
    def instantiate_timer(activity=None):
        """Instantiate a timer"""
        return Timer(activity=activity, record_file=Constants.RECORD_FILE, logging=False)

    @staticmethod
    def run_timer(activity):
        timer = TestTimer.instantiate_timer(activity)
        timer.start()
        # Insert some delay
        time.sleep(Constants.SLEEP_TIME)
        timer.end()
        timer.record()
        return timer

    def test_timer(self):
        """Test the base case"""
        activity = 'base case'
        timer = TestTimer.run_timer(activity)
        assert timer.file_data['activity'].values[0] == "base case"

    def test_timer_csv_file_created(self):
        """Test that the csv file is created"""
        activity = 'csv file created'
        timer = TestTimer.run_timer(activity)
        assert os.path.exists(os.path.join(timer.home, timer.timer_dir, timer.record_file))

    def test_that_duration_is_a_integer(self):
        """Test that the duration is an integer (seconds), as np.int64"""
        activity = 'duration is integer'
        timer = TestTimer.run_timer(activity)
        assert timer.file_data['duration'].dtypes == np.int64
