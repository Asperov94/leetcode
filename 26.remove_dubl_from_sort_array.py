class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in reversed(range(len(nums))):
            if  nums.count(nums[i]) >= 2:
                nums.pop(i)
        return len(nums)

