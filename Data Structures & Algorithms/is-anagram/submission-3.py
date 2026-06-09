class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # return sorted(s)==sorted(t)
        c={}
        for i in s:
            c[i]=c.get(i,0)+1
        for j in t:
            if j not in c:
                return False
            c[j]-=1
            if c[j]<0:
                return False
            
        return True
            
        