class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            res = False
            dist = len(s1)
            s1_dict = {}
            for i in range(dist):
                s1_dict[s1[i]] = 1 + s1_dict.get(s1[i],0)
            for r in range(len(s2)):
                if s2[r] not in s1:
                    continue
                elif r + dist <= len(s2):
                    sub_dict = {}
                    substring = s2[r:r+dist]
                    for i in range(dist):
                        sub_dict[substring[i]] =  1 + sub_dict.get(substring[i],0)
                    if sub_dict == s1_dict:
                        res = True
        return res