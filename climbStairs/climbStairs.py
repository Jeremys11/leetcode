class Solution:

    def __init__(self) -> None:
        self.climbRecords = {}

    def climbStairs(self, n: int) -> int:

        if n not in self.climbRecords:
            
            if n == 0:
                return 1
            sub1 = 0
            if n-1 >= 0:
                sub1 = self.climbStairs(n-1)
            sub2 = 0
            if n-2 >= 0:
                sub2 = self.climbStairs(n-2)

            self.climbRecords[n] = sub1+sub2

        return(self.climbRecords[n])
    

solution = Solution()

total = solution.climbStairs(45)
print(total)