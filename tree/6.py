import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0] * (n+1)
for i in range(n):
    position[inorder[i]] = i
    
def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart>inEnd) or (postStart>postEnd):
        return
    
    root = postorder[postEnd]
    print(root, end=' ')
    
    left = position[root] - inStart
    right = inEnd-position[root]
    
    preorder(inStart, inStart+left-1, postStart, postStart+left-1)
    preorder(inEnd-right+1, inEnd, postEnd-right, postEnd-1)
    

preorder(0, n-1, 0, n-1)
