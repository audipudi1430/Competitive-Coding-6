# Approach:
# - Use a Trie (Prefix Tree) to efficiently store and search messages character by character.
# - When searching a message, if it exists and 10 seconds have passed since last print, allow and update timestamp.
# - If the message is new or eligible (after 10 seconds), mark it and update timestamp.
#
# Time Complexity: O(L), where L is the length of the message (for both insert and search operations).
# Space Complexity: O(total characters), in the worst case one node per character of all messages.

class TrieNode:
    def __init__(self, timestamp=0):
        self.children = {}
        self.timestamp = timestamp
        self.is_end = False
        
class Logger:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, message, timestamp):
        node = self.root
        for ch in message:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        node.timestamp = timestamp

    def search(self, message, timestamp):
        node = self.root
        for char in message:
            if char not in node.children:
                self.insert(message, timestamp)
                return True
            node = node.children[char]
        if node.is_end:
            if node.timestamp + 10 <= timestamp:
                node.timestamp = timestamp
                return True
            else:
                return False
        else:
            node.is_end = True
            node.timestamp = timestamp
            return True
            
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        return self.search(message, timestamp)

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp, message)
