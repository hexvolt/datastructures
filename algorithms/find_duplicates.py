# Find Duplicates: You have an array with all the numbers from 1 to N, where
# N is at most 32,000. The array may have duplicate entries and you do not
# know what N is. With only 4 kilobytes of memory available, how would you
# print all duplicate elements in the array?


class BitVector(object):
    """
    Data structure which stores bits packed into array of bytes.
    """

    _vector = None

    def __init__(self, vector_size):
        self._vector = bytearray([0 for _ in range(vector_size)])

    def get_bit_address(self, number):
        """
        Returns the number of byte and number of bit
        which correspond to a given number.

        :param int number:
        :rtype: tupple
        """
        return number // 8, number % 8

    def include(self, number):
        """
        Sets a bit in the BitVector which corresponds given number
        """
        byte_num, bit_num = self.get_bit_address(number=number)
        self._vector[byte_num] |= 1 << bit_num

    def __contains__(self, item):
        byte_num, bit_num = self.get_bit_address(number=item)
        return (self._vector[byte_num] >> bit_num) & 1


if __name__ == '__main__':
    array = [1, 5, 31769, 31754, 44, 2, 1, 31769, 23, 2, 105, 3, 105]

    bit_vector = BitVector(vector_size=32000)

    for number in array:
        if number in bit_vector:
            print("Duplicate: %d" % number)
        else:
            bit_vector.include(number=number)
