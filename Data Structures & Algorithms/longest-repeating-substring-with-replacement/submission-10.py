class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        k2 = k
        for i in range(len(s)):
            if s[i] == s[i-1] and i > 0:
                continue
            k2 = k
            length = 0
            for j in range(i,len(s)):
                if k2 < 0:
                    break
                elif k2 == 0:
                    if s[j] == s[i]:
                        length += 1
                    else: 
                        k2 -= 1
                else:
                    if s[j] == s[i]:
                        length += 1
                    else: 
                        k2 -= 1
                        length += 1
            if k2 == 0:
                k2 -= 1
            elif k2 > 0 and i > 0:
                for t in range(i-1, -1, -1):
                    if k2 == 0:
                        k2 -= 1
                        break
                    elif s[t] != s[i]:
                        length += 1
                        k2 -= 1
            res = max(res,length)
        if k2 >= 0: 
            res = len(s)
        res = min(res,len(s))
        return res
