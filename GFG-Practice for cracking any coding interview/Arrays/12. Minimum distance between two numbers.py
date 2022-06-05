class Solution:
    def minDist(self, arr, n, x, y):
        x_index = -1
        y_index = -1
        min_distance = 10 ** 5
        for i in range(n):
            if arr[i] == x:
                x_index = i
            if arr[i] == y:
                y_index = i
            if x_index != -1 and y_index != -1:
                curr_distance = abs(y_index - x_index)
                min_distance = min(min_distance, curr_distance)
        if x_index == -1 or y_index == -1:
            return -1
        return min_distance
