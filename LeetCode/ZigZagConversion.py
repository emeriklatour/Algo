class ZigZagConversion:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ""
        for i in range(numRows):
            j = i
            while j < len(s):
                result += s[j]
                if i != 0 and i != numRows - 1 and j + 2 * (numRows - i - 1) < len(s):
                    result += s[j + 2 * (numRows - i - 1)]
                j += 2 * (numRows - 1)
        return result