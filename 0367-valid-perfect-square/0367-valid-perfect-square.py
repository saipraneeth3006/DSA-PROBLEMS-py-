class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        odd=1
        while num>0:
            num=num-odd
            odd=odd+2
        if num==0:
            return True
        else:
            return False
        