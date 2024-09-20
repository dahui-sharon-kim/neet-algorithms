class Node:
    def __init__(self):
        self.children = {}
        self.eow = False


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.eow = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            cur = node
            for i in range(index, len(word)):
                if word[i] == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                if word[i] not in cur.children:
                    return False

                cur = cur.children[word[i]]
            return cur.eow

        return dfs(0, self.root)
