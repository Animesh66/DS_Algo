class _Node:

    def __init__(self, value) -> None:
        self.value: int = value
        self.left: _Node = None
        self.right: _Node = None
        self._height: int = 0


class AVLTree(_Node):

    def __init__(self) -> None:
        self.root: _Node = None

    def __insert(self, root: _Node, value: int) -> _Node:
        # if root value is not set(None) then set the value of root to new node
        if root is None:
            return _Node(value)
        #  case 1: if the value to insert is less than the value of root then insert in left child.
        if value < root.value:
            root.left = self.__insert(root.left, value)
        #  case 2: if the value to insert is greater that the value of the root then insert in right child.
        else:
            root.right = self.__insert(root.right, value)
        # once the child is added we need to set the hight
        root._height = max(self.__height(root.left),
                           self.__height(root.right)) + 1
        root = self.balanced(root)
        return root

    def insert(self, value: int) -> int:
        # here set the value of root in the public insert method
        self.root = self.__insert(self.root, value)

    def __height(self, node: _Node) -> int:
        """
        Helper method to calculate the height
        Args:
            node (_Node): _description_
        """
        # case 1: base condition(if the tree is empty)
        if node is None:
            return -1
        # case 2: if tree is not empty then return the height
        return node._height

    def balanced_factor(self, node: _Node) -> int:
        """
        Calculate the balance factor of the tree
        balanced factor = height(left) tree - height(right) tree
        if the balanced factor is > 1 then the tree is left heavy
        if the balanced factor is < -1 then the tree is right heavy
        Args:
            node (_Node): _description_

        Returns:
            int: _description_
        """
        return 0 if node is None else self.__height(node.left) - self.__height(node.right)

    def is_left_heavy(self, node: _Node) -> bool:
        """
        returns true if the node is left heavy or else returns false
        Args:
            node (_Node): _description_
        """
        return self.balanced_factor(node) > 1

    def is_right_heavy(self, node: _Node) -> bool:
        """
        This method will return true if the balanced factor is right heavy else return false
        Args:
            node (_Node): _description_

        Returns:
            bool: _description_
        """
        return self.balanced_factor(node) < -1

    def balanced(self, node: _Node) -> _Node:
        """
        Returns the rotation required for an AVL tree.
        Args:
            node (_Node): _description_
        """
        if self.is_left_heavy(node):
            # caes 1: if the tree is left heavy tree perform right rotation
            # on root and before left rotation on left child.
            if self.balanced_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # case 2: if the tree is a right heavy tree.
        if self.is_right_heavy(node):
            # case 1: if the balanced factor of the right child of the node is negative
            # case 2: if the balaced factor of the right child of the node is positive
            if self.balanced_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def set_height(self, node: _Node) -> None:
        """
        set the height of a given node.
        """
        node._height = max(self.__height(node.left),
                           self.__height(node.right)) + 1

    def rotate_left(self, node: _Node) -> _Node:
        """
        This method will rotate the given node to left
        """
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        self.set_height(node)
        self.set_height(new_root)

        return new_root

    def rotate_right(self, node: _Node) -> _Node:
        """
        This method will rotate the given node to right
        """
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        self.set_height(node)
        self.set_height(new_root)

        return new_root

    def pre_order_traverse(self, root: _Node):
        # This is the solution for pre order traverse using recursion
        # root -> left -> right
        if root is None:  # This is called base condition
            return
        print(root.value)
        self.pre_order_traverse(root.left)
        self.pre_order_traverse(root.right)


avl_tree = AVLTree()
avl_tree.insert(10)
avl_tree.insert(30)
avl_tree.insert(20)
# avl_tree.insert(5)
# avl_tree.insert(25)
# avl_tree.pre_order_traverse(avl_tree.root)
# print(avl_tree.root._height)
