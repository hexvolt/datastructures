# A solution for the following task:
#
# 8.4 Write a method to return all subsets of a set


class Solution(object):

    result = None

    def __init__(self):
        self.result = {}

    def get_all_subsets(self, initial_set):
        """
        :param set initial_set: a set to find all the subsets of
        :rtype: list
        """

        subsets = []

        if not initial_set:
            return []

        for item in initial_set:
            subset1, subset2 = {item}, initial_set - {item}
            subsets.append(subset1)

            if subset2:
                subsets.append(subset2)
                subsets += self.get_all_subsets(subset2)

        return subsets

    def solve(self, initial_set):
        """
        :type initial_set: set
        """
        subsets = self.get_all_subsets(initial_set=initial_set)

        # filtering out the duplicates
        subsets = [frozenset(s) for s in subsets]
        return list(set(subsets))


if __name__ == '__main__':
    initial_set = {1, 2, 3, 4}
    print("Initial set: ", initial_set)

    solution = Solution()
    subsets = solution.solve(initial_set=initial_set)

    print("This set has {} subsets:".format(len(subsets)))

    for subset in subsets:
        print(subset)
