class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        text = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # text[i][j] -> max length of subsequence 
        # between text1[i:] and text2[j:]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    text[i][j] = 1 + text[i+1][j+1]
                else:
                    text[i][j] = max(text[i+1][j], text[i][j+1])
        return text[0][0]