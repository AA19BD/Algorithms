class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerical = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000, 'IV': 5, 'IX': 9,
            'XL': 50, 'XC': 90, 'CD': 500, 'CM': 900
        }

        sum_ = 0
        pred = 0
        for char in s:
            cur = roman_numerical[char]
            if pred < cur:
                sum_ -= pred * 2
            sum_ += cur
            pred = cur
        return sum_

        # ans = 0
        # i = 0
        # while i < len(s):
        #     if i < len(s) - 1 and roman_numerical[s[i]] < roman_numerical[s[i + 1]]:
        #         ans += roman_numerical[s[i + 1]] - roman_numerical[s[i]]
        #         i += 2
        #     else:
        #         ans += roman_numerical[s[i]]
        #         i += 1
        #
        # return ans