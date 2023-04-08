"""
Given an array A of N elements representing the monsters and a array B o f Q elements representing the heroes.
the i-th type of monster is represented by A[i][0], A[i][1] and A[i][2] which means a monster of i-th type is present at each integer co-ordinate from A[i][0] to A[i][1] and having a strength of A[i][2]. 

The i-th type of hero is represented by B[i][0] and B[i][1] which means a hero of strength B[i][1] will appear at the integer point B[i][0] aftre i seconds. When the i-th hero appears it will destroy each and every monster present at the B[i][0] and having a strength less than B[i][1].

For each i you have to determine the number of monsters left after the i-yh hero has completed their task.

"""

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        ans = [0] * m
        for i in range(m):
            ans[i] = n
        for i in range(m):
            for j in range(n):
                if A[j][0] <= B[i][0] <= A[j][1] and A[j][2] < B[i][1]:
                    ans[i] -= 1
        return ans
    
# Driver code
if __name__ == "__main__":
    A = [[1, 10, 5], [2, 5, 10]]
    B = [[1, 5], [2, 10]]
    print(Solution().solve(A, B))

# This code is contributed by Shreyanshi Arun.
