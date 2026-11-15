
def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_profit = 0

    for weight, profit in items:
        if capacity >= weight:
            capacity -= weight
            total_profit += profit
        else:
            fraction = capacity / weight
            total_profit += profit * fraction
            capacity = 0
            break

    return total_profit


# Main Program
n = int(input("Enter number of orders: "))

items = []

for i in range(n):
    weight = float(input("Enter weight of order " + str(i + 1) + ": "))
    profit = float(input("Enter profit of order " + str(i + 1) + ": "))
    items.append((weight, profit))

capacity = float(input("Enter maximum capacity: "))

max_profit = fractional_knapsack(capacity, items)

print("Maximum Profit =", max_profit)
