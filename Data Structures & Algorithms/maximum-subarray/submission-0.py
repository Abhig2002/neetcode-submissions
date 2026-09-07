class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        left, right = 0, 0
        maxSum = None
        currSum = None

        for right in range(len(nums)):
            if right == 0:
                maxSum = nums[right]
                currSum = nums[right]
            else:
                if nums[right] > nums[right] + currSum:
                    left += 1
                    currSum = nums[right]
                    if currSum > maxSum:
                        maxSum = currSum
                else:
                    currSum = nums[right] + currSum
                    if currSum > maxSum:
                        maxSum = currSum

        return maxSum

