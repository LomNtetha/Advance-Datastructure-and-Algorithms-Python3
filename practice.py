from typing import List, Tuple


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


def max_platform_need_train(arrival,departure):
   
   arrival = [time.zfill(5) for time in arrival]
   departure = [time.zfill(5) for time in departure]

   arrival.sort()
   departure.sort()

   i,j = 0,0
   platform_needed = 0
   max_platform = 0
   n = len(arrival)

   while i < n and j < n:
      if arrival[i] < departure[j]:
         platform_needed += 1
         max_platform = max(max_platform, platform_needed)
         i += 1
      else:
         platform_needed -= 1
         j += 1
   return max_platform
         
   
arrival = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

maxplatform = max_platform_need_train(arrival, departure)

print(maxplatform)

def job_sequencing(jobs):

   jobs.sort(key =lambda x:x[1], reverse = True )

   max_dealine = max(job[0] for job in jobs) 

   slots = [-1] *(max_dealine+1)

   total_profit = 0

   for dealine,profit in jobs:

      for j in range (min(dealine,max_dealine),0, -1):
         if slots[j] == -1:
            slots[j] = profit
            total_profit += profit
            break
   return total_profit

jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]

profit_dealine = job_sequencing(jobs)

print(profit_dealine)