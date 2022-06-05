class Solution:
    def merge(self, S1, S2):
        # code here
        if len(S1) > len(S2):
            remaining_string = S1[len(S2) :]
            updated_string = []
            for i in range(len(S2) * 2):
                if i % 2 == 0:
                    updated_string.append(S1[i // 2])
                else:
                    updated_string.append(S2[i // 2])
            return "".join(updated_string) + remaining_string
        else:
            remaining_string = S2[len(S1) :]
            updated_string = []
            for i in range(len(S1) * 2):
                if i % 2 == 0:
                    updated_string.append(S1[i // 2])
                else:
                    updated_string.append(S2[i // 2])
            return "".join(updated_string) + remaining_string
