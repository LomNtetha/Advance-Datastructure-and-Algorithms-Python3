def make_denominations(denominations,amount):

    denominations.sort(reverse = True)
    list_coin = []
    num_coins = 0

    for coin in denominations:

        if coin <= amount:
            num_coins +=1
            list_coin.append(coin)
            amount -=coin
           

    return list_coin, num_coins

denominations = [25, 16,10, 5, 1]
amount = 41  # Target amount in cents

list_oin, nums_coin = make_denominations(denominations, amount)
print(list_oin)
print(nums_coin)

def maximum_activities(start,end):

    activities = list(zip(start,end))
    activities.sort(key=lambda x:x[1])

    last_end_time = activities[0][1]
    count = 1
    select_activities = [0]

    for i in range(1, len(activities)):

        if activities[i][0] >= last_end_time:
            count+=1

            select_activities.append(i)

            last_end_time = activities[i][1]

    return count, select_activities

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

count, selected_activities = maximum_activities(start,end)
print(f"number of ctivities {count}")
print(f"selected activiies {selected_activities}")