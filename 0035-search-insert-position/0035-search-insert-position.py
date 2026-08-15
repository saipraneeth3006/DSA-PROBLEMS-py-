class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                x=nums.index(target)
                return x
            elif nums[i]>target:
                return i
            elif max(nums)<target:
                return len(nums)
                
                