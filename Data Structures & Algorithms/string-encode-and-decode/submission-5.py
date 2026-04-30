class Solution:

    def encode(self, strs: List[str]) -> str:

        # len:str:len:str

        result = []
        for s in strs:
            result.append(
                str(len(s))
            )
            result.append(s)
        
        return ":".join(result)

    def decode(self, s: str) -> List[str]:        
        i = 0

        result = []


        # 3:abc
        # 3:abc:4:abcd

        while i < len(s):
            delim_loc = s.find(":", i)

            substr_len = int(s[i : delim_loc])

            start = delim_loc + 1
            end = start + substr_len

            substr = s[start: end]
            result.append(substr)

            i = end + 1
        
        return result

