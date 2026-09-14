class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            while  nums[i] >= 1 and nums[i] <= len(nums):
                if nums[i] == nums[nums[i] - 1]:
                    break
                correct_index = nums[i] - 1
                temp = nums[i]
                nums[i] =  nums[correct_index]
                nums[correct_index] = temp

        smallest = 1

        for num in nums:
            if num == smallest:
                smallest += 1
            else:
                break

        return smallest

        
