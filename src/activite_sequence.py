"""Run a day's worth of activities"""


from .timer import Timer


class Day:
    """Day class"""

    def __init__(self, activities: list):
        self.activities = activities
        self.timer = Timer()

    def prompt_start_activity(self, activity):
        """Prompt to start an activity"""
        print(f'Press enter to start {activity}')
        input()
        self.timer.start()

    def prompt_end_activity(self, activity):
        """Prompt to end an activity"""
        print(f'Press enter to end {activity}')
        input()
        self.timer.end()

    def day_runner(self):
        """Run a day's worth of activities"""
        for activity in self.activities:
            self.prompt_start_activity(activity)
            self.prompt_end_activity(activity)
        print('Day completed')


