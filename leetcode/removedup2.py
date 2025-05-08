class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # p1 = 0
        # p2 = 1
        # nums1 = []
        # nums1.append(nums[0])
        # while p2 < len(nums):
        #     if nums[p1] == nums[p2] and p2 - p1 < 2:
        #         nums1.append(nums[p1])
        #         p2 += 1
        #     elif nums[p1] != nums[p2]:
        #         p1 = p2
        #         nums1.append(nums[p1])
        #         p2 += 1
        #     else:
        #         p2 += 1
        # nums = nums1
        # return len(nums), nums
        k = 2
        if len(nums) < 2:
            return len(nums)
        for x in nums:
            if x != nums[k - 2]:
                nums[k] = x
                k += 1
        return k


    
    
sol = Solution()
print(sol.removeDuplicates([1,1,2]))