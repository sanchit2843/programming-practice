class Solution:
    def transform(self, s):
        # code here
        split = s.split(" ")
        split_ = []
        for i in split:
            i = list(i)
            i[0] = i[0].upper()

            split_.append("".join(i))
        return " ".join(split_)
