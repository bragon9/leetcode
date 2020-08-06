class WordDictionary:
    
    class node:
        def __init__(self, val):
            self.val = val
            self.children = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        # Build trie.
        node = None
        start_char = word[0]
        if start_char in self.nodes:
            node = self.nodes[start_char]
        else:
            node = self.node(start_char)
            self.nodes[start_char] = node
        ptr = 1
        while ptr < len(word):
            char = word[ptr]
            if char not in node.children:
                node.children[char] = self.node(char)
            node = node.children[char]
            ptr += 1
        node.children['end'] = None

    def search(self, word: str, children=None) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            if 'end' in children:
                return True
            else:
                return False
        letter = word[0]
        if not(children):
            children = self.nodes
        # if current letter is a wildcard, check all letters.
        if letter == '.':
            for node in children:
                if node != 'end':
                    if self.search(word[1:], children[node].children):
                        return True
        # If actual letter, check children for this letter.
        else:
            if letter in children:
                if self.search(word[1:], children[letter].children):
                    return True
        return False
        
