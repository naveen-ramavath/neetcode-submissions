# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        ans=[]
        ans1=set()
        stack=[]
        cur=root
        while cur or stack:
            while cur:  
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            ans.append(cur.val)
            ans1.add(cur.val)
            cur=cur.right
        if len(ans1)==len(ans) and ans==sorted(ans):   
            return True
        else:
            return False