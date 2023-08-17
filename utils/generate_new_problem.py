from os import path
from utils.leetcode_helper import LeetcodeHelper
from utils.update_readme import UpdateReadme
from datetime import date

INPUT = {
    "leet_name": "368. Largest Divisible Subset",
    "lint_name": "603 · Largest Divisible Subset",
    "tags": "DP"
}


class GenerateProblem(object):
    def __init__(self, overwrite=False):
        self.overwrite = overwrite
        self.input = INPUT
        self.leetcode = LeetcodeHelper()

    def input_parser(self):
        leet_id = self.input['leet_name'].split('.')[0]
        leet_name = self.input['leet_name']
        leet_name = leet_name.replace('- ', '')  # delete any preexisting dash (and following space)  3/22/2023
        leet_slug = '-'.join(leet_name.split(' ')[1:]).lower()
        lint_id = self.input['lint_name'].split('·')[0]
        self.input['leet_id'] = leet_id
        self.input['leet_slug'] = leet_slug
        self.input['lint_id'] = lint_id
        self.input['leet_url'] = 'https://leetcode.com/problems/{}/'.format(leet_slug)
        self.input['lint_url'] = 'https://lintcode.com/problem/{}'.format(lint_id)

    def run(self):
        # Parse user input
        self.input_parser()
        file_path = "../problems/{}.md".format(self.get_name(self.input['leet_name']))
        if path.exists(file_path) and not self.overwrite:
            print('Problem already existed!')
            return

        # Get question component and write
        question = self.get_question()
        solution_and_notes = self.get_solution_and_notes()
        header = self.get_header()
        with open(file_path, 'w') as f:
            f.write(header)
            f.write(question)
            f.write(solution_and_notes)
            f.close()
        print('New Problem Generated: {}'.format(file_path.split('/')[-1]))

        # Update README
        UpdateReadme().update()


    def get_name(self, leet_name):
        number = leet_name.split('.')[0]
        name = leet_name.split('.')[1]
        while len(number) < 4:
            number = '0' + number
        new_name = '.'.join([number, name])
        return new_name

    def get_header(self):
        difficulty = 'Difficulty: {}'.format(self.input['difficulty'])
        leet = '[LeetCode: {}]({})'.format(self.input['leet_name'], self.input['leet_url'])
        lint = '[LintCode: {}]({})'.format(self.input['lint_name'], self.input['lint_url'])
        result = f'{difficulty}\n\n' \
                 f'Tags: {self.input["tags"]}\n\n' \
                 f'Need Review: False\n\n' \
                 f'Date Added: {date.today()}\n\n' \
                 f'{leet}\n\n' \
                 f'{lint}\n\n'
        return result

    def get_question(self):
        raw = self.leetcode.get_question(self.input['leet_slug'])
        self.input['difficulty'] = raw['difficulty']
        raw = raw['description']
        res = '## Description \n\n'
        last_idx = 0
        for idx, char in enumerate(raw):
            if char == '\n':
                res += (raw[last_idx:idx] + '\n\n')
                last_idx = idx + 1
        return res

    def get_solution_and_notes(self):
        res = "## Solution \n ```python \n\n ``` \n## Notes"
        return res


if __name__=='__main__':
    GenerateProblem(overwrite=False).run()


