class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word = strs[0]
        ans = ""
        for i in range(len(min_word)):
            flag = True
            for word in strs[1:]:
                if i > len(word) - 1 or min_word[i] != word[i]:
                    flag = False
                    break
            if flag:
                ans += min_word[i]
            else:
                break
        return ans
