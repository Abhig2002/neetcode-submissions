class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def helper(nums: List[int]):
                    
            dp = [None] * len(nums) 

            for i in range(len(nums)):
                if i == 0:
                    dp[i] = nums[i]
                elif i == 1:
                    if dp[i-1] > nums[i]:
                        dp[i] = dp[i-1]
                    else:
                        dp[i] = nums[i]
                else:
                    if dp[i-1] > dp[i-2] + nums[i]:
                        dp[i] = dp[i-1]
                    else:
                        dp[i] = dp[i-2] + nums[i]
            
            return dp[-1]
        
        return max(helper(nums[1:]) , helper(nums[0:len(nums)-1]))
            
        