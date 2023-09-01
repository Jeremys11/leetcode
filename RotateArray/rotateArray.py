class Solution:

    def rotate(self, nums, k: int) -> None:

        holding = {}
        for i in range(len(nums)):
            if i in holding:
                newPosition = (i+k) % len(nums)
                holding[newPosition] = nums[newPosition]
                nums[newPosition] = holding[i]
                holding.pop(i)
            else:
                newPosition = (i+k) % len(nums)
                holding[newPosition] = nums[newPosition]
                nums[newPosition] = nums[i]

nums = [1,2,3,4,5]
k = 6

solution = Solution()
solution.rotate(nums=nums,k=k)
print(nums)