class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        result = []

        for s in strs:

            counts = [0] * 26

            for c in s:
                counts[ord(c) - ord('a')] += 1
            
            if tuple(counts) in hashmap:
                hashmap[tuple(counts)].append(s)
            else:
                hashmap[tuple(counts)] = [s]

        for value in hashmap.values():
            result.append(value)

        return result




