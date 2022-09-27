class TrieNode:
    
    def __init__(self, value: str, is_end: bool):
        self.value = value
        self.is_end = is_end
        self.children = [None]*26
        
class Trie:

    def __init__(self):
        self.root = TrieNode("", False)

    def insert(self, word: str) -> None:
        curNode = self.root
        for i in range(len(word)):
            if curNode.children[ord(word[i])- ord('a')]==None:
                curNode.children[ord(word[i])- ord('a')] = TrieNode(word[i], False)
            curNode = curNode.children[ord(word[i])- ord('a')]
            if i == len(word)-1:
                curNode.is_end = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for i in range(len(word)):
            if curNode.children[ord(word[i]) - ord('a')]!=None:
                if i == len(word)-1 and curNode.children[ord(word[i]) - ord('a')].is_end==True:
                    return True
            else:
                return False
            curNode = curNode.children[ord(word[i]) - ord('a')]
        return False

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for i in range(len(prefix)):
            if curNode.children[ord(prefix[i]) - ord('a')]:
                if i == len(prefix)-1:
                    return True
            else:
                return False
            curNode = curNode.children[ord(prefix[i]) - ord('a')]
        return False
    

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
