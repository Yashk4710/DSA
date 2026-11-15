
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BST:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        else:
            print("Duplicate not allowed!")
        return root

    def search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        if data < root.data:
            return self.search(root.left, data)
        return self.search(root.right, data)

    def delete(self, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            t = root.right
            while t.left:
                t = t.left
            root.data = t.data
            root.right = self.delete(root.right, t.data)
        return root

    # Traversals
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Depth
    def depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    # Mirror
    def mirror(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.mirror(root.left)
            self.mirror(root.right)

    # Copy
    def copy(self, root):
        if root is None:
            return None
        n = Node(root.data)
        n.left = self.copy(root.left)
        n.right = self.copy(root.right)
        return n

    # Parent and Children
    def parents(self, root):
        if root:
            if root.left or root.right:
                print(root.data, "->",
                      root.left.data if root.left else "-",
                      root.right.data if root.right else "-")
            self.parents(root.left)
            self.parents(root.right)

    # Leaf nodes
    def leaves(self, root):
        if root:
            if root.left is None and root.right is None:
                print(root.data, end=" ")
            self.leaves(root.left)
            self.leaves(root.right)

    # Level-wise
    def level(self, root):
        q = [root] if root else []
        while q:
            n = q.pop(0)
            print(n.data, end=" ")
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

    # Vertical representation
    def vertical(self, root, space=0):
        if root:
            self.vertical(root.right, space + 5)
            print(" " * space + str(root.data))
            self.vertical(root.left, space + 5)


# Main
b = BST()
root = None

while True:
    print("\n--- BINARY SEARCH TREE ---")
    print("1.Insert")
    print("2.Delete")
    print("3.Search")
    print("4.Traversal")
    print("5.Depth")
    print("6.Mirror")
    print("7.Copy")
    print("8.Parents with Children")
    print("9.Leaf Nodes")
    print("10.Level Wise")
    print("11.Vertical Representation")
    print("12.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        root = b.insert(root, int(input("Enter value: ")))

    elif ch == 2:
        root = b.delete(root, int(input("Enter value: ")))

    elif ch == 3:
        x = int(input("Enter value: "))
        print("Found" if b.search(root, x) else "Not Found")

    elif ch == 4:
        print("Inorder: ", end="")
        b.inorder(root)
        print("\nPreorder: ", end="")
        b.preorder(root)
        print("\nPostorder: ", end="")
        b.postorder(root)

    elif ch == 5:
        print("Depth =", b.depth(root))

    elif ch == 6:
        b.mirror(root)
        print("Mirror image created!")

    elif ch == 7:
        copyroot = b.copy(root)
        print("Tree copied successfully!")

    elif ch == 8:
        print("Parent -> Left Right")
        b.parents(root)

    elif ch == 9:
        print("Leaf nodes: ", end="")
        b.leaves(root)

    elif ch == 10:
        print("Level wise: ", end="")
        b.level(root)

    elif ch == 11:
        print("\nVertical Tree:")
        b.vertical(root)

    elif ch == 12:
        print("Program ended!")
        break

    else:
        print("Invalid choice!")
