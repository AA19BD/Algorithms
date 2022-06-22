class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_num_words = []
        for i in sentences:
            max_num_words.append(i.count(' ')+1)
        return max(max_num_words)