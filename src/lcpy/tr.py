"""
Trie
https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58834/AC-Python-Solution/205713
"""
from typing import List

class Node:
    def __init__(self, c):
        self.c = c
        self.left = None
        self.right = None
        self.mid = None
        self.val = None

class Trie:
    """
    Ternary search tries.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None        

    def put(self, node, key, val, d):
        c = key[d]
        if not node:
            node = Node(c)
        if c < node.c:
            node.left = self.put(node.left, key, val, d)
        elif c > node.c:
            node.right = self.put(node.right, key, val, d)
        elif d < len(key) - 1:
            node.mid = self.put(node.mid, key, val ,d+1)
        else:
            node.val = val
        return node

    def insert(self, word, val = 1) -> None:
        """
        Inserts a word into the trie.
        """
        key = word
        # val = 1
        self.root = self.put(self.root, key, val, d=0)

    def _get(self, node, key, d):
        if not node:
            return None
        c = key[d]
        if c < node.c:
            return self._get(node.left, key, d)
        elif c > node.c:
            return self._get(node.right, key, d)
        elif d < len(key) - 1:
            return self._get(node.mid, key, d+1)
        else:
            return node

    def get(self, key):
        node = self._get(self.root, key, 0)
        if node:
            return node.val
        return None

    def contains(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        key = word
        node = self._get(self.root, key, 0)
        if not node:
            return False
        # print(node.val)
        if not node.val:
            return False
        else:
            return True

    def keys(self):
        """
        return list of string keys
        """
        result = []
        self.collect(self.root, "", result)
        return result

    def collect(self, node, prefix, result):
        if not node:
            return
        self.collect(node.left, prefix, result)
        if node.val != None:
            result.append(prefix + node.c)
        self.collect(node.mid, prefix + node.c, result)
        # prefix = prefix[:-1]
        self.collect(node.right, prefix, result)

    def startsWith(self, prefix: str) -> List[str]:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        if prefix is "", return all keys
        """
        if not prefix:
            return self.keys()        
        result = []
        node = self._get(self.root, prefix, 0)
        if not node:
            return result
        if node.val != None:
            result.append(prefix)
        self.collect(node.mid, prefix, result)
        return result


from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()

    def insert(self, word):
        # write your code here
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        # write your code here
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        # write your code here
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True


from collections import defaultdict
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word = False

class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        # write your code here
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True
    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        curr = self.root
        self.res = False
        self.dfs(curr, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.is_word:
                self.res = True
        elif word[0] == '.':
            for child in node.children.values():
                self.dfs(child, word[1:])
        else:
            node = node.children.get(word[0])
            if node is None:
                return
            self.dfs(node, word[1:])