class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        sum=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    x=nums[j]-nums[i]
                    sum=max(sum,x)
        return sum
        