class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        def dict(string):
            dict = {}
            for s in string:
                if s not in dict.keys():
                    dict[s] = 0
                dict[s] += 1
            return dict

        dict1 = dict(s)
        dict2 = dict(t)
        l1 = list(dict1.values())
        l2 = list(dict2.values())
        l1.sort()
        l2.sort()
        #print(l1,l2)
        if dict1.keys() == dict2.keys() and l1 == l2:
            return True
        else:
            return False

## Main
sol = Solution()
print(sol.isAnagram("aacc", "ccac"))