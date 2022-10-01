"""Simple project timer"""

import datetime
import os

import pandas as pd

from src.data import TimerData


class TimerDefines:
    """Timer data class"""
    DATE = None
    START = None
    STOP = None
    DURATION = None


class Timer:
    def __init__(self, activity=None, timer_dir='.timer_records', record_file='timer_records.csv',
                 delimiter='|', logging=True):
        self.logging = logging
        self.activity = activity
        self.timer_dir = timer_dir
        self.record_file = record_file
        self.defines = TimerDefines()
        self.data = TimerData(timer_dir=timer_dir, record_file=record_file, delimiter=delimiter)
        self.delimiter = delimiter
        self.home = os.path.expanduser('~')
        self.create_record_file()
        self.file_data = None
        self.data_frame_columns = ['date', 'activity', 'start', 'stop', 'duration']
        self.defines.DATE = datetime.datetime.now().strftime('%d/%m/%Y')

    def create_record_file(self):
        if not os.path.exists(os.path.join(self.home, self.timer_dir)):
            os.mkdir(os.path.join(self.home, self.timer_dir))
        if not os.path.exists(os.path.join(self.home, self.timer_dir, self.record_file)):
            with open(os.path.join(self.home, self.timer_dir, self.record_file), 'w') as f:
                f.write('')
            if self.logging:
                print(f'Timer record file "{self.record_file}" created')

    def start(self):
        self.defines.START = datetime.datetime.now()

    def end(self):
        self.defines.STOP = datetime.datetime.now()
        self.defines.DURATION = (self.defines.STOP - self.defines.START).seconds

    def record(self):
        self.file_data = self.data.read_record()
        new_entry = [
            self.defines.DATE,
            self.activity,
            self.defines.START,
            self.defines.STOP,
            self.defines.DURATION
        ]
        if not all(new_entry):
            raise ValueError(f'Missing data: {new_entry}')
        new_df = pd.DataFrame([new_entry], columns=self.data_frame_columns)
        if not isinstance(self.file_data, pd.DataFrame):
            self.file_data = new_df
        else:
            self.file_data = pd.concat([self.file_data, new_df], ignore_index=True)
        self._write_record()

    def _write_record(self):
        self.file_data.to_csv(
            os.path.join(self.home, self.timer_dir, self.record_file), index=False, sep=self.delimiter)

    def __str__(self):
        return f'Activity timer for {self.activity}'
