"""
You are given an array A of N integers. You will have to pick 3 subarrays from the array I1,I2 and I3. The subarray I1 must be a prefix and I3 must be a suffix. The minimum length of each of these subarrays must be 1. An element of the array cannot be present in more than 1 of these subarrays.

Find the maximum sum of all the elements in each of these three subarrays. Since the sum can be large, return the positive remainder after dividing the sum with 10 3 + 7.

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        mod = 10**3 + 7
        pre = [0] * n
        suf = [0] * n
        pre[0] = A[0]
        suf[n-1] = A[n-1]
        for i in range(1, n):
            pre[i] = pre[i-1] + A[i]
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1] + A[i]
        ans = 0
        for i in range(1, n-1):
            ans = max(ans, pre[i-1] * suf[i+1])
        return ans % mod
    
# Driver code
if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    print(Solution().solve(A))

# This code is contributed by Shreyanshi Arun.

