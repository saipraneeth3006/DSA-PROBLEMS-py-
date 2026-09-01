class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        a=requests[0]
        for i in range(1,len(requests)):
            a=a+abs(requests[i]-requests[i-1])
        return a
                