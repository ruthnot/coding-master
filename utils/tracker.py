import datetime
import matplotlib.pyplot as plt

PROBLEM_REQ = 3

class Tracker(object):
    def __init__(self):
        self.x_axis = []
        self.y_axis = []

    def run(self):
        start = datetime.date(2023, 1, 1)
        for day in range(365):
            date = start + datetime.timedelta(day)
            if date.weekday() == 0:  # Monday
                self.x_axis.append(f'{date.month}-{date.day}')

        self.y_axis.append(PROBLEM_REQ)
        for i in range(1, len(self.x_axis)):
            self.y_axis.append(self.y_axis[i-1] + PROBLEM_REQ)
        self.plot()

    def plot(self):
        fig = plt.figure()
        plt.plot(self.x_axis, self.y_axis, 'r')
        plt.xticks(rotation=45)
        plt.show()







if __name__=='__main__':
    Tracker().run()