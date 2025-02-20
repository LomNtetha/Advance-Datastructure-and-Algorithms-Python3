def maximum_activities(start,end):
    activities = list(zip(start,end))

    activities.sort(key=lambda x:x[1])

    last_end_time = activities[0][1]
    print(last_end_time)
    selected_activities = [activities[0]]
    print(selected_activities)
    count = 1

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            count += 1
            selected_activities.append(activities[i])
            last_end_time = activities[i][1]

    return count, selected_activities
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

c,s = maximum_activities(start, end)

print(c)
print(s)


def kanapsack_fractions(weights,values,capacity):

    items = zip(values,weights)

    items_ratios = [(v/w,w )for v,w in items]

    sort_items = sorted(items_ratios, reverse=True)

    total_value = 0.0

    for item_weight, weight in sort_items:

        if capacity >= weight:
            total_value += item_weight * weight
            capacity -= weight

        else:
            total_value += item_weight * capacity
            break

    return total_value
    
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

t = kanapsack_fractions(weights,values,capacity)

print(t)