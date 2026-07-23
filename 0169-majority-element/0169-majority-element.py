class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        y={}
        for i in range(len(nums)):
            val=nums[i]
            if val not in y:
                y[val]=1
            else:
                y[val]=y[val]+1
        z=max(y,key=y.get)
        return z
        