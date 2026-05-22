class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        elif t == "":
            return ""
        
        countT, window = {}, {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("infinity")
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in t and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        if resLen == float("infinity"):
            return ""
        else:
            l = res[0]
            r = res[1]
            return s[l:r+1]