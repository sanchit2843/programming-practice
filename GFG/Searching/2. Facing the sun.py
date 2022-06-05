class Solution:
    def countBuildings(self, h, n):
        # code here
        max_element = h[0]
        count = 1
        for i in range(1, n):
            if h[i] > max_element:
                count += 1
                max_element = h[i]
        return count
