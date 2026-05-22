import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        for i in range(len(cleaned_text) // 2):
            if cleaned_text[i].lower() != cleaned_text[len(cleaned_text) - 1 - i].lower():
                return False
        return True