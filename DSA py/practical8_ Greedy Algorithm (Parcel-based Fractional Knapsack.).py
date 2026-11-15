
# Fractional Knapsack using Greedy Algorithm

# Get number of parcels
n = int(input("Enter number of parcels: "))

parcels = []

# Input weight and profit of each parcel
for i in range(n):
    weight = float(input(f"Enter weight of parcel {i + 1}: "))
    profit = float(input(f"Enter profit of parcel {i + 1}: "))

    # Calculate profit/weight ratio
    ratio = profit / weight

    parcels.append([weight, profit, ratio, i + 1])

# Get truck capacity
capacity = float(input("Enter truck capacity: "))

# Sort parcels according to profit/weight ratio
parcels.sort(key=lambda x: x[2], reverse=True)

total_profit = 0

print("\nSelected Parcels:")
print("Parcel\tWeight\tProfit\tFraction")

# Select parcels
for weight, profit, ratio, parcel_no in parcels:

    if capacity == 0:
        break

    if weight <= capacity:
        # Take the complete parcel
        fraction = 1
        total_profit += profit
        capacity -= weight

    else:
        # Take only the required fraction
        fraction = capacity / weight
        total_profit += profit * fraction
        capacity = 0

    print(f"{parcel_no}\t{weight}\t{profit}\t{fraction:.2f}")

# Display maximum profit
print("\nMaximum Profit =", total_profit)
