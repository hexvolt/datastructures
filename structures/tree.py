import copy

from collections import Sized, Iterable, Container


class Node(object):
    """
    Represents a single Node of the BinaryTree.
    Each Node has a certain value and two connections with its child Nodes.
    """

    value = None
    left = None
    right = None
    
    def __init__(self, value, left=None, right=None):
        super(Node, self).__init__()

        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        
        self.value = value        
        self.left = left
        self.right = right
    
    @property    
    def is_leaf(self):
        return self.left is None and self.right is None
        
    def __repr__(self):
        return str(self.value)


class BinaryTree(Sized, Iterable, Container):
    """
    A Tree where each Node has only two child-nodes.
    """
    
    root = None
    
    def __contains__(self, value):
        return self.dfs(value) is not None
    
    def __len__(self):
        return self.get_node_count(self.root)
    
    @property
    def height(self):
        return self.get_node_height(self.root)
    
    def get_node_height(self, node):
        
        if (node is None) or (node and node.is_leaf):
            return 0

        return 1 + max(
            self.get_node_height(node.left),
            self.get_node_height(node.right)
        )
        
    def get_node_count(self, node):

        if node is None:
            return 0
        
        return 1 + self.get_node_count(node.left) + \
                   self.get_node_count(node.right)
    
    def bfs(self, value):
        """
        Breadth-First Search
        """

        if value is None:
            raise TypeError("Search value must be not None")

        return self._level_search(value, [self.root])
    
    def _level_search(self, value, level_nodes):
        sub_nodes = []
        
        for node in level_nodes:
            if node is None:
                continue
            
            if node.value == value:
                return node
            else:
                sub_nodes += [node.left, node.right]
        
        return self._level_search(value, sub_nodes) if sub_nodes else None
    
    def dfs(self, value):
        """
        Depth-First Search
        """

        return self._branch_search(value, self.root)
        
    def _branch_search(self, value, subtree):
        if subtree is None:
            return

        if value == subtree.value:
            return subtree
        
        return self._branch_search(value, subtree.left) or \
               self._branch_search(value, subtree.right)
    
    def get_level_nodes(self, level):
        # Breadth-First visiting
        level_nodes = [self.root]
        
        for _ in xrange(level):
            r = []

            for node in level_nodes:
                if node:
                    r += [node.left, node.right]

            level_nodes = copy.copy(r)
        
        return level_nodes
    
    def print_tree(self):
        level_nodes = [self.root]
        
        for level in xrange(self.height + 1):
            r = []
            width = 2**(self.height - level + 1)
            output = ''
            
            for node in level_nodes:
                output += '{0:^{width}}'.format(
                    str(node or ''), width=width, end=' '
                )
                
                r.append(node.left if node else None)
                r.append(node.right if node else None)
            
            level_nodes = copy.copy(r)            
            print(output)            
    
    def preorder_iterative(self):
        stack = []
        node = self.root
        
        while stack or node:    
            if node is not None:
                yield node
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()                
                node = node.right    
    
    def inorder_iterative(self):
        stack = []
        node = self.root
        
        while stack or node:    
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node
                node = node.right
    
    def preorder(self, node):
        if node is None:
            return
        
        yield node
        
        if node.left:
            for subnode in self.preorder(node.left):
                yield subnode
        if node.right:
            for subnode in self.preorder(node.right):
                yield subnode
    
    def inorder(self, node):
        if node is None:
            return
        
        if node.left:
            for subnode in self.inorder(node.left):
                yield subnode
        
        yield node
        
        if node.right:
            for subnode in self.inorder(node.right):
                yield subnode
    
    def postorder(self, node):
        if node is None:
            return
        
        if node.left:
            for subnode in self.postorder(node.left):
                yield subnode
               
        if node.right:
            for subnode in self.postorder(node.right):
                yield subnode
        
        yield node


class BSTree(BinaryTree):
    """
    Binary Search Tree.
    """
            
    def __init__(self, *args):
        super(BSTree, self).__init__()

        for arg in args:
            self.append(arg)
    
    def __iter__(self):
        pass
    
    def __contains__(self, value):
        return self.find(value) is not None
    
    def find(self, value):
        # binary search
        return self._find_in_subtree(value, self.root)
        
    def _find_in_subtree(self, value, subtree):
        if subtree is None:
            return        

        if subtree.value == value:
            return subtree
                
        if value > subtree.value:
            return self._find_in_subtree(value, subtree.right)
        else:
            return self._find_in_subtree(value, subtree.left)
    
    def append(self, value):
        node = Node(value)
        
        if self.root is None:
            self.root = node
        else:
            self._append_to_branch(node, self.root)
    
    def _append_to_branch(self, node, parent):        
        
        if node.value > parent.value:
            # move to the right
            if parent.right:
                self._append_to_branch(node, parent.right)
            else:
                parent.right = node
        else:
            # move to the left
            if parent.left:
                self._append_to_branch(node, parent.left)
            else:
                parent.left = node
        
    def __repr__(self):
        nodes = ', '.join(map(str, self.inorder(self.root)))
        return "BSTree({})".format(nodes)
    

if __name__ == '__main__':
    tree = BSTree(100, 50, 150, 25, 75, 125, 175, 110)

    tree.print_tree()

    print(list(tree.inorder(tree.root)))
    print(list(tree.inorder_iterative()))
    print(list(tree.preorder(tree.root)))
    print(list(tree.preorder_iterative()))
