class Trie:
    class TrieNode:
        def __init__(self): 
            self.children = {} # Dictionary to hold child characters
            self.is_end_of_word = False # Flag to mark the end of a word

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        node = self.root  # Start at the root node
        for char in word:  # Go through each letter in the word
            if char not in node.children:
                node.children[char] = self.TrieNode()  # Create a node if it doesn't exist
            node = node.children[char]  # Move to the next node
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # If a character is missing, word is not there
            node = node.children[char]
        return node.is_end_of_word  # True only if word ends here

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False  # Missing letter means no word with this prefix
            node = node.children[char]
        return True  # If we get through the whole prefix, it exists!



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)