class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        s_chars = [c for c in s]
        t_chars = [c for c in t]

        s_chars.sort()
        t_chars.sort()

        return s_chars == t_chars
        