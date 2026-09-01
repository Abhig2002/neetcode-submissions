class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        keys = []
        values = []

        for s in strs:

            counts = [0] * 26

            for c in s:
                counts[ord(c) - ord('a')] += 1
            
            if tuple(counts) in hashmap:
                hashmap[tuple(counts)].append(s)
            else:
                hashmap[tuple(counts)] = [s]
                keys.append(tuple(counts))

        for key in keys:
            values.append(hashmap[key])

        return values




