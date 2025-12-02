class WordDictionary:
    class TrieNode:
        def __init__(self): 
            self.children = {} # Dictionary to hold child characters
            self.is_end_of_word = False # Flag to mark the end of a word

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root  # Start at the root node
        for char in word:  # Go through each letter in the word
            if char not in node.children:
                node.children[char] = self.TrieNode()  # Create a node if it doesn't exist
            node = node.children[char]  # Move to the next node
        node.is_end_of_word = True  # Mark the end of the word


    def search(self, word: str) -> bool:
        def dfs(index, node):
            # If we reached the end of the word, return whether it's a full word
            if index == len(word):
                return node.is_end_of_word
            
            char = word[index]
    
            # If current char is '.', we must try ALL possible children
            if char == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
    
            # If it's a normal letter and not in children — word not found
            if char not in node.children:
                return False
    
            # Move to the next character
            return dfs(index + 1, node.children[char])
        
        # Start DFS from the root and 0 index
        return dfs(0, self.root)
    
            
    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)