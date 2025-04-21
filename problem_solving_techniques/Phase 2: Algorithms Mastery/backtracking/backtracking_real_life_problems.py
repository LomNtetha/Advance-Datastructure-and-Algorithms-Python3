
"""
Problem 1: Inventory Management
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

    result = []
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

   
    backtrack(0, target, [])
    return result

# Example Usage
items = [2, 3, 5]
target = 8
print(inventory_combinations(items, target))
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

"""
Problem 2: Team Formation
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

"""
5. Seating Arrangement in a Conference Hall
Problem Statement:
Given a hall with a specific number of seats, assign attendees while ensuring that certain attendees do not sit next to each other.

Example Input:
attendees = ["Alice", "Bob", "Charlie"]
restrictions = [("Alice", "Bob")]  # Cannot sit together
seats = 3
"""
def valid(arrangement, restrictions):
    for (a, b) in restrictions:
        if a in arrangement and b in arrangement and abs(arrangement.index(a) - arrangement.index(b)) == 1:
            return False
    return True

def arrange_seats(attendees, restrictions, arrangement=[]):
    if len(arrangement) == len(attendees):
        return arrangement if valid(arrangement, restrictions) else None

    for attendee in attendees:
        if attendee not in arrangement:
            arrangement.append(attendee)

            result = arrange_seats(attendees, restrictions, arrangement)
            if result:
                return result

            arrangement.pop()  # Backtrack

    return None

attendees = ["Alice", "Bob", "Charlie"]
restrictions = [("Alice", "Bob")]
seats = 3

print(arrange_seats(attendees, restrictions))
# Time Complexity:
# Worst Case: 
# O(N!), where N is the number of attendees.
# Space Complexity:
# O(N) due to recursion depth.
