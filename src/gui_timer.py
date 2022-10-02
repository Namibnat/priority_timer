"""Gui Timer

TODO: Flesh out this gui timer
"""

import os
import tkinter as tk

from src.timer import Timer
from src.data import TimerData


class GuiTimer:
    def __init__(self, timer_dir='.timer_records', record_file='timer_records.csv', delimiter='|'):
        self.timer_dir = timer_dir
        self.record_file = record_file
        self.delimiter = delimiter
        self.home = os.path.expanduser('~')
        self.data = TimerData(timer_dir=timer_dir, record_file=record_file, delimiter=delimiter)
        self.timer = Timer(timer_dir=timer_dir, record_file=record_file, delimiter=delimiter)
        self.root = tk.Tk()
        self.root.title('Timer')
        self.root.geometry('400x400')
        self.root.configure(bg='white')
        self.root.resizable(False, False)
        self.label = tk.Label(self.root, text='Timer', font=('Helvetica', 18, 'bold'), bg='white')
        self.label.pack(pady=10)
        self.activity_label = tk.Label(self.root, text='Activity', font=('Helvetica', 12), bg='white')
        self.activity_label.pack(pady=10)
        self.activity_entry = tk.Entry(self.root, font=('Helvetica', 12), width=20)
        self.activity_entry.pack(pady=10)
        self.start_button = tk.Button(self.root, text='Start', font=('Helvetica', 12), width=20, command=self.start)
        self.start_button.pack(pady=10)
        self.end_button = tk.Button(self.root, text='End', font=('Helvetica', 12), width=20, command=self.end)
        self.end_button.pack(pady=10)
        self.root.mainloop()

    def start(self):
        self.timer.activity = self.activity_entry.get()
        self.timer.start()
        self.start_button.config(state='disabled')
        self.end_button.config(state='normal')

    def end(self):
        self.timer.end()
        self.data.file_data = self.data.file_data.append(self.timer.new_entry_to_data_frame(), ignore_index=True)
        self.data.file_data.to_csv(
            os.path.join(self.home, self.timer_dir, self.record_file), index=False, sep=self.delimiter)
        self.start_button.config(state='normal')
        self.end_button.config(state='disabled')


if __name__ == '__main__':
    GuiTimer()
