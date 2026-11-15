
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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

            temp = root.right

            while temp.left:
                temp = temp.left

            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

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


# Main Program
b = BST()
root = None

while True:
    print("\n--- BINARY SEARCH TREE ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display Traversal")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        val = int(input("Enter value: "))
        root = b.insert(root, val)

    elif ch == 2:
        val = int(input("Enter value: "))
        root = b.delete(root, val)

    elif ch == 3:
        val = int(input("Enter value: "))
        if b.search(root, val):
            print("Element Found")
        else:
            print("Element Not Found")

    elif ch == 4:
        print("Inorder: ", end="")
        b.inorder(root)

        print("\nPreorder: ", end="")
        b.preorder(root)

        print("\nPostorder: ", end="")
        b.postorder(root)
        print()

    elif ch == 5:
        print("Program ended!")
        break

    else:
        print("Invalid choice!")
