class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # # return sorted(s)==sorted(t)
        # c={}
        # for i in s:
        #     c[i]=c.get(i,0)+1
        # for j in t:
        #     if j not in c:
        #         return False
        #     c[j]-=1
        #     if c[j]<0:
        #         return False
            
        # return True

        if len(s) != len(t):
            return False

        c = defaultdict(int)

        for ch in s:
            c[ch] += 1

        for ch in t:
            c[ch] -= 1
            if c[ch] < 0:
                return False

        return True
            
        