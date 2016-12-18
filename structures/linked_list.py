import collections


class Node(object):
    """
    Represents a single item of the LinkedList.
    Each Node has a certain value and a connection with another Node.
    """

    value = None
    next = None
    
    def __init__(self, value, next=None):
        super(Node, self).__init__()
        
        self.value = value
        self.next = next
    
    def __repr__(self):
        return str(self.value)


class LinkedList(collections.MutableSequence):
    """
    Represents a LinkedList data structure which comprises a sequence of Nodes.
    """

    head = None
    
    def __init__(self, *args):
        if not len(args):
            return
        
        self.head = Node(args[0])
        last_node = self.head
        
        for arg in args[1:]:
            node = Node(arg)
            last_node.next = node
            last_node = node
    
    def __contains__(self, value):
        """ Inherited from base Container class """

        return any(node.value == value for node in self)
        
    def __len__(self):
        """ Inherited from base Sized class """

        return sum(1 for node in self)
        
    def __iter__(self):
        """ Inherited from base Iterable class """
        
        # this method of iterable object must return an iterator object with
        # __next__() method etc. Generator basically supports all the
        # requirements for iterators, so here we are just defining a
        # generator function

        node = self.head
            
        while node:
            yield node
            node = node.next
    
    # The following methods are inherited from the base Sequence class:

    def __reversed__(self):
        """
        Returns a new iterator object that iterates items in reverse order
        """
        return self.traverse_backward(self.head)
    
    def __getitem__(self, index):

        if not isinstance(index, int):
            raise TypeError('Index must be an integer.')
        
        for i, node in enumerate(self):
            if i == index:
                return node
        
        raise IndexError('Index out of LinkedList length.')
    
    # The following methods are inherited from the base MutableSequence class:
    def __setitem__(self, index, value):
        self[index].value = value
    
    def __delitem__(self, index):
        next_node = self[index].next

        if index > 0:
            prev_node = self[index-1]
            prev_node.next = next_node

        else:
            self.head = next_node
    
    def append(self, node):
        pass

    def insert(self, index, value):
        current_node = self[index]
        new_node = Node(value, current_node)
        
        if index > 0:
            prev_node = self[index-1]
            prev_node.next = new_node
        else:
            self.head = new_node
    
    def remove(self, index):
        pass
    
    def pop(self, index):
        pass
    
    # custom methods

    def traverse_forward(self, node=None):
        if node is None:
            return   
        
        yield node
        
        for sub_node in self.traverse_forward(node.next):
            yield sub_node
        
    def traverse_backward(self, node=None):
        if node is None:
            return   
      
        for sub_node in self.traverse_backward(node.next):
            yield sub_node
        
        yield node
    
    def reverse(self):
        #    1 -> 2 -> 3 -> 
        # <- 1 <- 2 <- 3
        # need to keep track a prev_node during moving forward through the list
        prev_node = None
        
        node = self.head
        
        while node:
            next_node = node.next
            node.next = prev_node
            
            prev_node = node
            node = next_node
        
        self.head = prev_node
            
        return self
    
    def reverse_recursive(self, node):
        #    1 -> 2 -> 3 -> 
        # <- 1 <- 2 <- 3
        # we don't have to carry about not loosing links to existing elements - 
        # every element is preserved automatically due to recursion stack,
        # so on each step we always have a pair of node and next_node.
        # All we need to carry about is to start from the end.
        
        next_node = node.next
        
        if next_node is None:
            self.head = node
            return
        
        self.reverse_recursive(next_node)
        
        next_node.next = node
        node.next = None
        
        return self
            
    def __repr__(self):
        values = ', '.join((str(node) for node in self))

        return 'LinkedList({values})'.format(values=values)


if __name__ == '__main__':
    l = LinkedList(1, 2, 3, 6, 'a', 10)

