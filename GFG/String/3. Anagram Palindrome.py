class Solution:
    def isPossible(self, S):
        d = {}
        for l in S:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1
        count = 0
        for v in d.values():
            if v % 2 != 0:
                count += 1
            if count > 1:
                return False
        return True
        # code here
