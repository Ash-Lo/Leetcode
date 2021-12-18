class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        i, j = 0, 0
        while (i < m) and (j < n):
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1

        if (i < m):
            for k in range(i, m): temp.append(nums1[k])

        elif(j < n):
            for k in range(j, n): temp.append(nums2[k])

        nums1 = temp
        return nums1

## Main
sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))