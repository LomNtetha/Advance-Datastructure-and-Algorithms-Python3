def denominations_coin(denominations, amount):

    denominations.sort(reverse= True)

    coin_used = []
    coin_count = 0

    for coin in denominations:
     
     if coin <= amount:

        coin_used.append(coin)
        coin_count += 1
        amount-= coin

    return coin_count, coin_used    


denominations = [25, 16,10, 5, 1]

amount = 41

total_denominations, used_coin = denominations_coin(denominations, amount)

print(total_denominations)

print(used_coin)


def max_activities(start, end):
   
   activities = list(zip(start,end))

   activities.sort(key=lambda x:x[1])

   last_end = activities[0][1]
   count = 1
   select_activities = [0]

   for i in range(1, len(activities)):
      if activities[i][0] >= last_end:
         count += 1
         select_activities.append(i)
         last_end = activities[i][1]
   return count, select_activities

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]


num_activities, select_activity = max_activities(start,end)

print(f"Number of activities {num_activities}")

print(f"selected activities {select_activity}")


def fractiona_kanapsack(weights,values, capacity):
   
   items = zip(values,weights)
   

   ratio_items = [(v/w,w) for v, w in items]

   items= sorted(ratio_items,key=lambda x:x[1])

   total_value = 0.0

   for value_per_item, weight in ratio_items:
      if capacity >= weight:
         total_value += value_per_item * weight
         capacity-= weight

      else:
         total_value += value_per_item * capacity
         break
   return total_value




weights = [10, 20, 30]  # Weights of items
values = [60, 100, 120]  # Values of items
capacity = 50

max_value = fractiona_kanapsack(weights,values,capacity)
print(max_value)
