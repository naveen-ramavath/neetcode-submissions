class Solution:
    def isPalindrome(self, s: str) -> bool:
        filt=""
        for i in s:
            if i.isalnum():
                filt+=i.lower()
        left=0
        right=len(filt)-1
        while left<right:
            if filt[left] != filt[right]:
                return False
            else:
                left+=1
                right-=1
        return True
                
        
