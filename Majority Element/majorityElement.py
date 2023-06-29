class Solution:
    def majorityElement(self, nums) -> int:

        counts = {}
        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1

        max_key = max(counts, key=counts.get)
        return max_key
    


nums = [1,1,2,2,24,45,5,6,6,6]

solution = Solution()
majorityElement = solution.majorityElement(nums=nums)

print(majorityElement)