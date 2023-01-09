class TreeNode:
    def __init__(self, value):
        self.value = value
        self.ifEnd = False
        self.children = [None]*26

class Trie:
    def __init__(self):
        self.root = TreeNode("")

    def insert(self, word: str) -> None:
        curNode = self.root
        for char in word:
            charIndex = ord(char)-ord('a')
            if curNode.children[charIndex]==None:
                curNode.children[charIndex] = TreeNode(char)
            curNode = curNode.children[charIndex]
        curNode.ifEnd = True
        
    def search(self, word: str) -> bool:
        curNode = self.root
        for char in word:
            charIndex = ord(char)-ord('a')
            if curNode.children[charIndex]==None:
                return False
            curNode = curNode.children[charIndex]
        return curNode.ifEnd

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for char in prefix:
            charIndex = ord(char)-ord('a')
            if curNode.children[charIndex]==None:
                return False
            curNode = curNode.children[charIndex]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
