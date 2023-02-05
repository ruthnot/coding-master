import requests
import json

INPUT = {
    'leetcode_url': "https://leetcode.com/problems/peak-index-in-a-mountain-array/",
    'lintcode_url': ""
}


# class LeetcodeHelper(object):
#     def __init__(self):
#         pass
#
#     def id2name(self):
#         url = 'https://leetcode.com/problemset/all/'
#         res = requests.get(url)
#
#         print(res.text)

class GenerateProblem(object):
    def __init__(self):
        self.input = INPUT

    def run(self):
        url = self.input['leetcode_url']
        res = requests.get(url).text
        description_start_idx = res.index('\"description\" content=\"')
        print(res[832:])



if __name__=='__main__':
    GenerateProblem().run()


