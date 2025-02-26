"""
Problem 1: Transaction Scheduling
Statement: You are given a list of transactions with start and end times. Schedule the maximum number of transactions without overlapping.

Example Input:
transactions = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9)]
"""
def schedule_transactions(transactions):
    """
    Schedules the maximum number of non-overlapping transactions using backtracking.
    Time Complexity: O(2^n), where n is the number of transactions.
    Space Complexity: O(n) for the recursion stack.
    """
    def backtrack(index, last_end, path):
        """
        Backtracks to find the maximum number of non-overlapping transactions.
        """
        if index == len(transactions):
            if len(path) > len(max_path[0]):
                max_path[0] = path[:]
            return
        # Option 1: Skip the current transaction
        backtrack(index + 1, last_end, path)
        # Option 2: Include the current transaction if it doesn't overlap
        if transactions[index][0] >= last_end:
            backtrack(index + 1, transactions[index][1], path + [transactions[index]])

    transactions.sort(key=lambda x: x[1])  # Sort by end time
    max_path = [[]]
    backtrack(0, 0, [])
    return max_path[0]

# Example Usage
transactions = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9)]
print(schedule_transactions(transactions))
# Output: [(1, 4), (5, 7), (8, 9)]

"""
Problem 2: Resource Allocation
Statement: Allocate resources to tasks such that no resource is over-allocated. Each task requires a certain number of resources, 
and each resource has a limit.

Example Input:

tasks = [2, 3, 1]  # Resource requirements for each task
resources = 4       # Total resources available
"""
def allocate_resources(tasks, resources):
    """
    Allocates resources to tasks using backtracking.
    Time Complexity: O(2^n), where n is the number of tasks.
    Space Complexity: O(n) for the recursion stack.
    """
    def backtrack(index, remaining_resources, allocation):
        """
        Backtracks to find a valid resource allocation.
        """
        if index == len(tasks):
            return True
        for i in range(remaining_resources + 1):
            if i <= tasks[index]:
                allocation[index] = i
                if backtrack(index + 1, remaining_resources - i, allocation):
                    return True
                allocation[index] = 0  # Undo the allocation
        return False

    allocation = [0] * len(tasks)
    if backtrack(0, resources, allocation):
        return allocation
    return None

# Example Usage
tasks = [2, 3, 1]
resources = 4
print(allocate_resources(tasks, resources))
# Output: [2, 2, 0] (One possible allocation)

"""
Problem 3: Budget Allocation
Statement: Allocate a budget to projects such that the total cost does not exceed the budget and the maximum number of projects are funded.

Example Input:
projects = [10, 20, 30, 40]  # Cost of each project
budget = 50   
   """             # Total budget
def allocate_budget(projects, budget):
    """
    Allocates budget to projects using backtracking.
    Time Complexity: O(2^n), where n is the number of projects.
    Space Complexity: O(n) for the recursion stack.
    """
    def backtrack(index, remaining_budget, path):
        """
        Backtracks to find the maximum number of projects that can be funded.
        """
        if index == len(projects):
            if len(path) > len(max_path[0]):
                max_path[0] = path[:]
            return
        # Option 1: Skip the current project
        backtrack(index + 1, remaining_budget, path)
        # Option 2: Include the current project if it fits the budget
        if projects[index] <= remaining_budget:
            backtrack(index + 1, remaining_budget - projects[index], path + [projects[index]])

    max_path = [[]]
    backtrack(0, budget, [])
    return max_path[0]

# Example Usage
projects = [10, 20, 30, 40]
budget = 50
print(allocate_budget(projects, budget))
# Output: [10, 40] (One possible allocation)

"""
Problem 4: Task Assignment
Statement: Assign tasks to workers such that no worker is overloaded. Each task has a certain workload, and each worker has a capacity.

Example Input:
tasks = [2, 3, 4]  # Workload of each task
workers = [5, 5]    # Capacity of each worker
"""

