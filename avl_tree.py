class _Node:

    def __init__(self, value) -> None:
        self.value: int = value
        self.left: _Node = None
        self.right: _Node = None


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

        return root

    def insert(self, value: int) -> int:
        # here set the value of root in the public insert method
        self.root = self.__insert(self.root, value)

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
avl_tree.insert(20)
avl_tree.insert(30)
avl_tree.insert(5)
avl_tree.insert(25)
avl_tree.pre_order_traverse(avl_tree.root)
