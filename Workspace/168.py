class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        #Constructing Dictionary
        ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        while columnNumber > 26:
            tmp = columnNumber // 26
            res = ref[(columnNumber - (tmp*26))-1] + res
            columnNumber = tmp
        if columnNumber >= 0:
            res = ref[columnNumber-1] + res
        return res


## Main
sol = Solution()
print(sol.convertToTitle(52))
