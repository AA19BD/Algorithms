class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digit = int("".join(map(str, digits))) + 1
        # # print(digit)
        # stack = []
        # while digit:
        #     digit, d = divmod(digit, 10)
        #     stack.insert(0, d)
        # return stack
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)
        return digits if not carry else [carry] + digits

