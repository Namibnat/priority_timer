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
