from collections import deque
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return root
        
        q = deque([ root ])

        while q:
            curr = q.popleft()
            if curr is None:
                continue
            curr.left, curr.right = curr.right, curr.left 
            q.append(curr.left)
            q.append(curr.right)
        
        return root
