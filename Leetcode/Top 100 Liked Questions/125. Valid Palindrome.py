class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num_char_list = ""
        for char in s:
            if (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90) or (
                    ord(char) >= 48 and ord(char) <= 57):
                alpha_num_char_list += char.lower()

        for char in range(0, (len(alpha_num_char_list) // 2)):
            if alpha_num_char_list[char] != alpha_num_char_list[len(alpha_num_char_list) - char - 1]:
                return False
        return True