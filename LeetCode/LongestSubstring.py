class LongestSubstring:
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        max_len = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(set(s[i:j])) == len(s[i:j]):
                    max_len = max(max_len, j - i)
                else:
                    break
        return max_len


def test_longest_substring():
    ls = LongestSubstring()
    print(ls.lengthOfLongestSubstring("abaabcbb"))


test_longest_substring()
