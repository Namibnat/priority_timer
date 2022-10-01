"""Test our timer module"""

import os

import numpy as np

from .helpers import Constants, instantiate_timer, run_timer


class TestTimer:
    @classmethod
    def teardown_class(cls):
        timer = instantiate_timer()
        os.remove(os.path.join(timer.home, timer.timer_dir, timer.record_file))

    def test_timer(self):
        """Test the base case"""
        activity = f'base case {Constants.UNIQUE_ID}'
        timer = run_timer(activity)
        assert timer.file_data['activity'].values[-1] == activity

    def test_timer_csv_file_created(self):
        """Test that the csv file is created"""
        activity = f'csv file created {Constants.UNIQUE_ID}'
        timer = run_timer(activity)
        assert os.path.exists(os.path.join(timer.home, timer.timer_dir, timer.record_file))

    def test_that_duration_is_a_integer(self):
        """Test that the duration is an integer (seconds), as np.int64"""
        activity = f'duration is integer {Constants.UNIQUE_ID}'
        timer = run_timer(activity)
        assert timer.file_data['duration'].dtypes == np.int64
