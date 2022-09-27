class TrieNode:
    
    def __init__(self, value: str):
        self.value = value
        self.is_end = False
        self.children = [None]*26
        
class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        curNode = self.root
        for i in range(len(word)):
            diff = ord(word[i])- ord('a')
            if curNode.children[diff]==None:
                curNode.children[diff] = TrieNode(word[i])
            curNode = curNode.children[diff]
            if i == len(word)-1:
                curNode.is_end = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for i in range(len(word)):
            diff = ord(word[i])- ord('a')
            if curNode.children[diff]!=None:
                if i == len(word)-1 and curNode.children[diff].is_end==True:
                    return True
            else:
                return False
            curNode = curNode.children[diff]
        return False

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for i in range(len(prefix)):
            diff = ord(prefix[i])- ord('a')
            if not curNode.children[diff]:
                return False
            curNode = curNode.children[diff]
        return True
    

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