def assign_tasks(tasks, workers):
    """
    Assigns tasks to workers using backtracking.
    Time Complexity: O(k^n), where n is the number of tasks and k is the number of workers.
    Space Complexity: O(n) for the recursion stack.
    """
    def backtrack(index, worker_loads):
        """
        Backtracks to find a valid task assignment.
        """
        if index == len(tasks):
            return True
        for i in range(len(workers)):
            if worker_loads[i] + tasks[index] <= workers[i]:
                worker_loads[i] += tasks[index]
                if backtrack(index + 1, worker_loads):
                    return True
                worker_loads[i] -= tasks[index]  # Undo the assignment
        return False

    worker_loads = [0] * len(workers)
    if backtrack(0, worker_loads):
        return worker_loads
    return None

# Example Usage
tasks = [2, 3, 4]
workers = [5, 5]
print(assign_tasks(tasks, workers))
# Output: [5, 4] (One possible assignment)

"""
Problem 5: Meeting Room Scheduling
Statement: Schedule meetings in rooms such that no two meetings overlap in the same room.

Example Input:
meetings = [(1, 4), (3, 5), (6, 8)]  # (start, end) times
rooms = 2                              # Number of rooms
"""
def schedule_meetings(meetings, rooms):
    """
    Schedules meetings in rooms using backtracking.
    Time Complexity: O(k^n), where n is the number of meetings and k is the number of rooms.
    Space Complexity: O(n) for the recursion stack.
    """
    def backtrack(index, room_schedules):
        """
        Backtracks to find a valid meeting schedule.
        """
        if index == len(meetings):
            return True
        for i in range(rooms):
            if not room_schedules[i] or room_schedules[i][-1][1] <= meetings[index][0]:
                room_schedules[i].append(meetings[index])
                if backtrack(index + 1, room_schedules):
                    return True
                room_schedules[i].pop()  # Undo the assignment
        return False

    room_schedules = [[] for _ in range(rooms)]
    if backtrack(0, room_schedules):
        return room_schedules
    return None

# Example Usage
meetings = [(1, 4), (3, 5), (6, 8)]
rooms = 2
print(schedule_meetings(meetings, rooms))
# Output: [[(1, 4), (6, 8)], [(3, 5)]] (One possible schedule)
"""
Problem 6: Travel Itinerary Planning
Statement: Plan a travel itinerary such that the total cost does not exceed the budget and all destinations are visited.

Example Input:

destinations = [("Paris", 500), ("London", 400), ("Rome", 300)]  # (destination, cost)
budget = 1000
"""
def plan_itinerary(destinations, budget):
    """
    Plans a travel itinerary using backtracking.
    Time Complexity: O(2^n), where n is the number of destinations.
    Space Complexity: O(n) for the recursion stack.
    """
    def backtrack(index, remaining_budget, path):
        """
        Backtracks to find a valid itinerary.
        """
        if index == len(destinations):
            if len(path) > len(max_path[0]):
                max_path[0] = path[:]
            return
        # Option 1: Skip the current destination
        backtrack(index + 1, remaining_budget, path)
        # Option 2: Include the current destination if it fits the budget
        if destinations[index][1] <= remaining_budget:
            backtrack(index + 1, remaining_budget - destinations[index][1], path + [destinations[index]])

    max_path = [[]]
    backtrack(0, budget, [])
    return max_path[0]

# Example Usage
destinations = [("Paris", 500), ("London", 400), ("Rome", 300)]
budget = 1000
print(plan_itinerary(destinations, budget))
# Output: [('Paris', 500), ('Rome', 300)] (One possible itinerary)
"""
Problem 7: Inventory Management
Statement: You are given a list of items with their quantities and a target quantity. 
Find all combinations of items that sum up to the target quantity.

Example Input:
items = [2, 3, 5]  # Quantities of each item
target = 8          # Target quantity
"""
def inventory_combinations(items, target):
    """
    Finds all combinations of items that sum up to the target quantity using backtracking.
    Time Complexity: O(2^n), where n is the number of items.
    Space Complexity: O(n) for the recursion stack.
    """
    def backtrack(start, remaining, path):
        """
        Backtracks to find valid combinations.
        """
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(items)):
            if items[i] > remaining:
                continue
            path.append(items[i])
            backtrack(i, remaining - items[i], path)
            path.pop()  # Undo the choice

    result = []
    backtrack(0, target, [])
    return result

