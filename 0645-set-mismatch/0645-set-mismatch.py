class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup=0
        miss=0
        s=set()
        for i in range(len(nums)):
            val=nums[i]
            if val not in s:
                s.add(val)
            else:
                dup=val
        for i in range(0,len(nums)+1):
            if i not in s:
                miss=i
        return [dup,miss]
        