import requests
from bs4 import BeautifulSoup as bs


class LeetcodeHelper(object):
    def __init__(self):
        pass

    def get_question(self, titleSlug):
        res = dict()
        data = {"operationName": "questionData", "variables": {"titleSlug": titleSlug},
                "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}
        r = requests.post('https://leetcode.com/graphql', json=data).json()
        question = r['data']['question']

        res['title'] = question['title']
        res['id'] = question['questionFrontendId']
        soup = bs(question['content'], 'lxml')
        res['description'] = soup.get_text()
        res['difficulty'] = question['difficulty']
        return res


if __name__=='__main__':
    LeetcodeHelper().get_question("zigzag-conversion")