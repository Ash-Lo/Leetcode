class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # if not s or not t:
        #     return False
        #
        # def freq_counter(s):
        #     dict = {}
        #     alph = set()
        #     for letter in s:
        #         if letter not in alph:
        #             dict[letter] = 1
        #             alph.add(letter)
        #         elif letter in alph:
        #             dict[letter] += 1
        #     return dict.values()
        #
        # if list(freq_counter(s)) == list(freq_counter(t)):
        #     return True
        # return False
        if not s or not t:
            return False

        def freq_counter(s):
            dict = {}
            alph = set()
            for letter in s:
                if letter not in alph:
                    dict[letter] = 1
                    alph.add(letter)
                elif letter in alph:
                    dict[letter] += 1
            return dict.values()

        if list(freq_counter(s)) == list(freq_counter(t)):
            return True
        return False


## Main
sol = Solution()
print(sol.isIsomorphic("paper", "title"))