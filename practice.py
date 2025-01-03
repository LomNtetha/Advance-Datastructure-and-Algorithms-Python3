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