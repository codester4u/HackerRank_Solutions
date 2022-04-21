

def levelOrder(self,root):
    #Write your code here
    if root is None:
        return 
        
    qu = []
    qu.append(root)
    while len(qu) !=0:
        p = qu.pop(0)
        print(p.data, end=' ')
        if p.left is not None:
            qu.append(p.left)
        if p.right is not None:
            qu.append(p.right)

