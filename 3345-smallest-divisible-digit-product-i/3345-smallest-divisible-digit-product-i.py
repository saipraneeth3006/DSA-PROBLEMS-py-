class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+10):
            f=1
            for digit in str(i):
                f=f*int(digit)
            if f%t==0:
                return i
                
        
        
        