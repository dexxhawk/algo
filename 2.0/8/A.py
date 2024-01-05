from sys import stdin

class Node:
    def __init__(self, key: int, flag: bool = False):
        self.left = None
        self.right = None
        self.key = key
        self.flag = flag

class Tree:
    def __init__(self):
        self.root = None
    
    def _add(self, node: Node, n: int) -> Node:
        if not node:
            return Node(n)
        if n == node.key:
            self.flag = True
            return node
        elif n < node.key:
            node.left = self._add(node.left, n)
        else:
            node.right = self._add(node.right, n)
        return node
    
    def _search(self, node: Node, n: int) -> None:
        if not node:
            return
        if n == node.key:
            self.flag = True
            return
        elif n < node.key:
            self._search(node.left, n)
        else:
            self._search(node.right, n)
        return
    
    def tostring(self, node: Node, res: str, lvl: int) -> str:
        if node.left:
            res = self.tostring(node.left, res, lvl + 1) 
            res += "\n"

        res += lvl * "."
        res += str(node.key)

        if node.right:
            res += "\n"
            res = self.tostring(node.right, res, lvl + 1)

        return res
    
    
    def add(self, n: int) -> str:
        self.flag = False
        self.root = self._add(self.root, n)
        return "ALREADY" if self.flag else "DONE"
    
    def search(self, n: int) -> str:
        self.flag = False
        self._search(self.root, n)
        return "YES" if self.flag else "NO"
    
    def __str__(self):
        ans = ""
        return self.tostring(self.root, ans, 0)




tree = Tree()
for line in stdin:
    line = line.strip().rstrip().split()

    if line[0] == "PRINTTREE":
        print(tree)
    elif line[0] == "ADD":
        print(tree.add(int(line[1])))
    elif line[0] == "SEARCH":
        print(tree.search(int(line[1])))
        