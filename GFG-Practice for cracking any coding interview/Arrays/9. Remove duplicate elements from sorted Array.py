class Solution:
    def remove_duplicate(self, A, N):
        # code here
        i = 0
        while len(A) - 1 > i:
            if A[i + 1] == A[i]:
                A.pop(i + 1)
            else:
                i += 1

        return len(A)
