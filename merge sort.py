
def merge_sort(orders):
    if len(orders) > 1:
        mid = len(orders) // 2

        left = orders[:mid]
        right = orders[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orders[k] = left[i]
                i += 1
            else:
                orders[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orders[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orders[k] = right[j]
            j += 1
            k += 1


# Main Program
n = int(input("Enter number of orders: "))

orders = []

for i in range(n):
    time = int(input("Enter delivery time of order " + str(i + 1) + ": "))
    orders.append(time)

print("Original delivery times:", orders)

merge_sort(orders)

print("Sorted delivery times:", orders)
