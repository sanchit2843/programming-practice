class Solution:

    # Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        # code here
        d1 = {}
        d2 = {}
        for i in a:
            if i in d1.keys():
                d1[i] += 1
            else:
                d1[i] = 1
        for i in b:
            if i in d2.keys():
                d2[i] += 1
            else:
                d2[i] = 1
        if d1 == d2:
            return 1
        return 0
