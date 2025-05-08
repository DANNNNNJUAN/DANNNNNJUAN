class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1 = []
        for i in nums[(len(nums) - k)::]:
            nums1.append(i)
        for i in nums[:len(nums) - k]:
            nums1.append(i)
        nums = nums1[:]
        return nums
# Test the function
sol = Solution()
print(sol.rotate([1,2,3,4,5,6,7,8], 0))  # Output: [5,6,7,1,2,3,4]