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
        """Create the record file"""
        if not os.path.exists(os.path.join(self.home, self.timer_dir)):
            os.mkdir(os.path.join(self.home, self.timer_dir))
        if not os.path.exists(os.path.join(self.home, self.timer_dir, self.record_file)):
            with open(os.path.join(self.home, self.timer_dir, self.record_file), 'w') as f:
                f.write('')
            if self.logging:
                print(f'Timer record file "{self.record_file}" created')

    def start(self):
        """Start the timer"""
        self.defines.START = datetime.datetime.now()

    def end(self):
        """End the timer and calculate the duration"""
        self.defines.STOP = datetime.datetime.now()
        self.defines.DURATION = (self.defines.STOP - self.defines.START).seconds

    def new_entry_to_data_frame(self):
        """Return a new entry as data frame"""
        new_entry = [
            self.defines.DATE,
            self.activity,
            self.defines.START,
            self.defines.STOP,
            self.defines.DURATION
        ]
        if not all(new_entry):
            raise ValueError(f'Missing data: {new_entry}')
        return pd.DataFrame([new_entry], columns=self.data_frame_columns)

    def record(self):
        """Record the activity"""
        self.file_data = self.data.read_record()
        new_df = self.new_entry_to_data_frame()
        if not isinstance(self.file_data, pd.DataFrame):
            self.file_data = new_df
        else:
            self.file_data = pd.concat([self.file_data, new_df], ignore_index=True)
        self._write_record()

    def _write_record(self):
        """Write the record file"""
        self.file_data.to_csv(
            os.path.join(self.home, self.timer_dir, self.record_file), index=False, sep=self.delimiter)

    def __repr__(self):
        return f'Activity timer for {self.activity}'
