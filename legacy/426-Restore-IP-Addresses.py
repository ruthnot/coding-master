class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        answers = []
        self.dfs(s, [], answers)
        return answers

    def dfs(self, s, answer, answers):
        if len(answer) == 4 and len(s) == 0:
            answers.append(".".join(answer))
            return
        if len(answer) == 4 or len(s) == 0:
            return
        for i in range(1, len(s) + 1):
            substr = s[:i]
            if int(substr) > 255:
                break
            if len(substr) >= 2 and substr[0] == "0":
                break
            answer.append(substr)
            self.dfs(s[i:], answer, answers)
            answer.pop()

class Solution2:  # (less elegant)
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        results = []
        self.dfs(s, 0, [], results)
        return results

    def dfs(self, s, index, result, results):
        if index == len(s) and len(result) == 4:
            results.append(".".join(result))
            return
        if len(result) == 4 and index < len(s):
            return
        if index == len(s) and len(result) != 4:
            return

        result.append(s[index])
        self.dfs(s, index + 1, result, results)
        result.pop()

        if s[index] == '0':
            return

        if index + 1 < len(s):
            result.append(s[index:index+2])
            self.dfs(s, index + 2, result, results)
            result.pop()

        if index + 2 < len(s) and int(s[index:index+3]) <= 255:
            result.append(s[index:index+3])
            self.dfs(s, index + 3, result, results)
            result.pop()

if __name__ == '__main__':
    a = "1116512311"
    print(Solution().restoreIpAddresses(a))