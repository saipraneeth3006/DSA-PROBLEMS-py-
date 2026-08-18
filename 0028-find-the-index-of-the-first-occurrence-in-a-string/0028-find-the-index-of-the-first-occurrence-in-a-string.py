class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)
        for i in range(n+1-m):
            match=True
            for j in range(m):
                if haystack[i+j]!=needle[j]:
                    match=False
                    break
            if match:
                return i
        return -1

        