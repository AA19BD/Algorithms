class Solution:
    def reverseWords(self, s: str) -> str:
        # res = str() # First approach
        # for i in s.split():
        #     res += " " + i[::-1]
        # return  res.strip()
        # return " ".join([i[::-1] for i in s.split()]) # Second approach

        word = s.split(" ") # Third approach
        for w in range(len(word)):
            word[w] = word[w][::-1]
        return " ".join(word)