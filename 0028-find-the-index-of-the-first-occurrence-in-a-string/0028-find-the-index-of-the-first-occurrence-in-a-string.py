class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        l = 0 
        r = len(needle)
        while r<= n:
            if haystack[l:r] == needle:
                return l
            l+=1
            r+=1
        return -1
        