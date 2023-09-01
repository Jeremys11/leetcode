class Solution:
    def removeDuplicates(self, nums) -> int:

        counts = {}
        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1

        for key in counts:
            print(counts[key])
            while counts[key] > 2:
                nums.remove(key)
                counts[key] -= 1
        
        return len(nums)
    
nums = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]

solution = Solution()
solution.removeDuplicates(nums=nums)

print(nums)