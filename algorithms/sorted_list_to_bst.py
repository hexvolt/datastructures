# A solution for the following task on the leetcode.com:
#
# Given a singly linked list where elements are sorted in ascending order.
# Convert it to a height balanced BST.
#
# The solution is tend to minimize the runtime complexity [O(N log N)]
# and space complexity [O(log N)]

from math import log, trunc


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_list_length(head):
    """ Returns the length of the linked list """

    node = head

    length = 0
    while node:
        node = node.next
        length += 1

    return length


class Solution(object):

    current_node = None

    list_length = 0
    tree_height = 0

    def get_height(self, index):
        """
        Returns a height of the list node #index in future BST

        :param index: index of the list node of the linked list
        :return int: height in the tree, where 0 is the lowest height

        For example:
        indexes = [1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16]
        height    [                     4                               ]
                  [         3                          3                ]
                  [   2           2            2               2        ]
                  [1     1     1     1     1       1       1       1    ]
                  [                                                    0]
        """

        left, right = 1, self.list_length
        height = self.tree_height

        current_index = left + (right - left) / 2

        while current_index != index and left <= current_index <= right:

            if index < current_index:
                right = current_index - 1
            else:
                left = current_index + 1

            current_index = left + (right - left) / 2
            height -= 1

        return height

    def assign_heights(self, head):
        """
        Assigns a height for each list node in terms of its positions in BST
        """

        self.tree_height = trunc(log(self.list_length, 2))

        node = head

        index = 1
        while node:
            node.height = self.get_height(index)
            node = node.next
            index += 1

    def build_tree(self, node):

        top_node = node
        top_tree_node = TreeNode(node.val)

        self.current_node = node.next

        while self.current_node:

            # calculating the height delta between the current and topmost node
            delta = self.current_node.height - top_node.height

            if delta == 1:
                # current node is one level higher than the topmost,
                # so the old topmost node is a left child of the current one
                tree_node = TreeNode(self.current_node.val)
                tree_node.left = top_tree_node

                # assigning a new topmost node
                top_tree_node = tree_node
                top_node = self.current_node

            elif delta == -1:
                # current node is one level lower than the topmost,
                # so the current node is a right child of the topmost
                tree_node = TreeNode(self.current_node.val)
                top_tree_node.right = tree_node

            elif delta < -1:
                # current node is few levels lower than the topmost,
                # so the are no direct connection with the topmost
                if not top_tree_node.right:
                    # if there is no right branch yet - determine it:
                    top_tree_node.right = self.build_tree(self.current_node)

                else:
                    # the right branch already exists,
                    # so current node is descendant of rightmost tree node
                    right_tree_node = top_tree_node.right
                    right_tree_node.right = self.build_tree(self.current_node)

                continue

            elif delta > 1:
                # if we have a positive leap of height then there are no direct
                # ascendants in the provided linked list, i.e. we are inside
                # the sub-call and it is a time to quit and return its result
                return top_tree_node

            # move forward
            if self.current_node:
                self.current_node = self.current_node.next

        return top_tree_node

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return

        self.list_length = get_list_length(head)
        self.assign_heights(head)

        return self.build_tree(head)


if __name__ == '__main__':

    values = range(5)

    head = None

    for value in reversed(values):
        node = ListNode(value)
        node.next = head
        head = node

    solution = Solution()
    tree_root = solution.sortedListToBST(head)
