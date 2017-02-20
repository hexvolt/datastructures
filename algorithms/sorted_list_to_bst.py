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


def assign_heights(head):
    medium = get_list_length(head) / 2


class Solution(object):

    current_node = None

    def build_tree(self, node):

        topmost_node = node
        topmost_tree_node = TreeNode(node.val)

        self.current_node = node.next

        while self.current_node:

            # calculating the height delta between the current node and the topmost node
            delta = self.current_node.height - topmost_node.height

            if delta == 1:
                # current node is one level higher than the topmost, so the old topmost node is a left child of the current one
                tree_node = TreeNode(self.current_node.val)
                tree_node.left = topmost_tree_node

                # assigning a new topmost node
                topmost_tree_node = tree_node
                topmost_node = self.current_node

            elif delta == -1:
                # current node is one level lower than the topmost, so the current node is a right child of the topmost
                tree_node = TreeNode(self.current_node.val)
                topmost_tree_node.right = tree_node

            elif delta < -1:
                # current node is few levels lower than the topmost, so the are no direct connection with the topmost
                if not topmost_tree_node.right:
                    # if there is no right branch yet - determine it:
                    topmost_tree_node.right = self.build_tree(self.current_node)
                else:
                    # the right branch already exists so current node is descendant of topmost's right branch
                    topmost_tree_node.right.right = self.build_tree(self.current_node)

                continue

            elif delta > 1:
                # if we have a positive leap of height then there are no direct ascendants in the provided linked list,
                # i.e. we are inside the subcall and it is a time to quit and return a result of subcall
                return topmost_tree_node

            # move forward
            if self.current_node:
                self.current_node = self.current_node.next

        return topmost_tree_node

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # preparation
        assign_heights(head)

        return self.build_tree(head)


if __name__ == '__main__':

    heights = [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 0]

    head = None

    for i, height in enumerate(reversed(heights)):
        node = ListNode(len(heights) - i)
        node.height = height
        node.next = head
        head = node

    solution = Solution()
    tree_root = solution.sortedListToBST(head)
    print(tree_root)
