# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root) :

        ans_list = []
        def dfs(node):
            if not node:
                return None

            elif not node.left and not node.right:
                ans_list.append(node.val)
                return None

            if node.left:
                ans_list.append(dfs(node.left))
            if node.right:
                ans_list.append(dfs(node.right))
            ans_list.append(node.val)
            return None

        dfs(root)
        ans = []
        for val in ans_list:
            if val != None:
                ans.append(val)
        return ans