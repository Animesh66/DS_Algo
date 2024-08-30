class _Node:

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(_Node):

    def __init__(self) -> None:
        self.root = None

    def insert(self, value) -> bool:
        new_node = _Node(value=value)
        # case 1: check if the three is empty or not
        if self.root is None:
            self.root = new_node
            return True
        # case 2: if there are more than one items in the three
        current = self.root
        # compare the new node with current node iteratively until reach the end of the three
        while True:
            # case 1: if the new node to be inserted is equals to the for current node then return none
            if new_node.value == current.value:
                return False
            # case 2: if the new node value is less than the value of the current node then traverse left side and insert the new node on tehe empty spot
            if new_node.value < current.value:
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            # case 3: if the new node value is greater than the value of the current node then traverse right side and insert the new node on an empty spot
            else:
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right

    def contains(self, value) -> bool:
        # if there are items in the three then find the value
        current = self.root
        while current:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def pre_order_traverse(self, root: _Node):
        # This is the solution for pre order traverse using recursion
        # root -> left -> right
        if root is None:  # This is called base condition
            return
        print(root.value)
        self.pre_order_traverse(root.left)
        self.pre_order_traverse(root.right)

    def in_order_traverse(self, root: _Node):
        # This is the solution for in order traverse using recursion
        # left -> root -> right
        if root is None:
            return
        self.in_order_traverse(root.left)
        print(root.value)
        self.in_order_traverse(root.right)

    def post_order_traverse(self, root: _Node):
        # This is the solution for post order traversal using recursion
        # left -> right -> root
        if root is None:
            return
        self.post_order_traverse(root.left)
        self.post_order_traverse(root.right)
        print(root.value)

    def height(self, root: _Node) -> int:
        # case 1: check if the three is empty
        if root is None:
            return -1
        # case 2: set up base condition. if the Node is a leaf node then height is 0.
        if root.left is None and root.right is None:
            return 0
        # case 3: for all other scenarios use recursion to get the height
        return (1 + max(self.height(root.left), self.height(root.right)))

    def find_minimum(self) -> int:
        """
        This test will find the minimum value in a banry search three
        """
        # case 1: when the tree is empty
        if self.root is None:
            return None
        # case 2: when three has item in it
        current = self.root
        last = current
        while current is not None:
            last = current
            current = current.left
        return last.value

    def find_minimum_in_binary_three(self, root: _Node | int) -> _Node:
        """
        This method will find the minimum value in a binary search three
        """
        # create base condition for recustion when the node is a leaf node then we will terminate search
        if root.left is None and root.right is None:
            return root.value
        left = self.find_minimum_in_binary_three(root.left)
        right = self.find_minimum_in_binary_three(root.right)
        min_value = min(min(left, right), root.value)
        return min_value


bst = BinarySearchTree()
bst.insert(10)
bst.insert(7)
bst.insert(13)
bst.insert(5)
bst.insert(8)
bst.insert(11)
bst.insert(17)
# bst.insert(2)
print(bst.find_minimum_in_binary_three(bst.root))
