class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:

            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
#         alpha_num_char_list = ""
#         for char in s:
#             if (ord(char)>=97 and ord(char)<=122) or (ord(char)>=65 and ord(char)<=90) or (ord(char)>=48 and ord(char)<=57):
#                 alpha_num_char_list += char.lower()

#         for char in range(0, (len(alpha_num_char_list)//2)):
#              if alpha_num_char_list[char] != alpha_num_char_list[len(alpha_num_char_list)-char-1]:
#                     return False
#         return True
