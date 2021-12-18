class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        flag = n %2
        n = n // 2
        while n:
            if n % 2 == flag:
                return False

            flag = n % 2
            n = n //2
        return True

## Main
sol = Solution()
print(sol.hasAlternatingBits(7))