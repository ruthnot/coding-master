import os
from collections import OrderedDict

TAGS = ('Binary Search', 'Two Pointers', 'BFS', 'Math', 'Untagged')

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
            f.write('# Total: {}\n\n'.format(self.total))
            for tag, problems in self.category.items():
                line = '### {}\n\n'.format(tag)
                f.write(line)
                for problem in problems:
                    frontend_name = problem.replace(' ', '%20')
                    line = f'[{problem}]({frontend_name})\n\n'
                    f.write(line)
            f.close()
        print('README Updated!')

    def scan(self):
        path = "../problems/"
        problems = os.listdir(path)
        for problem in problems:
            self.total += 1
            problem_name = problem.split('.md')[0]
            with open(path+problem, 'r') as f:
                for line in f:
                    if 'Tags' in line:
                        main_tag = line.split(': ')[1].rstrip()
                        if len(main_tag) == 0:  # not tagged yet:
                            self.category['Untagged'].append(problem_name)
                        elif main_tag not in self.category:
                            self.category[main_tag] = [problem_name]
                        else:
                            self.category[main_tag].append(problem_name)
                        break


if __name__=='__main__':
    x = UpdateReadme()
    x.update()
