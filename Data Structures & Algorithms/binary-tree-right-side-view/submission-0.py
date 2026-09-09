# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = collections.deque([root])

        result = []

        while q:
            rightNode = None
            level_length = len(q)

            for i in range(level_length):
                node = q.popleft()
                
                if node:
                    rightNode = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightNode:
                result.append(rightNode.val)
        
        return result






            





