# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q=deque([root])
        while q:
            a=q.popleft()
            a.left,a.right=a.right,a.left
            if a.right:
                q.append(a.right)
            if a.left:
                q.append(a.left)
        return root
