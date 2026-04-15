class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = 0

        l = 0
        r = 0

        if len(s) <= 1:
            return len(s)
        
        while r < len(s):
            print(f"(L, R) : ({l}, {r})")
            if s[r] not in seen or seen[s[r]] < l:
                print(f"s[r] : {s[r]} is valid")
                seen[s[r]] = r
                res = max(res, r - l + 1)
                r += 1
            else:
                print(f"s[r] : {s[r]} is invalid")
                l += 1
        
        return res



        