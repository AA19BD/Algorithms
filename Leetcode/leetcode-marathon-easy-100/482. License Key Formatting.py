class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s_format = s.upper().replace('-', '')

        if len(s_format) % k != 0:
            a = ([s_format[:len(s_format) % k]] + [s_format[i:i + k] for i in
                                                   range(len(s_format) % k, len(s_format), k)])
        else:
            a = ([s_format[i:i + k] for i in range(0, len(s_format), k)])
        return "-".join(a)

