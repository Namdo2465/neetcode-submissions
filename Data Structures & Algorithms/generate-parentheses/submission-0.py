class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(openCnt, closingCnt, path):
            if openCnt == n and closingCnt == n:
                res.append("".join(path))
            if openCnt < n:
                path.append('(')
                backtrack(openCnt + 1, closingCnt, path)
                path.pop()
            if closingCnt < openCnt:
                path.append(')')
                backtrack(openCnt, closingCnt + 1, path)
                path.pop()
        backtrack(0, 0, [])
        return res
