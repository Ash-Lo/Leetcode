class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        val = 0
        for i in range(len(columnTitle)):
            val += (ord(columnTitle[i]) - 64) * pow(26, len(columnTitle)-1 -i)

        return val


## Main
sol = Solution()
columnTitle = "ZZ"
print(sol.titleToNumber(columnTitle))