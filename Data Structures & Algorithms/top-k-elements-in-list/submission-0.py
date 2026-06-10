class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=defaultdict(int)
        for i in nums:
            l[i]+=1
        # for j in l:
        #     if l[j]>=k:
        #         a.append(l[j])
        sorted_items = sorted(l.items(),
                              key=lambda x: x[1],
                              reverse=True)

        return [num for num, count in sorted_items[:k]]
        
        