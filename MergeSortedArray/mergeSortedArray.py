class Solution:

    def merge(self, nums1, nums2, m, n) -> None:
        #Modify nums1 in place

        tempMerged = nums1[:m]+nums2

        index = 0
        while (len(tempMerged) != 0):
            tempMin = min(tempMerged)
            minIndex = tempMerged.index(tempMin)
            nums1[index] = tempMin
            tempMerged.pop(minIndex)
            index += 1



if __name__ == "__main__":

    nums2 = [1,3,6,7,9,11,16,18,19,24]
    n = len(nums2)
    m = 10
    nums1 = [5,6,9,12,54,67,89,90,91,92]
    for i in range(n):
        nums1.append(0)

    solution = Solution()

    solution.merge(nums1,nums2,m,n)

    print(nums1)