class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node_dict = {}  

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        start_letter = word[0]
        if start_letter in self.node_dict:
            node = self.node_dict[start_letter]
        else:
            new_node = Node(start_letter)
            self.node_dict[start_letter] = new_node
            node = new_node
        for letter in word[1:]:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = Node(letter)
                node.add_child(new_node)
                node = new_node
        if 'end' not in node.children:
            end_node = Node('end')
            node.add_child(end_node)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        start_letter = word[0]
        if start_letter in self.node_dict:
            node = self.node_dict[start_letter]
            for letter in word[1:]:
                if letter not in node.children:
                    return False
                node = node.children[letter]
            if 'end' in node.children:
                return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        start_letter = prefix[0]
        if start_letter in self.node_dict:
            node = self.node_dict[start_letter]
            for letter in prefix[1:]:
                if letter not in node.children:
                    return False
                node = node.children[letter]
            return True
        return False

class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
    
    def add_child(self, node):
        self.children[node.value] = node
