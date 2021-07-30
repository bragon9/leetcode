class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = {}


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = {}
        self.dummy = Node()

    def insert(self, key: str, val: int) -> None:
        old_val = self.words.get(key, 0)
        self.words[key] = val
        diff = val - old_val
        node = self.dummy
        for letter in key:
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter]
            node.val += diff
        node.children['VALUE'] = diff

    def sum(self, prefix: str) -> int:
        node = self.dummy
        for letter in prefix:
            try:
                node = node.children[letter]
            except:
                return 0
        return node.val
