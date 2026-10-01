class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        current = 0

        while queue:
            currentlen = len(queue)
            current += 1
            for _ in range(currentlen):
                newelement = queue.popleft()
                if newelement.left:
                    queue.append(newelement.left)
                if newelement.right:
                    queue.append(newelement.right)
            
        return current
