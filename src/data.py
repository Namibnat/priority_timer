"""Working with timer data"""

import collections
import os

import pandas as pd

Activities = collections.namedtuple('Activities', ['date', 'activity', 'start', 'stop', 'duration'])


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
        """Read the record file"""
        try:
            self.file_data = pd.read_csv(
                os.path.join(self.home, self.timer_dir, self.record_file), delimiter=self.delimiter)
        except pd.errors.EmptyDataError:
            self.file_data = None
        return self.file_data

    def activities_to_namedtuple(self):
        """Return a list of activities as named tuple"""
        self.read_record()
        activities = []
        for index, row in self.file_data.iterrows():
            activities.append(Activities(
                date=row['date'],
                activity=row['activity'],
                start=row['start'],
                stop=row['stop'],
                duration=row['duration']
            ))
        return activities

    def sum_duration(self):
        """Return the sum of all durations"""
        self.read_record()
        return self.file_data['duration'].sum()

    def max_duration(self):
        """Return the activity with the longest duration"""
        activity_with_max_duration = None
        activities = self.activities_to_namedtuple()
        max_duration = 0
        for activity in activities:
            if activity.duration > max_duration:
                max_duration = activity.duration
                activity_with_max_duration = activity
        return activity_with_max_duration

    def __getitem__(self, position):
        """Return the activity at the given position"""
        activities = self.activities_to_namedtuple()
        return activities[position]

    def __repr__(self):
        return f'Data from {self.record_file}'

    def __len__(self):
        self.read_record()
        return self.file_data[self.file_data.columns[0]].count()
