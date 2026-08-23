class Solution:
    def checkDivisibility(self, n: int) -> bool:
        org=n
        sum=0
        mul=1
        while n>0:
            x=n%10
            n=n//10
            sum=sum+x
            mul=mul*x
        if org%(sum+mul)==0:
            return True
        else:
            return False
