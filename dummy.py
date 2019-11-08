def search(root, key):
    """
    search BST for a specefic key
    :param root: root node of BST
    :param key: key to search for
    :return: key if found or None
    """
    if key == root.value or root.value == None:
        return root.value
    elif key < root.value:
        return search(root.left, key)
    else:
        return search(root.right, key)


def insert(root, key):
    """
    insert a key in BST inplace
    :param root: root node of BST
    :param key: value to be inserted
    :return: None
    """
    if root == None:
        root = Node(key)
    else:
        if key > root.value:
            if root.right == None:
                root.right = Node(key)
            else:
                insert(root.right, key)
        elif key < root.value:
            if root.left == None:
                root.left = Node(key)
            else:
                insert(root.left, key)
