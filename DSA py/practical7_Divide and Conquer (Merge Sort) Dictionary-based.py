
def merge_sort(orders):
    """
    Sorts a list of online orders in ascending order of delivery time.
    """

    # Base case
    if len(orders) <= 1:
        return orders

    # Divide
    mid = len(orders) // 2
    left_half = orders[:mid]
    right_half = orders[mid:]

    # Conquer
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Combine
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    Merges two sorted lists based on delivery_time.
    """

    sorted_list = []
    i = j = 0

    # Compare elements
    while i < len(left) and j < len(right):
        if left[i]["delivery_time"] <= right[j]["delivery_time"]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


# Driver Code
if __name__ == "__main__":

    online_orders = [
        {"order_id": "ORD-101", "item": "Pizza", "delivery_time": 45},
        {"order_id": "ORD-102", "item": "Burger", "delivery_time": 20},
        {"order_id": "ORD-103", "item": "Sushi", "delivery_time": 35},
        {"order_id": "ORD-104", "item": "Tacos", "delivery_time": 15},
        {"order_id": "ORD-105", "item": "Pasta", "delivery_time": 30},
    ]

    print("Unsorted Orders:")

    for order in online_orders:
        print(f"ID: {order['order_id']} | Item: {order['item']} | Delivery Time: {order['delivery_time']} mins")

    # Sort orders
    prioritized_orders = merge_sort(online_orders)

    print("\nPrioritized Orders (Sorted by Delivery Time):")

    for order in prioritized_orders:
        print(f"ID: {order['order_id']} | Item: {order['item']} | Delivery Time: {order['delivery_time']} mins")
