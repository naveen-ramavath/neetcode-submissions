class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        n=len(nums)
        dp=[[-1]*n for _ in range(n)]
        def f(i,j):
            if i>j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            ans=0
            for k in range(i,j+1):
                cost=nums[i-1]*nums[k]*nums[j+1]+f(i,k-1)+f(k+1,j)
                ans=max(cost,ans)
            dp[i][j]=ans
            return ans
        return f(1,n-2)
        