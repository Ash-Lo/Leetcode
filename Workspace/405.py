class Solution:
    def toHex(self, num: int) -> str:

        #Preprocessisng
        ref_str = '0123456789abcdef'
        ref_dict = {}
        for i, s in enumerate(ref_str):
            ref_dict[i] = s

        ## Code
        hex = ""
        if num == 0:
            return "0"
        else:
            if num < 0:
                num += 2 ** 32
            while num:
                hex = ref_dict[num % 16] + hex
                num = num // 16
            return hex

## Main
sol = Solution()
print(sol.toHex(-1))