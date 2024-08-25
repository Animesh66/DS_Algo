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


bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)
print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
