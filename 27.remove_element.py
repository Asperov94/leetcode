class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=nums.count(val)
        while val in nums:
            nums.remove(val)
