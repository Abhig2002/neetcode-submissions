class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashset = set()

        left = 0
        maxLength = 0

        for right in range(len(s)):

            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1

            hashset.add(s[right])

            maxLength = max(maxLength, right - left + 1)

        return maxLength