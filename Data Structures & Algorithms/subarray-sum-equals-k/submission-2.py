class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        mp={0:1}
        prefix=0
        c=0
        for i in nums:
            prefix+=i
            if prefix-k in mp:
                c+=mp[prefix-k]
            mp[prefix]=mp.get(prefix,0)+1
        return c
        