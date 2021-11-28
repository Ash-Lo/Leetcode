class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        tot =  (len(nums)) * (len(nums) + 1 ) // 2
        sum = 0
        for i in nums:
            sum += i

        return tot - sum


## Main
sol = Solution()
print(sol.missingNumber([1, 0, 3]))