class Solution:
    @staticmethod
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = int("-" + (str(x)[::-1])[0:-1])
            return 0 if x < -2**31 else x
        else:
            x = int(str(x)[::-1])
            return 0 if x > 2**31 - 1 else x


if __name__ == '__main__':
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))


# problem statement -> https://leetcode.com/problems/reverse-integer/
