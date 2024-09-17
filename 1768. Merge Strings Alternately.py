class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = []
        len1, len2 = len(word1), len(word2)

        for i in range(max(len1, len2)):
            if i < len1:
                word.append(word1[i])
            if i < len2:
                word.append(word2[i])

        return ''.join(word)



    
print(Solution.mergeAlternately(Solution, 'abcde', '123'))