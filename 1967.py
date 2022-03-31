import sys
input = sys.stdin.readline

tree = []

class node:
    def __init__(self):
        self.parent = (0,0)
        self.child = []
    
    def leftMax(self):
        if self.child == []:
            return 0
        
        return max(self.leftMax(tree[self.child[0][0]]), self.rightMax(tree[self.child[1][0]]))
    def rightMax(self):
        if self.child == []:
            return 0
        
        return max(self.leftMax(tree[self.child[0][1]]), self.rightMax(tree[self.child[1][1]]))
    
    def midMax(self):
        me = self.leftMax() + self.rightMax()
        if self.child == []:
            return me
        return max(me,self.midMax(tree[self.child[0][1]]),self.midMax(tree[self.child[1][1]]))


n = int(input())

tree =[node() for _ in range(n+1)]

for ____ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].child.append((b,c))
    tree[b].parent = (a,c)

print(tree[1].midMax())





