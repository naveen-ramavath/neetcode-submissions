class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans=[]
        
        # for i in range(len(temperatures)):
        #     found=False
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             ans.append(j-i)
        #             found=True
        #             break
        #     if not found:
        #         ans.append(0)      
        # return ans

        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)

        return ans