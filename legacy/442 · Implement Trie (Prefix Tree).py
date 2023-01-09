"""Implement a Trie with insert, search, and startsWith methods.

You may assume that all inputs are consist of lowercase letters a-z.

Example
Example 1:

Input:
  insert("lintcode")
  search("lint")
  startsWith("lint")
Output:
  false
  true
Example 2:

Input:
  insert("lintcode")
  search("code")
  startsWith("lint")
  startsWith("linterror")
  insert("linterror")
  search("lintcode“)
  startsWith("linterror")
Output:
  false
  true
  false
  true
  true"""



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        # do initialization if necessary
        self.root = TrieNode()

    def insert(self, word):
        # write your code here
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        # write your code here
        node = self.root
        last_node = None
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
            last_node = node
        return last_node.is_word

    def startsWith(self, prefix):
        # write your code here
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
