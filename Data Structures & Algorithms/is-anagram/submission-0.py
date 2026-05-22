class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_list_1 = sorted(list(s))
        char_list_2 = sorted(list(t))
        if (char_list_1 == char_list_2):
            return True
        else:
            return False
        