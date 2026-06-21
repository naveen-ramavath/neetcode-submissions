class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        l=0
        r=n
        while l<r and r<=len(s2):
            if Counter(s2[l:r])==Counter(s1):
                return True
            else:
                l+=1
                r+=1
        return False
        