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
