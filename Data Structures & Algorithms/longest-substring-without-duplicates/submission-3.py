class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substr = set()

        l = 0 
        r = 0

        best = 0

        while r < len(s):
            if s[r] not in substr:
                substr.add(s[r])
                r += 1
                best = max(best, r - l)
            else:
                while l <= r:
                    substr.remove(s[l])
                    l += 1 
                    if s[l-1] == s[r]:
                        break
        return best
                    

            
        