# TC O(n), SC O(n)
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        stack = [ (p, q) ]
        while stack:
            current = stack.pop()
            one, two = current[0], current[1]
            if (one is None and two is not None) or ( one is not None and two is None):
                return False
            if one is None and two is None:
                continue
            if one.val != two.val:
                return False    
            stack.append((one.left, two.left))
            stack.append((one.right, two.right))
        return True



