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
        #print(dict1, dict2)
        # l1 = list(dict1.values())
        # l2 = list(dict2.values())
        # l1.sort()
        # l2.sort()
        flag = 0
        for key in dict1.keys():
            if dict1[key] != dict2[key]:
                flag = 1
                break
            else: continue
        #print(l1,l2)
        if flag:
            return False
        return True

## Main
sol = Solution()
print(sol.isAnagram("", ""))