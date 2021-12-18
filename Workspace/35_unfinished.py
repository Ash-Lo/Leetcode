class Solution:
    def searchInsert(self, nums, target: int) -> int:

        if target < nums[0]:
            return 0

        elif target > nums[-1]:
            return len(nums)

        else:
            l = 0
            r = len(nums) - 1
            #mid = (l + r) // 2

            while l < r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid

                elif nums[mid] > target:
                    r = mid

                elif nums[mid] < target:
                    l = mid + 1


## Main
sol = Solution()
nums = [1, 3, 5, 6]
target = 2
print(sol.searchInsert(nums,target))