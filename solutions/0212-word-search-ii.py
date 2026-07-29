class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.word=True
    def search(self, word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return cur.word
            


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie=Trie()
        for w in words:
            trie.insert(w)
        ROWS, COLS=len(board), len(board[0])
        res, visit=set(),set()

        def dfs(r,c, node, word):
            if (r<0 or c<0 or r == ROWS or c == COLS or (r,c) in visit or 
            board[r][c] not in node.children):
                return
            visit.add((r,c))
            node=node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            visit.remove((r,c))
        

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,trie.root,"")
        return list(res)
