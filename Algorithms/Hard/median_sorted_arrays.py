class Solution:
    def find_median_sorted_arrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)

        if n == 0:
            middle = self.find_middle(nums2)
            if len(middle) > 1:
                return float((middle[0] + middle[1]) / 2)
            else:
                return float(middle[0])

        if m == 0:
            middle = self.find_middle(nums1)
            if len(middle) > 1:
                return float((middle[0] + middle[1]) / 2)
            else:
                return float(middle[0])

        merged_list = [None] * (n + m)

        i = 0
        j = 0
        merged_index = 0

        while i < n or j < m:
            if i == n:
                while j < m:
                    merged_list[merged_index] = nums2[j]
                    merged_index += 1
                    j += 1
                break

            if j == m:
                while i < n:
                    merged_list[merged_index] = nums1[i]
                    merged_index += 1
                    i += 1
                break

            if nums1[i] < nums2[j]:
                merged_list[merged_index] = nums1[i]
                i += 1
            else:
                merged_list[merged_index] = nums2[j]
                j += 1

            merged_index += 1

        middle = self.find_middle(merged_list)
        if len(middle) > 1:
            return float((middle[0] + middle[1]) / 2)
        else:
            return float(middle[0])

    @staticmethod
    def find_middle(input_list):
        length = len(input_list)
        middle = int(length / 2)

        if length % 2 == 0:
            return [input_list[middle - 1], input_list[middle]]
        else:
            return [input_list[middle]]


if __name__ == '__main__':
    print(Solution().find_median_sorted_arrays([], [1, 2, 3, 4, 5, 6, 7]))


# problem statement -> https://leetcode.com/problems/median-of-two-sorted-arrays/
