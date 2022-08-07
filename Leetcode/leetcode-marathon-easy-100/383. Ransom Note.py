class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False

        ransom_d = {}
        magazine_d = {}
        for i in range(len(magazine)):
            magazine_d[magazine[i]] = magazine_d.get(magazine[i], 0) + 1

        for i in range(len(ransomNote)):
            ransom_d[ransomNote[i]] = ransom_d.get(ransomNote[i], 0) + 1

        # print(ransom_d, magazine_d)

        for k, v in ransom_d.items():
            if not (k in magazine_d and v <= magazine_d.get(k)):
                return False
        return True
        # print(k, v, magazine_d.get(k))
