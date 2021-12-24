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



class Constructor_eg:
    def __init__(self):
        self.length = 5
        self.breadth = 10

    def overwrite(self, val1, val2):
        self.length = val1
        self.breadth = val2

    def get_val(self):
        return self.length, self.breadth
## Main
#sol = Solution()
#print(sol.toHex(-1))

example = Constructor_eg()
print(example.length, example.breadth)
example.overwrite(100,100)
print(example.length, example.breadth)


