from os import path
from utils.leetcode_helper import LeetcodeHelper

INPUT = {
    "leet_name": "33. Search in Rotated Sorted Array",
    "lint_name": "62 · Search in Rotated Sorted Array"
}


class GenerateProblem(object):
    def __init__(self):
        self.input = INPUT
        self.leetcode = LeetcodeHelper()

    def input_parser(self):
        leet_id = self.input['leet_name'].split('.')[0]
        leet_slug = '-'.join(self.input['leet_name'].split(' ')[1:]).lower()
        lint_id = self.input['lint_name'].split('·')[0]
        self.input['leet_id'] = leet_id
        self.input['leet_slug'] = leet_slug
        self.input['lint_id'] = lint_id
        self.input['leet_url'] = 'https://leetcode.com/problems/{}/'.format(leet_slug)
        self.input['lint_url'] = 'https://lintcode.com/problem/{}'.format(lint_id)

    def run(self):
        self.input_parser()
        file_path = "../problems/{}.md".format(self.input['leet_name'])
        if path.exists(file_path):
            print('Problem already existed!')
            return

        question = self.get_question()
        solution_and_notes = self.get_solution_and_notes()
        header = self.get_header()
        with open(file_path, 'w') as f:
            f.write(header)
            f.write(question)
            f.write(solution_and_notes)
            f.close()

    def get_header(self):
        difficulty = 'Difficulty: {}'.format(self.input['difficulty'])
        leet = '[LeetCode: {}]({})'.format(self.input['leet_name'], self.input['leet_url'])
        lint = '[LintCode: {}]({})'.format(self.input['lint_name'], self.input['lint_url'])
        result = '{}\n\n{}\n\n{}\n\n'.format(difficulty, leet, lint)
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
    GenerateProblem().run()


