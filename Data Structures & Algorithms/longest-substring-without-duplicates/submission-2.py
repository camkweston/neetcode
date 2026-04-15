class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = 0

        l = 0
        r = 0

        if len(s) <= 1:
            return len(s)
        
        while r < len(s):
            if s[r] not in seen or seen[s[r]] < l:
                seen[s[r]] = r
                res = max(res, r - l + 1)
                r += 1
            else:
                l += 1
        
        return res



        