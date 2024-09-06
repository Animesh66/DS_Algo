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
        if self.is_left_heavy(root):
            print(f"{root.value} is left heavy.")
        if self.is_right_heavy(root):
            print(f"{root.value} is right heavy.")
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

    def pre_order_traverse(self, root: _Node):
        # This is the solution for pre order traverse using recursion
        # root -> left -> right
        if root is None:  # This is called base condition
            return
        print(root.value)
        self.pre_order_traverse(root.left)
        self.pre_order_traverse(root.right)


avl_tree = AVLTree()
avl_tree.insert(30)
avl_tree.insert(20)
avl_tree.insert(10)
# avl_tree.insert(5)
# avl_tree.insert(25)
# avl_tree.pre_order_traverse(avl_tree.root)
# print(avl_tree.root._height)
