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
