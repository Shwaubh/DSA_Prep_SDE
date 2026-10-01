from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        data = deque()
        data.append(root)
        output = []
        while data:
            currentlen = len(data)
            temp = [  ]
            while currentlen:       
                current = data.popleft()        
                temp.append(current.val)

                if current.left:
                    data.append(current.left)
                if current.right:
                    data.append(current.right)

                currentlen -= 1
            output.append(temp)
        
        return output
            
