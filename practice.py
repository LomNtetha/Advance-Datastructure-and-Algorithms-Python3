def maxmum_activities(start,end):

    activities = list(zip(start,end))
    print(activities)

    activities.sort(key=lambda x :x[1])

    print(f"sorted: {activities}")


    last_end = activities[0][1]
    count = 1
    selected_activities = [0]

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]


act = maxmum_activities(start, end)