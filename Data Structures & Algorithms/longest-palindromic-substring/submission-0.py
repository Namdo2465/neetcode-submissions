class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        if n == 1:
            return s
        else:
            max_cnt = 1
            res = ""
            for i in range(n):
                cnt = -1
                left = i
                right = i
                while left >= 0 and right < n and s[left] == s[right]:
                    cnt += 2
                    left -= 1
                    right += 1
                if cnt >= max_cnt:
                    max_cnt = cnt
                    res = s[left+1:right]
            for i in range(n-1):
                if s[i] != s[i+1]:
                    continue
                else: 
                    cnt = 0
                    left = i
                    right = i + 1
                    while left >= 0 and right < n and s[left] == s[right]:
                        cnt += 2
                        left -= 1
                        right += 1
                    if cnt >= max_cnt:
                        max_cnt = cnt
                        res = s[left+1:right]
            return res
        

        