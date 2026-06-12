class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=defaultdict(int)
        for i in nums:
            n[i]+=1
        return max(n,key=n.get)