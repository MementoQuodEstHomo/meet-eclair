from bst import binary_search_tree


def main():
    print "1. Only root."
    bst_1 = binary_search_tree.BinarySearchTree(1)
    assert (bst_1.root.key == 1)

    print "2. Root with 1 leaf."
    bst_2 = binary_search_tree.BinarySearchTree(2, 1)
    assert (bst_2.root.left_leaf.key == 1)

    print "3. Insert key."
    bst_3 = binary_search_tree.BinarySearchTree(1)
    bst_3.insert_key(2)
    assert (bst_3.root.right_leaf.key == 2)

    print "4. Find node"
    bst_4 = binary_search_tree.BinarySearchTree(2, 1, 3)
    assert (bst_4.find_node_with_key(2).key == 2)

    print "5. Get node with max key"
    bst_5 = binary_search_tree.BinarySearchTree(2, 1, 3)
    assert (bst_5.get_max_key_node().key == 3)

    print "6. Get node with min key"
    bst_6 = binary_search_tree.BinarySearchTree(2, 1, 3)
    assert (bst_6.get_min_key_node().key == 1)

    print "7. Delete leaf"
    bst_7 = binary_search_tree.BinarySearchTree(2, 1, 3)
    bst_7.delete_node_by_key(3)
    assert (bst_7.root.right_leaf is None)

    print "8. Delete node with one leaf"
    bst_8 = binary_search_tree.BinarySearchTree(2, 1, 3, 4)
    bst_8.delete_node_by_key(3)
    assert (bst_8.root.right_leaf.key == 4)

    print "9. Delete node with 2 leaves"
    bst_9 = binary_search_tree.BinarySearchTree(2, 1, 3, 4)
    bst_9.delete_node_by_key(2)
    assert (bst_9.root.left_leaf.key == 1)
    assert (bst_9.root.right_leaf.key == 4)

    print "10. Find not existing node"
    bst_10 = binary_search_tree.BinarySearchTree(2, 1, 3)
    assert (bst_10.find_node_with_key(0) is None)

    print "11. Delete not existing node"
    bst_11 = binary_search_tree.BinarySearchTree(2, 1, 3, 4)
    assert (bst_11.delete_node_by_key(100) is False)

    print "12. Delete node. Tree with no root."
    bst_12 = binary_search_tree.BinarySearchTree()
    assert (bst_12.delete_node_by_key(100) is False)

    print "13. In-order traversal."
    bst_13 = binary_search_tree.BinarySearchTree(2, 1, 3, 4)
    bst_13.inorder_traversal()

    print "14. Pre-order traversal."
    bst_14 = binary_search_tree.BinarySearchTree(2, 1, 3, 4)
    bst_14.preorder_traversal()

    print "15. Post-order traversal."
    bst_15 = binary_search_tree.BinarySearchTree(2, 1, 3, 4)
    bst_15.postorder_traversal()


if __name__ == '__main__':
    main()
