class Solution:
    def nextGreaterElement(self, nums1, nums2):
        dp = [0] * len(nums2)
        dp[-1] = -1
