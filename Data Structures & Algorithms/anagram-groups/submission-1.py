class Solution:
    def check_anagram(self, str1, str2):
        if len(str1) != len(str2):
            return False
        else:
            letter_count_str1 = {}
            letter_count_str2 = {}
            for i in range(len(str1)):
                letter_count_str1[str1[i]] = 1 + letter_count_str1.get(str1[i],0)
                letter_count_str2[str2[i]] = 1 + letter_count_str2.get(str2[i],0)
            return letter_count_str1 == letter_count_str2
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        used_index = set()
        for i in range(len(strs)):
            anagram_array = []
            if (i not in used_index):
                anagram_array.append(strs[i])
                used_index.add(i)
                for j in range(i+1, len(strs)):
                    if (j not in used_index):
                        if self.check_anagram(strs[i],strs[j]):
                            anagram_array.append(strs[j])
                            used_index.add(j)
            if (anagram_array != []):
                output.append(anagram_array)
        return output
                