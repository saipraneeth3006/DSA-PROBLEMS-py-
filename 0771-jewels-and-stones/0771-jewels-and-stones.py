class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum=0
        x=set(jewels)
        for i in stones:
            if i in jewels:
                sum=sum+1
        return sum
        