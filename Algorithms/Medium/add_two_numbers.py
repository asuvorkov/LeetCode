# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, x):
        if self.val is None:
            self.val = x
            return

        node = self

        while node.next is not None:
            node = node.next
        node.next = ListNode(x)


class Solution:
    @staticmethod
    def add_two_numbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        linked_list_1 = l1
        linked_list_2 = l2

        rest = 0
        result = ListNode(None)

        while linked_list_1 is not None or linked_list_2 is not None:

            if linked_list_1 is not None and linked_list_2 is not None:
                val_sum = linked_list_1.val + linked_list_2.val + rest
            else:
                if linked_list_1 is None:
                    val_sum = linked_list_2.val + rest
                else:
                    val_sum = linked_list_1.val + rest

            if val_sum == 10:
                rest = 1
                val_sum = 0
            else:
                if val_sum > 10:
                    rest = 1
                    val_sum -= 10
                else:
                    rest = 0

            if result.val is None:
                result.val = val_sum
            else:
                node = result

                while node.next is not None:
                    node = node.next
                node.next = ListNode(val_sum)

            if linked_list_1 is not None:
                linked_list_1 = linked_list_1.next

            if linked_list_2 is not None:
                linked_list_2 = linked_list_2.next

        if rest > 0:
            node = result

            while node.next is not None:
                node = node.next
            node.next = ListNode(rest)

        return result


if __name__ == '__main__':
    list1 = ListNode(9)
    list1.add(4)
    list1.add(3)

    list2 = ListNode(9)
    list2.add(6)
    list2.add(4)

    print(Solution().add_two_numbers(list1, list2))


# problem statement -> https://leetcode.com/problems/add-two-numbers