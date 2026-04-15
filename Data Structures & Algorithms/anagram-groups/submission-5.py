class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        result = [[strs.pop(0)]]

        for word in strs:
            found_match = False
            for sl in result:
                if self.isAnagram(word, sl[0]):
                    sl.append(word)
                    found_match = True
                    break
            if not found_match:
                result.append([word])
        
        return result


    
    def isAnagram(self, w1: str, w2:str) -> bool:
        if len(w1) != len(w2):
            return False
        seen = [0] * 26
        for i in range(len(w1)):
            c1 = w1[i]
            c2 = w2[i]
            seen[ord(c1) - ord('a')] += 1
            seen[ord(c2) - ord('a')] -= 1
        
        return seen == [0] * 26

        