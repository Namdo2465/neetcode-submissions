class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        else:
            t_dict = {}
            for letter in t:
                t_dict[letter] = 1 + t_dict.get(letter,0)
            min_length = 1000000000000
            output_dict = {}
            l = 0
            r = 0
            for l in range(len(s)):
                if s[l] not in t:
                    continue
                else:
                    r = l+1
                    while r <= len(s):
                        word = s[l:r]
                        enough = True
                        s_dict = {}
                        for letter in word:
                            s_dict[letter] = 1 + s_dict.get(letter,0)
                        for key in t_dict:
                            if key not in s_dict:
                                enough = False
                            elif t_dict[key] > s_dict[key]:
                                enough = False
                        if enough == False:
                            r += 1
                        else:
                            length = r - l + 1
                            output_dict[length] = s[l:r]
                            min_length = min(min_length,length)
                            break
            if min_length == 1000000000000:
                return ""
            else:
                return output_dict[min_length]




