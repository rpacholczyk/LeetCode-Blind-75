class Solution:
    def longestPalindrome(self, string: str) -> str:
        lenght = len(string)
        if lenght == 0:
            return ""

        start, maxLen = 0, 1

        # Traverse the input string
        for number in range(lenght):

        # THIS RUNS TWO TIMES 
        # for both odd and even length
        # palindromes. j = 0 means odd
        # and j = 1 means even length
            for second_number in range(2):
                low, high = number, number + second_number

            # Expand substring while it is a palindrome
            # and in bounds
                while low >= 0 and high < lenght and string[low] == string[high]:
                    currLen = high - low + 1
                    if currLen > maxLen:
                        start = low
                        maxLen = currLen
                    low -= 1
                    high += 1

        return string[start:start + maxLen]
