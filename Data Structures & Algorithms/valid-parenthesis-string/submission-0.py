class Solution:
    def checkValidString(self, s: str) -> bool:
        stackP = []
        stackS = []

        for i, c in enumerate(s):
            if c == "(":
                stackP.append(i)
            elif c == "*":
                stackS.append(i)
            else:
                if stackP:
                    stackP.pop()
                elif stackS:
                    stackS.pop()
                else:
                    return False
        while stackP and stackS:
            p, s = stackP.pop(), stackS.pop()
            if p > s:
                return False
        return True if not stackP else False
