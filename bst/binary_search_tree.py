class Node(object):
    def __init__(self, parent, key):
        self.parent = parent
        self.key = key
        self.left_leaf = None
        self.right_leaf = None

    def __str__(self):
        return str(self.key)

    def has_left_leaf(self):
        if self.left_leaf is not None:
            return True
        else:
            return False

    def has_right_leaf(self):
        if self.right_leaf is not None:
            return True
        else:
            return False

    def is_leaf(self):
        if self.has_left_leaf() or self.has_right_leaf():
            return False
        else:
            return True

    def is_left_leaf(self):
        if self.parent is not None and self.parent.left_leaf == self:
            return True
        else:
            return False

    def insert_key(self, key):
        if self.key > key:
            if self.has_left_leaf():
                self.left_leaf.insert_key(key)
            else:
                self.left_leaf = Node(self, key)
                return True
        elif self.key < key:
            if self.has_right_leaf():
                self.right_leaf.insert_key(key)
            else:
                self.right_leaf = Node(self, key)
                return True
        else:
            return False

    def find_node_with_key(self, key):
        if self.key > key:
            if self.has_left_leaf():
                return self.left_leaf.find_node_with_key(key)
            else:
                return None
        elif self.key < key:
            if self.has_right_leaf():
                return self.right_leaf.find_node_with_key(key)
            else:
                return None
        else:
            return self

    def get_min_key_node(self):
        if self.has_left_leaf():
            return self.left_leaf.get_min_key_node()
        else:
            return self

    def get_max_key_node(self):
        if self.has_right_leaf():
            return self.right_leaf.get_max_key_node()
        else:
            return self

    def find_successor_node(self):
        successor = None
        if self.has_right_leaf():
            successor = self.right_leaf.get_min_key_node()
        else:
            if self.parent:
                if self.left_leaf is not None:
                    successor = self.parent
                else:
                    self.parent.right_leaf = None
                    successor = self.parent.find_successor_node()
                    self.parent.right_leaf = self
        return successor

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_leaf():
                self.parent.left_leaf = None
            else:
                self.parent.right_leaf = None
        else:
            if self.has_left_leaf():
                if self.is_left_leaf():
                    self.parent.left_leaf = self.left_leaf
                else:
                    self.parent.right_leaf = self.left_leaf
                self.left_leaf.parent = self.parent
            else:
                if self.is_left_leaf():
                    self.parent.left_leaf = self.right_leaf
                else:
                    self.parent.right_leaf = self.right_leaf
                self.right_leaf.parent = self.parent

    def inorder_traversal(self):
        if self.has_left_leaf():
            self.left_leaf.inorder_traversal()
        print self.__str__()
        if self.has_right_leaf():
            self.right_leaf.inorder_traversal()

    def preorder_traversal(self):
        print self.__str__()
        if self.has_left_leaf():
            self.left_leaf.preorder_traversal()
        if self.has_right_leaf():
            self.right_leaf.preorder_traversal()

    def postorder_traversal(self):
        if self.has_left_leaf():
            self.left_leaf.postorder_traversal()
        if self.has_right_leaf():
            self.right_leaf.postorder_traversal()
        print self.__str__()


class BinarySearchTree(object):
    def __init__(self, *args):
        self.root = None
        for key in args:
            self.insert_key(key)

    def is_empty_tree(self):
        if self.root is None:
            return True
        else:
            return False

    def insert_key(self, key):
        if self.is_empty_tree():
            self.root = Node(self, key)
            return True
        else:
            return self.root.insert_key(key)

    def find_node_with_key(self, key):
        if self.is_empty_tree():
            return None
        else:
            return self.root.find_node_with_key(key)

    def get_min_key_node(self):
        if not self.is_empty_tree():
            return self.root.get_min_key_node()

    def get_max_key_node(self):
        if not self.is_empty_tree():
            return self.root.get_max_key_node()

    def delete_node_by_key(self, key):
        if self.is_empty_tree():
            return False

        node_to_delete = self.find_node_with_key(key)
        if node_to_delete is None:
            return False

        if node_to_delete.is_leaf():
            if node_to_delete.parent.left_leaf.key == key:
                node_to_delete.parent.left_leaf = None
            else:
                node_to_delete.parent.right_leaf = None

        elif node_to_delete.left_leaf is None or node_to_delete.right_leaf is None:
            if node_to_delete.has_right_leaf():
                if node_to_delete.parent.left_leaf.key == key:
                    node_to_delete.parent.left_leaf = node_to_delete.right_leaf
                else:
                    node_to_delete.parent.right_leaf = node_to_delete.right_leaf
            else:
                if node_to_delete.parent.left_leaf.key == key:
                    node_to_delete.parent.left_leaf = node_to_delete.left_leaf
                else:
                    node_to_delete.parent.right_leaf = node_to_delete.left_leaf
        else:
            successor_node = node_to_delete.find_successor_node()
            successor_node.splice_out()
            node_to_delete.key = successor_node.key

    def inorder_traversal(self):
        if not self.is_empty_tree():
            self.root.inorder_traversal()

    def preorder_traversal(self):
        if not self.is_empty_tree():
            self.root.preorder_traversal()

    def postorder_traversal(self):
        if not self.is_empty_tree():
            self.root.postorder_traversal()
