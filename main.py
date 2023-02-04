
import requests
import json

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"
    res = requests.get(url)
    x = res.text
    print(x)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
