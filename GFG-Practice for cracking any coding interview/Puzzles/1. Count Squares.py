class Solution:
    def countSquares(self, N):
        # code here
        number_of_sq = (N - 1) ** 0.5
        return int(number_of_sq)
