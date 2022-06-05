class Solution:
    # Function to count the number of possible triangles.
    def findNumberOfTriangles(self, arr, n):
        # code here
        arr.sort()
        total_sum = 0
        for i in range(n):
            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n and arr[k] < arr[i] + arr[j]:
                    k += 1
                total_sum += k - j - 1
        return total_sum
