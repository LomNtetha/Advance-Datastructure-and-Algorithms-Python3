from typing import List, Tuple


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


def max_platforms_needed(arrival,departure):

    arrival = [time.zfill(5)for time in arrival]
    departure = [time.zfill(5)for time in departure]

    arrival.sort()
    departure.sort()
    i,j = 0,0
    platform_needed = 0
    maximum_platforms = 0
    n = len(arrival)


    while i < n and j < n:

        if arrival[i] < departure[j]:
            platform_needed+=1
            maximum_platforms = max(maximum_platforms, platform_needed)
            i+=1
        else:
            platform_needed-=1
            j+=1
    return maximum_platforms

arrival = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

maxi = max_platforms_needed(arrival,departure)

print(f"Here is the max platfrom required: {maxi}")


def Job_squence_Max_proit(jobs):
    jobs.sort(key=lambda x:x[1], reverse= True)
    maximum_dealine = max(job[0] for job in jobs)
    slots = [-1] * (maximum_dealine + 1)
    total_profit = 0
    for dealine, profit in jobs:
        for j in range(min(dealine,maximum_dealine),0,-1):
            if slots[j]== -1:
                slots[j]=profit
                total_profit+=profit
                break

    return total_profit
jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]
profit = Job_squence_Max_proit(jobs)
print(f"Max Profit {profit}")