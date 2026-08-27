# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def DFS(node):
            if node is None:
                return
            

            tempLeft = node.left
            tempRight = node.right

            node.left = tempRight
            node.right = tempLeft

            DFS(node.left)
            DFS(node.right)

            return node
        
        return DFS(root)