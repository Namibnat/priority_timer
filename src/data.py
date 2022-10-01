"""Working with timer data"""

import os

import pandas as pd


class TimerData:
    """Timer data class"""
    def __init__(self, timer_dir='.timer_records', record_file='timer_records.csv', delimiter='|'):
        self.timer_dir = timer_dir
        self.record_file = record_file
        self.delimiter = delimiter
        self.home = os.path.expanduser('~')
        self.file_data = None
        self.data_frame_columns = ['date', 'activity', 'start', 'stop', 'duration']

    def read_record(self):
        try:
            self.file_data = pd.read_csv(
                os.path.join(self.home, self.timer_dir, self.record_file), delimiter=self.delimiter)
        except pd.errors.EmptyDataError:
            self.file_data = None
