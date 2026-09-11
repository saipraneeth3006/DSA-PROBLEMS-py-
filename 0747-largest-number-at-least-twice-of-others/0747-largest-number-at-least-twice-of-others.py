class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        count=0
        li=nums[:]
        nums.sort()
        m=max(nums)
        nums.pop()
        for i in nums:
            if m>=i*2:
                count+=1
            else:
                return -1
        if count==len(nums):
            return li.index(max(li))