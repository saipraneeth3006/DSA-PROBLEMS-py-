class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums and len(nums)>1:
            return 0
        if len(nums)==1:
            if nums[0]==1:
                return 0
            elif nums[0]==0:
                return 1
        nums.sort()
        if nums[len(nums)-1]==len(nums):
            for i in range(1,len(nums)):
                if nums[i]!=nums[i-1]+1:
                    return nums[i]-1
        else:
            return len(nums)
                