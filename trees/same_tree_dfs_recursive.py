# TC O(n) , SC O(h) -> Stack 

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        
        if ( not p and q ) or (not q and p):
            return False

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)    
        else:
            return False        
