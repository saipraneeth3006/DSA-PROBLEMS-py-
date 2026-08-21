class Solution:
    def countValidPrefixes(self, s: str) -> int:
        x=0
        ns,no=0,0
        for i in s:
            if i=="0":
                ns=ns+1
            else:
                no=no+1
            if abs(no-ns)<=1:
                x=x+1
        return x

        