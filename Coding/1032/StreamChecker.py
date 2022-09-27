class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [None] * 26
        self.is_end = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode("")
        self.positions = [self.root]
        for w in words:
            curNode = self.root
            for i in range(len(w)):
                c = w[i]
                diff = ord(c)-ord("a")
                if curNode.children[diff] == None:
                    curNode.children[diff] = TrieNode(c)
                curNode = curNode.children[diff]
                if i==len(w)-1: curNode.is_end = True

    def query(self, letter: str) -> bool:
        newPos = [self.root]
        ret = False
        for p in self.positions:
            diff = ord(letter) - ord("a")
            if p.children[diff]:
                newPos.append(p.children[diff])
                if p.children[diff].is_end:
                    ret = True
        self.positions = newPos
        return ret


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
