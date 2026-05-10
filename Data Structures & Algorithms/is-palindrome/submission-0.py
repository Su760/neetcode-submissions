class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = ''
        for c in s:
            if c.isalnum():
                letters += c.lower()
        return letters == letters[::-1]
