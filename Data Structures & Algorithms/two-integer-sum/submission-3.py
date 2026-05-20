class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in map:
                map[nums[i]] = i
            else:
                if i < map[complement]:
                    return [i, map[complement]]
                else:
                    return [map[complement], i]
            
        return []


