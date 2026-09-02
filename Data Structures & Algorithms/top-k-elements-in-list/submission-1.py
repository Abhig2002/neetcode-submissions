class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        keys  = []
        bucket = [[] for i in range(len(nums)+1)]
        result = []

        for num in nums:

            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
                keys.append(num)
        
        for key in keys:
            bucket[counts[key]].append(key)

        for i in range(len(bucket)-1, 0, -1):
            for j in range(len(bucket[i])):

                if k == 0:
                    break

                result.append(bucket[i][j])
                k -= 1
            
            if k == 0:
                break
        
        return result
            


