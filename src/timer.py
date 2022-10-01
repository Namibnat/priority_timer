"""Simple project timer"""

import datetime
import os

import pandas as pd


class TimerData:
    """Timer data class"""
    DATE = None
    START = None
    STOP = None
    DURATION = None


class Timer:
    def __init__(self, activity=None, timer_dir='.timer_records', record_file='timer_records.csv', delimiter='|'):
        self.activity = activity
        self.timer_dir = timer_dir
        self.record_file = record_file
        self.data = TimerData()
        self.delimiter = delimiter
        self.home = os.path.expanduser('~')
        self.create_record_file()
        self.file_data = None
        self.data_frame_columns = ['date', 'activity', 'start', 'stop', 'duration']
        self.data.DATE = datetime.datetime.now().strftime('%d/%m/%Y')

    def create_record_file(self):
        if not os.path.exists(os.path.join(self.home, self.timer_dir)):
            os.mkdir(os.path.join(self.home, self.timer_dir))
        if not os.path.exists(os.path.join(self.home, self.timer_dir, self.record_file)):
            with open(os.path.join(self.home, self.timer_dir, self.record_file), 'w') as f:
                f.write('')
            print('Timer record file created')
        else:
            print('Timer record file already exists')

    def start(self):
        self.data.START = datetime.datetime.now()

    def end(self):
        self.data.STOP = datetime.datetime.now()
        self.data.DURATION = self.data.STOP - self.data.START

    def record(self):
        self._read_record()
        new_entry = [
            self.data.DATE,
            self.activity,
            self.data.START,
            self.data.STOP,
            self.data.DURATION
        ]
        if not all(new_entry):
            raise ValueError('Missing data')
        if not isinstance(self.file_data, pd.DataFrame):
            self.file_data = pd.DataFrame([new_entry], columns=self.data_frame_columns)
        else:
            self.file_data = self.file_data.append(pd.DataFrame([new_entry], columns=self.data_frame_columns))
        self._write_record()

    def _read_record(self):
        try:
            self.file_data = pd.read_csv(
                os.path.join(self.home, self.timer_dir, self.record_file), delimiter=self.delimiter)
        except pd.errors.EmptyDataError:
            self.file_data = None

    def _write_record(self):
        self.file_data.to_csv(
            os.path.join(self.home, self.timer_dir, self.record_file), index=False, sep=self.delimiter)

