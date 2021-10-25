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