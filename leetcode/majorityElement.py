class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums_set = set(nums)
        nums_dict = {}
        for i in nums_set:
            nums_dict[i] = 0
        for i in nums:
            nums_dict[i] += 1
        
        return max(nums_dict, key = lambda x: nums_dict[x])
    
sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))