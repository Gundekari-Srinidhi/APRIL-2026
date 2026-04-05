class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        def squares(n):

            if n == 0:
                return 0
            if n in memo:
                return memo[n]
            ans = float("inf")
            i = 1
            while i*i<=n:
                val = n - i*i 
                ans = min(ans, 1+squares(val))
                i+=1
            memo[n] = ans
            return ans
        return squares(n)
        