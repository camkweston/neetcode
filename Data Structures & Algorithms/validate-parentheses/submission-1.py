class Solution:
    def isValid(self, s: str) -> bool:
        res = 0

        stack = []

        open_p = set(["(", "{", "["])

        closed_p = {
            "}" : "{",
            "]" : "[", 
            ")" : "("
        }

        for i, s in enumerate(s):
            if s in open_p:
                stack.append(s)
            elif s in closed_p:
                if not stack:
                    res += 1
                elif stack[-1] != closed_p[s]:                
                    res += 1
                else:
                    stack.pop(-1)
        
        print("Num invalid : ", res + len(stack))
        return res == 0 and len(stack) == 0

        