import os
import datetime
import random

class ProblemManager(object):
    def __init__(self):
        path = "../problems/"
        self.problem_paths = [path + x for x in os.listdir(path)]

    def total_count(self):
        return len(self.problem_paths)

    def single_add_content(self, path, line_num, content):
        with open(path, 'r') as file:
            data = file.readlines()
        data[line_num] = content
        with open(path, 'w') as file:
            file.writelines(data)

    @staticmethod
    def pick_random_date(start, end):
        assert isinstance(start, datetime.date)
        assert isinstance(end, datetime.date)
        delta = (end - start).days
        random_day = random.randrange(1, delta+1)
        random_date = start + datetime.timedelta(random_day)
        return random_date

    @staticmethod
    def convert_date_format(date):
        if isinstance(date, str):
            year, month, day = [int(x) for x in date.split('-')]
            return datetime.date(year, month, day)
        if isinstance(date, datetime.date):
            return f'{date.year}-{date.month}-{date.day}'
        return None

if __name__=='__main__':
    c = ProblemManager()
    for p in c.problem_paths:
        with open(p) as f:
            for num, line in enumerate(f):
                if "Date Added" in line:
                    # print(line)
                    break
                if "Leetcode" in line:  # when date is not found
                    # Pick a random date
                    random_date = ProblemManager.pick_random_date(datetime.date(2023, 1, 1), datetime.date(2023, 3, 1))
                    # Add into the document to prevent pick again next time
                    print(p)
                    print(random_date)
                    # c.single_add_content(p, num-1, f'\nDate Added: {random_date}\n')