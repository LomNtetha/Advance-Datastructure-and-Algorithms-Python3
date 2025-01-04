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


def fraction_capacity(weights,values,capacity):

    zip_items = zip(values,weights)

    zip_fractions_items = ((v/w,w) for v, w in zip_items)

    items = sorted(zip_fractions_items, reverse=True)

    total_value = 0.0

    for items_per_value,weight in items:

        if capacity >= weight:
            total_value+=items_per_value*weight
            capacity -= weight
        else:
            total_value+= items_per_value * capacity
            break

    return total_value


weights = [10, 20, 30]  # Weights of items
values = [60, 100, 120]  # Values of items
capacity = 50  # Capacity of the knapsack
total = fraction_capacity(weights,values,capacity)

print(f"Here is the return value {total}")