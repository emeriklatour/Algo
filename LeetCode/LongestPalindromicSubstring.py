class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        max_palindrome = ""
        for i in range(len(s)+1)[::-1]:
            for j in range(i + 1):
                if s[j:i] == s[j:i][::-1] and len(s[j:i]) > len(max_palindrome):
                    max_palindrome = s[j:i]
                    break
        return max_palindrome

def test_longest_palindromic_substring():
    lps = LongestPalindromicSubstring()
    print(lps.longestPalindrome("abbb"))


test_longest_palindromic_substring()
