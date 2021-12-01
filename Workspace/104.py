class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0

            if (not node.left) and (not node.right):
                return 1

            else:
                return 1 + max(dfs(node.left), dfs(node.right))
        return dfs(root)