class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = 0;
        nums.sort()
        bucket = [[] for _ in range(len(nums) + 1)]

        result = []
        
        for i in range(len(nums)):

            if i == 0:
                count += 1
            elif nums[i] == nums[i-1]:
                count += 1
            else:
                bucket[count].append(nums[i-1])
                count = 1
        
        bucket[count].append(nums[-1])

        for i in range(len(bucket)-1, -1, -1):
            for j in range(len(bucket[i])):
                
                if k == 0:
                    break
                
                result.append(bucket[i][j])
                k -= 1
            
            if k == 0:
                break

           
        return result