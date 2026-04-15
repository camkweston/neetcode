class Solution:


    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(word: str, memo: dict):

            if word in memo:
                return memo[word]

            l = 0
            r = len(word) - 1

            while l <= r:
                if word[l] != word[r]:
                    memo[word] = False
                    return False
                else:
                    l += 1
                    r -= 1
            memo[word] = True
            return True



        best = s[0]
        memo = {}

        for i in range(len(s)):
            for j in range(i, len(s)):
                candidate = s[i:j+1]
                if len(candidate) > len(best) and isPalindrome(candidate, memo):
                    best = s[i : j+1]
        
        return best

