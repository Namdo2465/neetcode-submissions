import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        store = []
        for i in tokens:
            if i not in '+-*/':
                store.append(int(i))
            elif i == "+":
                y = store.pop()
                x = store.pop()
                res = x + y
                store.append(res)
            elif i == "-":
                y = store.pop()
                x = store.pop()
                res = x - y
                store.append(res)
            elif i == "*":
                y = store.pop()
                x = store.pop()
                res = x * y
                store.append(res)
            elif i == "/":
                y = store.pop()
                x = store.pop()
                res = math.trunc(x / y)
                store.append(res)
        return store.pop()