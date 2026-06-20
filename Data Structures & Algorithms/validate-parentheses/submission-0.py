class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c not in brackets:
                stack.append(c)
            else:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
