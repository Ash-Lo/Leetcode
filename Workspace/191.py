class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n % 2
            n = n // 2
        return res

## Main
sol = Solution()
print(sol.hammingWeight(5))