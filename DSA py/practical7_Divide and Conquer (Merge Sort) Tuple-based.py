
def merge_sort(orders):
    # Base case
    if len(orders) <= 1:
        return orders

    # Divide the list into two halves
    mid = len(orders) // 2
    left = merge_sort(orders[:mid])
    right = merge_sort(orders[mid:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    # Compare delivery times and add smaller one
    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining orders
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Input: Order ID and estimated delivery time in minutes
orders = [
    ("ORD101", 45),
    ("ORD102", 20),
    ("ORD103", 35),
    ("ORD104", 10),
    ("ORD105", 60),
    ("ORD106", 25),
    ("ORD107", 15),
    ("ORD108", 40)
]

print("Original Orders:")
for order_id, time in orders:
    print(order_id, "-", time, "minutes")

# Sort orders using Merge Sort
sorted_orders = merge_sort(orders)

print("\nOrders Sorted by Delivery Time:")
for order_id, time in sorted_orders:
    print(order_id, "-", time, "minutes")
