# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.is_end = True
    
    def search_with_curr(self, word: str, idx: int, curr: TrieNode) -> bool:
        if idx == len(word):
            return curr.is_end
        c = word[idx]
        if c == ".":
            for child_node in curr.children.values():
                if self.search_with_curr(word, idx+1, child_node):
                    return True # 여러 child_node 중 하나라도 True면 True를 리턴
            return False
        else:
            if c not in curr.children:
                return False
            return self.search_with_curr(word, idx+1, curr.children[c])
        
    def search(self, word: str) -> bool:
        return self.search_with_curr(word, 0, self.root)
