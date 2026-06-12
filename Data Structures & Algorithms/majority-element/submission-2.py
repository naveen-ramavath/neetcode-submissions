class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n=defaultdict(int)
        # for i in nums:
        #     n[i]+=1
        # return max(n,key=n.get)
        candidate = None
        cnt = 0

        for num in nums:
            if cnt == 0:
                candidate = num

            if num == candidate:
                cnt += 1
            else:
                cnt -= 1

        return candidate