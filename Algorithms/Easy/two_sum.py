class Solution:
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_dict = {}

        for i in range(len(nums)):
            current_num = nums[i]
            complement = target - current_num
            if current_num in complement_dict:
                return [complement_dict[current_num], i]
            else:
                complement_dict.update({complement: i})


if __name__ == '__main__':
    Solution().two_sum([2, 7, 11, 15], 9)

# problem statement -> https://leetcode.com/problems/two-sum/description/