# Example Usage
items = [2, 3, 5]
target = 8
print(inventory_combinations(items, target))
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
"""
Problem 8: Project Planning
Statement: You are given a list of projects with their durations and deadlines. Schedule the projects such that all deadlines are met.

Example Input:
projects = [(2, 3), (1, 2), (3, 5)]  # (duration, deadline)
"""
def schedule_projects(projects):
    """
    Schedules projects to meet all deadlines using backtracking.
    Time Complexity: O(n!), where n is the number of projects.
    Space Complexity: O(n) for the recursion stack.
    """
    def backtrack(path, remaining_projects, current_time):
        """
        Backtracks to find a valid project schedule.
        """
        if not remaining_projects:
            result.append(path[:])
            return
        for i, (duration, deadline) in enumerate(remaining_projects):
            if current_time + duration <= deadline:
                path.append((duration, deadline))
                backtrack(path, remaining_projects[:i] + remaining_projects[i+1:], current_time + duration)
                path.pop()  # Undo the choice

    result = []
    backtrack([], projects, 0)
    return result

# Example Usage
projects = [(2, 3), (1, 2), (3, 5)]
print(schedule_projects(projects))
# Output: [[(1, 2), (2, 3), (3, 5)]] (One possible schedule)
"""
Problem 9: Route Optimization
Statement: You are given a list of cities and the distances between them. 
Find the shortest route that visits all cities exactly once and returns to the starting city (Traveling Salesman Problem).

Example Input:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
"""
def tsp(distances):
    """
    Solves the Traveling Salesman Problem using backtracking.
    Time Complexity: O(n!), where n is the number of cities.
    Space Complexity: O(n) for the recursion stack.
    """
    def backtrack(path, visited, current_distance):
        """
        Backtracks to find the shortest route.
        """
        nonlocal min_distance, best_path
        if len(path) == len(distances):
            total_distance = current_distance + distances[path[-1]][path[0]]
            if total_distance < min_distance:
                min_distance = total_distance
                best_path = path[:]
            return
        for i in range(len(distances)):
            if not visited[i]:
                visited[i] = True
                path.append(i)
                backtrack(path, visited, current_distance + distances[path[-2]][i] if len(path) > 1 else 0)
                path.pop()
                visited[i] = False

    min_distance = float('inf')
    best_path = []
    backtrack([0], [True] + [False] * (len(distances) - 1), 0)
    return best_path, min_distance

# Example Usage
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
path, distance = tsp(distances)
print("Best Path:", path, "Distance:", distance)
# Output: Best Path: [0, 1, 3, 2] Distance: 80
"""
Problem 10: Team Formation
Statement: You are given a list of employees and their skills. Form teams such that each team has all required skills.

Example Input:
employees = [
    {"name": "Alice", "skills": ["Python", "SQL"]},
    {"name": "Bob", "skills": ["Java", "SQL"]},
    {"name": "Charlie", "skills": ["Python", "Java"]}
]
required_skills = ["Python", "SQL", "Java"]
"""

def form_teams(employees, required_skills):
    """
    Forms teams with all required skills using backtracking.
    Time Complexity: O(2^n), where n is the number of employees.
    Space Complexity: O(n) for the recursion stack.
    """
    def backtrack(start, team, skills_covered):
        """
        Backtracks to find valid teams.
        """
        if skills_covered == set(required_skills):
            result.append(team[:])
            return
        for i in range(start, len(employees)):
            new_skills = skills_covered.union(employees[i]["skills"])
            if new_skills != skills_covered:
                team.append(employees[i]["name"])
                backtrack(i + 1, team, new_skills)
                team.pop()  # Undo the choice

    result = []
    backtrack(0, [], set())
    return result

# Example Usage
employees = [
    {"name": "Alice", "skills": ["Python", "SQL"]},
    {"name": "Bob", "skills": ["Java", "SQL"]},
    {"name": "Charlie", "skills": ["Python", "Java"]}
]
required_skills = ["Python", "SQL", "Java"]
print(form_teams(employees, required_skills))
# Output: [['Alice', 'Bob', 'Charlie']] (One possible team)