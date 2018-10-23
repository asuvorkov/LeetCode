class Solution:
    @staticmethod
    def longest_palindrome(s):
        ss = ''
        for i in s:
            ss = ss + '#'
            ss = ss + i
        ss = ss + '#'
        p = [0] * 2001
        start, end, max_length, mx = 0, 0, 0, 0

        for i in range(len(ss)):
            if i < mx:
                p[i] = min(p[2 * id - i], mx - i)
            else:
                p[i] = 1
            while (i - p[i]) >= 0 and i + p[i] < len(ss) and ss[i - p[i]] == ss[i + p[i]]:
                p[i] += 1
            if mx < i + p[i]:
                id = i
                mx = i + p[i]
            if max_length < (p[i] - 1):
                max_length = p[i] - 1
                start = i + 1 - p[i]
                end = i + p[i] - 1

        return ss[start:end + 1].replace('#', '')


if __name__ == '__main__':
    print(Solution().longest_palindrome("ccc"))
    print(Solution().longest_palindrome("babad"))
    print(Solution().longest_palindrome("cbbd"))
    print(Solution().longest_palindrome("tenet"))
    print(Solution().longest_palindrome("redder"))
    print(Solution().longest_palindrome("repaper"))

# problem statement -> https://leetcode.com/problems/longest-palindromic-substring/
