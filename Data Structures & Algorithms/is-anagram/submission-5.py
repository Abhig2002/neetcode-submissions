class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        S, T = {}, {}

        if len(s) != len(t):
            return False

        for cs, ct in zip(s, t):
            if cs not in S:
                S[cs] = 1
            else:
                S[cs] += 1

            if ct not in T:
                T[ct] = 1
            
            else:
                T[ct] += 1
        
        return S == T
