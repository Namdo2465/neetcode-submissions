class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        global word_list
        word_list = []
        for word in strs:
            output += word
            word_list.append(word)
        return output

    def decode(self, s: str) -> List[str]:
        return word_list
        