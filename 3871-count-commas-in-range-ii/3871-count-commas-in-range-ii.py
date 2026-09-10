class Solution:
    def countCommas(self, n: int) -> int:
        p=1000
        s=0
        while p<=n:
            s+=n-p+1
            p=p*1000
        return s
        