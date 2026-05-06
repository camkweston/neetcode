class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        big = s1 if s1_len > s2_len else s2
        small = s2 if s1 == big else s1

        l = 0 
        r = len(small) - 1

        small_chars = [
            0 for _ in range(27)
        ]

        for c in small:
            small_chars[ord(c) - ord('a')] += 1

        big_chars = [
            0 for _ in range(27)
        ]

        for c in range(0, len(small)):
            big_chars[ord(big[c]) - ord('a')] += 1

        while r < len(big) - 1:
            print(small_chars)
            print(big_chars)
            if small_chars == big_chars:
                return True
            else:
                l_val = big[l]
                print("removing ", l_val)
                big_chars[ord(l_val) - ord('a')] -= 1
                l += 1


                r += 1
                r_val = big[r]
                print("Adding ", r_val)
                big_chars[ord(r_val) - ord('a')] += 1
        

        return small_chars == big_chars










        