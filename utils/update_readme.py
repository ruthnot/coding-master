import os
from collections import OrderedDict

TAGS = ('Binary Search', 'Two Pointers')

class UpdateReadme(object):
    def __init__(self, tags=TAGS):
        self.total = 0
        self.tags = tags
        self.category = OrderedDict()
        for tag in tags:
            self.category[tag] = []

    def update(self):
        self.scan()

        with open('../README.md', 'w') as f:
            f.write('#Total: {}\n\n'.format(self.total))
            for tag, problems in self.category.items():
                line = '###{}\n\n'.format(tag)
                f.write(line)
                for problem in problems:
                    line = "[{}](problems/{})\n\n".format(problem, problem.replace(' ', '%20'))
                    f.write(line)
            f.close()

    def scan(self):
        path = "../problems/"
        problems = os.listdir(path)
        for problem in problems:
            self.total += 1
            with open(path+problem, 'r') as f:
                for line in f:
                    if 'Tags' in line:
                        main_tag = line.split(': ')[1].rstrip()
                        self.category[main_tag].append(problem)
                        break

if __name__=='__main__':
    x = UpdateReadme()
    x.update()
