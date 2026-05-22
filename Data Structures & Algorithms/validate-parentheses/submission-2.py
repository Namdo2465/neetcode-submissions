class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CloseToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if char not in CloseToOpen:
                stack.append(char)
            else:
                if stack and CloseToOpen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False