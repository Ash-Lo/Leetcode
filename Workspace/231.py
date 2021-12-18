class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n < 0:
            return False
        elif n >= 1:
            return not(n & (n-1))

## Main
sol = Solution()
#print(sol.isPowerOfTwo(16))

print(4 & 3)