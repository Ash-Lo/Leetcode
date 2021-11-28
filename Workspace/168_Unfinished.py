class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        #Constructing Dictionary
        ref = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        while columnNumber >= 26:
            tmp = columnNumber // 26
            res = ref[(columnNumber - (tmp*26))] + res
            columnNumber = tmp
        if columnNumber:
            res = ref[columnNumber] + res
        return res


## Main
sol = Solution()
print(sol.convertToTitle(701))