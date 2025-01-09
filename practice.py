def max_denominations(denominations,amount):

    denominations.sort(reverse=True)

    coin_used = []
    number_coin = 0

    for coin in denominations:
        if coin <= amount:
            coin_used.append(coin)
            number_coin += 1
            amount -= coin
    return coin_used, number_coin
denominations = [25, 10, 5, 16,1]
# Example usage
amount = 41  # Target amount in cents

c, n = max_denominations(denominations, amount)

print(f"here is the coin used: {c}")
print (f"here is the number of coins {n}")


def max_activities(start,end):

    activities = list(zip(start,end))

    activities.sort(key=lambda x:x[1])

    selected_activities = [0]
    last_end_time = activities[0][1]
    count = 1

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            selected_activities.append(i)
            count+=1
            last_end_time = activities[i][1]
    return count, selected_activities
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

s,e = max_activities(start,end)
print(s)
print(e)

