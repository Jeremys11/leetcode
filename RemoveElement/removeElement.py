class Solution:
    def removeElement(self, nums, val) -> int:
        while val in nums:
            nums.remove(val)
        return(len(nums))
    

if __name__ == "__main__":

    nums1 = [5,6,4,4,4,6,34,5,6,4]
    val = 4

    solution = Solution()

    solution.removeElement(nums1,val)

    print(nums1)