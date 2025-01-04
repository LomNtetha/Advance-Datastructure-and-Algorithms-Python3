from typing import List


def max_activities(start,end):

    activities = list(zip(start,end))

    activities.sort(key=lambda x:x[1])

    last_end = activities[0][1]
    count = 1
    selected_activities = [0]

    for i in range(1, len(activities)):

        if activities[i][0]>= last_end:
            count+=1
            selected_activities.append(i)
            last_end = activities[i][1]

    return count, selected_activities
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

count, selected = max_activities(start, end)

print(f"Number of activities {count}")
print(f"slected activities {selected}")

def fractional_kanapsack(weights,values,capacity):

    zip_items = zip(values,weights)
    zip_items_fractions = ((values/weights,weights)for values,weights in zip_items)

    items = sorted(zip_items_fractions, reverse= True)

    total_value = 0.0

    for item_per_value, weight in items:
        if capacity >= weight:
            total_value += item_per_value * weight
            capacity-=weight
        else:
            total_value += item_per_value*capacity
            break
    return total_value

weights = [10, 20, 30]  # Weights of items
values = [60, 100, 120]  # Values of items
capacity = 50  # Capacity of the knapsack

total_v = fractional_kanapsack(weights,values,capacity)

print(f"here is the Total Value: {total_v}")
def fractional_allocation(costs, returns, budget):
        # Step 1: Zip costs and returns together
        zipped_items = zip(costs, returns)
        
        # Step 2: Calculate return-to-cost ratios and create a list of tuples
        investments = [(r / c, r) for c, r in zipped_items]
        
        # Step 3: Sort investments by ratio in descending order
        investments.sort(reverse=True, key=lambda x: x[0])
        
        total_return = 0.0  # Total return accumulated
        
        # Step 4: Allocate budget
        for ratio, cost in investments:
            if budget >= cost:
                # Take the full investment
                total_return += ratio * cost
                budget -= cost
            else:
                # Take a fractional part of the investment
                total_return += ratio * budget
                break
        
        return total_return

# Example usage
costs = [10000, 20000, 15000]
returns = [15000, 25000, 18000]
budget = 50000

max_return = fractional_allocation(costs, returns, budget)
print(f"Maximum return from the investment: ${max_return:.2f}")