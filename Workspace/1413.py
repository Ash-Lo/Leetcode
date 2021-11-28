class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = nums[0]
        arr_min = nums[0]

        for i in range(1, len(nums)):
            cur_sum += nums[i]
            arr_min = min(arr_min, cur_sum)

        if arr_min < 0:
            return (-1)*(arr_min) + 1

        return 1


## main
sol = Solution()
nums = [-3,2,-3,4,2]
print(sol.minStartValue(nums))

print("7//2 = " + str(7//2))