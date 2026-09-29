class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return root
        
        st = [ root ]

        while st:
            curr = st.pop()
            if curr is None:
                continue
            curr.left, curr.right = curr.right, curr.left 
            st.append(curr.left)
            st.append(curr.right)
        
        return root
