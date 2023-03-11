import datetime
import matplotlib.pyplot as plt

PROBLEM_REQ = 3

class Tracker(object):
    def __init__(self):
        self.x_num, self.x_week = [], []
        self.y_plan, self.y_actual = [], []

    def run(self):
        start = datetime.date(2023, 1, 1)
        for day in range(365):
            date = start + datetime.timedelta(day)
            year, week, weekday = datetime.datetime.isocalendar(date)
            if year == 2023 and weekday == 7:  # Sunday, the end of week
                self.x_week.append(f'{date.month}/{date.day}')
        self.y_plan.append(PROBLEM_REQ)
        for i in range(1, len(self.x_week)):
            self.y_plan.append(self.y_plan[i-1] + PROBLEM_REQ)
        self.plot()

    @staticmethod
    def date_to_num(date):
        _, week, weekday = datetime.datetime.isocalendar(date)
        num = week - 1 + round(weekday/7, 1) - 1
        return num

    def plot(self):
        # Plot Planed Trajectory
        plt.figure()
        plt.plot(self.x_week, self.y_plan, 'r')
        plt.xticks(rotation=45)

        # Plot Today's date
        x_num = Tracker.date_to_num(datetime.datetime.today())
        plt.axvline(x=x_num)

        plt.show()


if __name__=='__main__':
    t = Tracker()
    t.run()