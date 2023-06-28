class Solution:
    def removeDuplicates(self, nums) -> int:
        nums = list(set(nums))
        nums.sort()
        return (len(nums))
    
class Solution2:
    def removeDuplicates(self, nums) -> int:
        temp = list(set(nums))
        temp.sort()
        for i in range(len(temp)):
            nums[i] = temp[i]

        return(len(temp))

solution = Solution()

nums = [-1,0,0,0,0,3,3]
k = solution.removeDuplicates(nums=nums)
print(k)