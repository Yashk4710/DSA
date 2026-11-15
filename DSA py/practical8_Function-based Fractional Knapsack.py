# Fractional Knapsack using Greedy Algorithm

def fractional_knapsack(weights, profits, capacity):
    n = len(weights)
    items = []

    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append((ratio, weights[i], profits[i], i + 1))

    items.sort(reverse=True)

    total_profit = 0
    remaining_capacity = capacity

    print("\nItems selected:")
    print("Item\tWeight\tProfit\tFraction")

    for ratio, weight, profit, item_no in items:

        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            fraction = 1
            total_profit += profit
            remaining_capacity -= weight

        else:
            fraction = remaining_capacity / weight
            total_profit += profit * fraction
            remaining_capacity = 0

        print(f"{item_no}\t{weight}\t{profit}\t{fraction:.2f}")

    print("\nMaximum Profit =", total_profit)


print("FRACTIONAL KNAPSACK PROBLEM")

n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    print(f"\nEnter details for Item {i + 1}:")
    weight = float(input("Weight: "))
    profit = float(input("Profit: "))

    weights.append(weight)
    profits.append(profit)

capacity = float(input("\nEnter truck capacity: "))

fractional_knapsack(weights, profits, capacity)