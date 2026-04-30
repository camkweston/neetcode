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
                    return False
                elif stack[-1] != closed_p[s]:                
                    return False
                else:
                    stack.pop(-1)
        
        return len(stack) == 0

        