class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def leaders(self, A, N):
        ans = []
        a = A[::-1]
        max = -1
        for items in a:
            if items >= max:
                max = items
                ans.append(max)
        return ans[::-1]
