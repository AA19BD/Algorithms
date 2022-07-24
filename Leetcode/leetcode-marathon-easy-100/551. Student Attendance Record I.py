class Solution:
    def checkRecord(self, s: str) -> bool:
        l_cnt = 0
        a_cnt = 0
        for att in s:
            if att != 'L':
                l_cnt = 0

            if att == 'A':
                a_cnt += 1
                if a_cnt >= 2:
                    return False

            if att == 'L':
                l_cnt += 1
                if l_cnt > 2:
                    return False
        return True
