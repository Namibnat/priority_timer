"""Test getting data back from the csv file"""

import os

from src.data import TimerData
from .helpers import run_timer, Constants, instantiate_timer


class TestTimerData:
    @classmethod
    def teardown_class(cls):
        timer = instantiate_timer()
        os.remove(os.path.join(timer.home, timer.timer_dir, timer.record_file))

    def test_get_data(self):
        """Test getting data back from the csv file"""
        activity = f'get data {Constants.UNIQUE_ID}'
        timer = run_timer(activity)
        timer_data = TimerData(record_file=timer.record_file)
        data = timer_data.activities_to_namedtuple()
        assert data[-1].activity == activity

    def test_get_length_of_data(self):
        """Test getting the length of the data"""
        activity = f'get length of data {Constants.UNIQUE_ID}'
        timer = run_timer(activity)
        _ = TimerData(record_file=timer.record_file)
        activity = f'get length of data 2 {Constants.UNIQUE_ID}'
        timer = run_timer(activity)
        timer_data = TimerData(record_file=timer.record_file)
        assert len(timer_data) >= 2

    def test_get_data_by_index(self):
        """Test getting data by index"""
        activity = f'get data by index {Constants.UNIQUE_ID}'
        timer = run_timer(activity)
        _ = TimerData(record_file=timer.record_file)
        activity2 = f'get data by index 2 {Constants.UNIQUE_ID}'
        timer = run_timer(activity2)
        timer_data = TimerData(record_file=timer.record_file)
        assert timer_data[len(timer_data) - 2].activity == activity

    def test_sum_duration(self):
        """Test summing the duration"""
        timer_data = None
        for i in range(5):
            activity = f'sum duration {Constants.UNIQUE_ID} {i}'
            timer = run_timer(activity)
            timer_data = TimerData(record_file=timer.record_file)
        if hasattr(timer_data, 'sum_duration'):
            assert timer_data.sum_duration() >= 5 * Constants.ACTIVITY_DURATION
        else:
            assert False

    def test_max_duration(self):
        """Test max duration"""
        activity_max = f'max duration'
        timer = run_timer(activity_max, set_duration=Constants.ACTIVITY_DURATION * 2)
        timer_data = TimerData(record_file=timer.record_file)
        for i in range(5):
            activity = f'max duration {Constants.UNIQUE_ID} {i}'
            timer = run_timer(activity)
            timer_data = TimerData(record_file=timer.record_file)
        if hasattr(timer_data, 'max_duration'):
            longest_activity = timer_data.max_duration()
            assert longest_activity.activity == activity_max
        else:
            assert False
