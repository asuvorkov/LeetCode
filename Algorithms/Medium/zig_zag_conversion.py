class Solution:
    @staticmethod
    def convert(s, num_rows):
        """
        :type s: str
        :type num_rows: int
        :rtype: str
        """
        length = len(s)
        result = ""
        hash_table = [""] * num_rows

        if num_rows >= length or num_rows == 1:
            return s

        for i in range(length):
            index = i % (2 * num_rows - 2)
            if index < num_rows:
                hash_table[index] += s[i]
            else:
                hash_table[2 * num_rows - 2 - index] += s[i]

        for i in range(num_rows):
            result += hash_table[i]

        return result


if __name__ == '__main__':
    print(Solution().convert("PAYPALISHIRING", 3))


# problem statement -> https://leetcode.com/problems/zigzag-conversion/
