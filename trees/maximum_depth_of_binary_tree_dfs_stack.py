class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
       
        st = [ (root, 1) ]
        res = 0

        while st:
            node, depth = st.pop()
            res = max(res, depth)

            if node.left:
                st.append( ( node.left, depth + 1) )
            
            if node.right:
                st.append( (node.right, depth + 1) )
            
        return res
