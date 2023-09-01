class Solution:
    def mySqrt(self, x: int) -> int:
        prev = 0
        if (x == 0):
            return 0
        if (x == 1):
            return 1
        for i in range(x):
            if i*i > x:
                return(prev)
            prev = i
        return prev

x = 0

solution = Solution()
sqareRoot = solution.mySqrt(x=x)

print(sqareRoot)