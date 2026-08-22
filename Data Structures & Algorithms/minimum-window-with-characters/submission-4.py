class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        for char in t:
            countT[char] += 1
        have = 0
        need = len(countT)
        i = 0
        window = defaultdict(int)
        seen = set()
        res, resLen = [-1, -1], float('inf')
        
        for j in range(len(s)):
            window[s[j]] += 1
            if s[j] not in seen and s[j] in countT and window[s[j]] >= countT[s[j]]:
                have += 1
                seen.add(s[j])
            if have == need:
                while s[i] not in countT or window[s[i]] - 1 >= countT[s[i]]:
                    window[s[i]] -= 1
                    i += 1
                if resLen > j - i + 1:
                    resLen = j - i + 1
                    res = [i, j]
        if resLen != float('inf'):
            i = res[0]
            j = res[1]
            return s[i:j+1] 
        else:
            return ""
            
        