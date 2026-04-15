class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counts = [0] * 26
        for i in range(len(s)):
            print(f"{s[i]} --> {ord(s[i])}")
            char_counts[ord(s[i]) - ord('a')] += 1
            char_counts[ord(t[i]) - ord('a')] -= 1
        return char_counts == [0] * 26

        

