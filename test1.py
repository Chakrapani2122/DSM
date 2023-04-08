"""
There are A cities conected by A-1 bi-directional roads such that all the cities are connected.
Roads are given by array 2D array B where i-th road connects B[i][0] city to B[i][1].
You go on C trips wheere on the i-th trip you travel from C[i][0] city to C[i][1] city. All the trips are independent of each other.
You have to pay a tax on D[i] on entering or leaving the i-th city. if you pay the tax while entering then you dont nee to pay at the time of leaving.

You can choose some on non-adjacent cities and make their tax half.

What can be the minimum sum of taxes you pay for all the C trips? Since the anser can be large, return the remainder afer dividing it by 10 3 + 7

"""

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : list of list of integers
    # @param D : list of integers
    # @return an integer
    def solve(self, A, B, C, D):
        mod = 10**3 + 7
        n = len(C)
        m = len(D)
        adj = [[] for i in range(m)]
        for i in range(n):
            adj[C[i][0]-1].append(C[i][1]-1)
            adj[C[i][1]-1].append(C[i][0]-1)
        dp = [0] * m
        for i in range(m):
            dp[i] = D[i]
        for i in range(m):
            for j in adj[i]:
                dp[i] = min(dp[i], dp[j])
        return sum(dp) % mod
    
# Driver code
if __name__ == "__main__":
    A = 4
    B = [[1, 2], [2, 3], [3, 4]]
    C = [[1, 2], [2, 3], [3, 4]]
    D = [1, 2, 3, 4]
    print(Solution().solve(A, B, C, D))

# This code is contributed by Shreyanshi Arun.

"""
You are given an array A of N integers. You will have to pick 3 subarrays from the array I1,I2 and I3. The subarray I1 must be a prefix and I3 must be a suffix. The minimum length of each of these subarrays must be 1. An element of the array cannot be present in more than 1 of these subarrays.

Find the maximum sum of all the elements in each of these three subarrays. Since the sum can be large, return the positive remainder after dividing the sum with 10 3 + 7.

"""
