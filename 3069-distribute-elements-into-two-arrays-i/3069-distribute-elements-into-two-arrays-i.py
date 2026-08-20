class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        x1=[nums[0]]
        x2=[nums[1]]
        for i in range(2,len(nums)):
            if x1[-1]>x2[-1]:
                x1.append(nums[i])
            else:
                x2.append(nums[i])
        return x1+x2

        
        