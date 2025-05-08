class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p1 = 0
        p2 = len(nums) - 1
        k = 0
        while p1 != p2:
            if nums[p1] == val:
                k += 1
                nums[p1] = nums[p2]
                p2 -= 1
            else:
                p1 += 1
        nums = nums[:len(nums) - k]
        return len(nums)

# Test the function 
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums) 