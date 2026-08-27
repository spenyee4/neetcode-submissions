# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        def DFS(node, depth):

            if not node:
                return 0
            
            
            
            return 1 + max(DFS(node.left,depth), DFS(node.right, depth))
            
            
            
            
        
        
        return DFS(root, 0)