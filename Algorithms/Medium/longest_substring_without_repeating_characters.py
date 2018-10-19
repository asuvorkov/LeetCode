class Solution:
    @staticmethod
    def longest_substring_without_repeating_characters(s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        char_dict = {}
        current_result = 0
        i = 0

        for char in list(s):
            if char in char_dict:
                if current_result > result:
                    result = current_result
                char_dict = {key: val for key, val in char_dict.items() if val > char_dict.get(char)}
                current_result = len(char_dict) + 1
            else:
                current_result += 1

            char_dict.update({char: i})
            i += 1

        if current_result > result:
            return current_result
        else:
            return result


if __name__ == '__main__':
    print(Solution().longest_substring_without_repeating_characters("aab"))


# problem statement -> https://leetcode.com/problems/longest-substring-without-repeating-characters/
