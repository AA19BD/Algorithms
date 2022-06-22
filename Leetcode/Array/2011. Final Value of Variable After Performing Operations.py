class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        finalValue = 0
        for i in range(len(operations)):
            if operations[i] == '--X' or operations[i] == 'X--':
                finalValue -= 1
            # elif  operations[i] == '++X' or operations[i] == 'X++':
            else:
                finalValue += 1
        return finalValue