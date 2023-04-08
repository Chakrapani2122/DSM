"""
You have A natural numbers  from 1 to A, each occuring exactly once. Now, you choose any of the A (each number being equally likely) numbers and do the followingprocedures.
1. Initialze a variable step = 0
2. let X be the current nuber you have
3. Randomly choose any divisior of X ( each divisior being equally likely) Let it be Y, now replace X by X/Y. Also, increment step by 1
4. If X is not equal to 1, repeat from step 2.

Let expected value of step be represented in the form of a irreducible fraction x/y. Return xy -1 mod(10 9 + 7) where y -1 is the modulo multiplicative inverse of y modulo(10 9 + 7).


"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return (A - 1) % 1000000007
    

# Driver code
if __name__ == "__main__":
    A = 10
    print(Solution().solve(A))

# This code is contributed by Shreyanshi Arun.



