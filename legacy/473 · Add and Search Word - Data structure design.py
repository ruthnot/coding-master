"""
Description
Design a data structure that supports the following two operations: addWord(word) and search(word)

Addword (word) adds a word to the data structure.search(word) can search a literal word or a regular expression string containing only letters a-z or ..

A . means it can represent any one letter.

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


You may assume that all words are consist of lowercase letters a-z.

Example
Example 1:

Input:
  addWord("a")
  search(".")
Output:
  true
Example 2:

Input:
  addWord("bad")
  addWord("dad")
  addWord("mad")
  search("pad")
  search("bad")
  search(".ad")
  search("b..")
Output:
  false
  true
  true
  true
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        if word is None:
            return False
        return self.dfs(self.root, word, 0)

    def dfs(self, node, word, index):
        if node is None:
            return False

        if index >= len(word):
            return node.is_word

        char = word[index]
        if char != '.':
            return self.dfs(node.children.get(char), word, index + 1)

        for child in node.children:
            if self.dfs(node.children[child], word, index + 1):
                return True

        return False