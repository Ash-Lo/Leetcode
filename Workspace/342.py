class Solution:
    def isPowerOfFour(self, n: int) -> bool:
            if n & n-1 == 0:
                return True
            return False

## Main
sol = Solution()
print(sol.isPowerOfFour(8))