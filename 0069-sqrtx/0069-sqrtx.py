class Solution:
    def mySqrt(self, x: int) -> int:
        nums=0
        for i in range(x+1):
            if i*i >x:
                break
            elif i*i<=x:
                nums=i
        return nums
         



        