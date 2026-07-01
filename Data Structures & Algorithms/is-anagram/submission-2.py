class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S_letters = {}
        T_letters = {}
        for letter in s:
            S_letters[letter] = S_letters.get(letter, 0) + 1
        for letter in t:
            T_letters[letter] = T_letters.get(letter,0) + 1
        return S_letters == T_letters
        