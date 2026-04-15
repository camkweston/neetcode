class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        best = ""
        for i in range(0, len(strs[0])):
            maybe = strs[0][0 : i + 1]
            for w in range(1, len(strs)):
                if not strs[w].startswith(maybe):
                    return best
            
            best = maybe
        

        return best

        