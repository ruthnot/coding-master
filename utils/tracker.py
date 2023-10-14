import datetime
import matplotlib.pyplot as plt
import os
import random
from problem_manager import ProblemManager

PROBLEM_REQ = 3


class Tracker(object):
    def __init__(self):
        self.problems = ProblemManager()
        self.x_plan, self.x_actual = [], []
        self.y_plan, self.y_actual = [], []

    def run(self):
        start = datetime.date(2023, 1, 1)
        for day in range(365):
            date = start + datetime.timedelta(day)
            year, week, weekday = datetime.datetime.isocalendar(date)
            if year == 2023 and weekday == 7:  # Sunday, the end of week
                self.x_plan.append(f'{date.month}/{date.day}')
        self.y_plan.append(PROBLEM_REQ)
        for i in range(1, len(self.x_plan)):
            self.y_plan.append(self.y_plan[i-1] + PROBLEM_REQ)

        count_by_date = self.get_count_by_date()
        self.calc_history(count_by_date)

        self.plot_tracker()

    def calc_history(self, count_by_date):
        res = []
        for date, count in count_by_date.items():
            res.append([date, count])
        count = [x[1] for x in res]
        # Sort by date
        res.sort(key=lambda x: x[0])
        # Count Aggregation
        for i in range(1, len(res)):
            res[i][1] += res[i-1][1]
        # Return x, y
        x = [Tracker.date_to_num(x[0]) for x in res]
        y = [x[1] for x in res]
        self.x_actual, self.y_actual = x, y



    def get_count_by_date(self):
        count_by_date = dict()
        for problem in self.problems.problem_paths:
            with open(problem, 'r') as f:
                for line_num, line in enumerate(f):
                    if "Date Added" in line:
                        date = ProblemManager.convert_date_format(line.split(': ')[1])
                        count_by_date[date] = count_by_date.get(date, 0) + 1
                        break

        return count_by_date


    @staticmethod
    def date_to_num(date):
        _, week, weekday = datetime.datetime.isocalendar(date)
        num = week - 1 + round(weekday/7, 1) - 1
        return num

    def plot_tracker(self):
        # Plot Planed Trajectory
        plt.figure()
        plt.plot(self.x_plan, self.y_plan, 'r', label='Planned')
        plt.xticks(rotation=45)

        # Plot Today's date
        today_num = Tracker.date_to_num(datetime.datetime.today())
        plt.axvline(x=today_num, label='Today')

        # Plot Actual data
        plt.plot(self.x_actual, self.y_actual, label='Actual')

        # Calculate Plan vs Actual
        actual = max(self.y_actual)
        plan = int(today_num + 1) * PROBLEM_REQ
        plt.title(f'Planned: {plan} vs Actual: {actual} - Gap: {plan - actual}')


        plt.legend()
        plt.grid('On')
        plt.show()


if __name__=='__main__':
    t = Tracker()
    t.run()