"""Test our timer module"""

import os

from src.timer import Timer


class TestTimer:
    @classmethod
    def teardown_class(cls):
        timer = Timer(activity=None, record_file='test_timer_records.csv')
        os.remove(os.path.join(timer.home, timer.timer_dir, timer.record_file))

    def test_timer(self):
        """Test the base case"""
        timer = Timer(activity="base case", record_file='test_timer_records.csv')
        timer.start()
        timer.end()
        timer.record()
        assert timer.file_data['activity'].values[0] == "base case"

    def test_timer_csv_file_created(self):
        """Test that the csv file is created"""
        timer = Timer(activity="test file", record_file='test_timer_records.csv')
        timer.start()
        timer.end()
        timer.record()
        assert os.path.exists(os.path.join(timer.home, timer.timer_dir, timer.record_file))
