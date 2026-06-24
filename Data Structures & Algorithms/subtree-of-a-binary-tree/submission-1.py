# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(node,subRoot):
            if not node and not subRoot:
                return True
            if not node or not subRoot:
                return False
            if node.val != subRoot.val:
                return False
            return (issame(node.left,subRoot.left) and issame(node.right,subRoot.right))
        if not root:
            return False
        if issame(root,subRoot):
            return True
        else:
            return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
        