class Solution:
    def reverseBits(self, n: int) -> str:
        res = []
        string = ""

        def int_to_bin(n, string):
            if n:
                string = str(n % 2) + string
                int_to_bin(n//2, string)
            return string
        int_to_bin(n, string)
        return string


## Main
sol = Solution()
print(sol.reverseBits(6))

