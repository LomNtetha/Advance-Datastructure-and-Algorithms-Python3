
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

    Args:
        items (List[int]): List of item quantities available.
        target (int): Desired total quantity to achieve.

    Returns:
        List[List[int]]: All valid combinations of item quantities that sum to the target.
    """

    result = []  # List to store all valid combinations

    def backtrack(start, remaining, path):
        """
        Helper function to perform backtracking.

        Args:
            start (int): Current index in items list to consider (allows reusing the same item).
            remaining (int): Remaining quantity needed to reach the target.
            path (List[int]): Current combination of selected items.
        """
        # Base case: if remaining quantity is zero, a valid combination is found
        if remaining == 0:
            result.append(path[:])  # Add a copy of the current path to the results
            return
        
        # Explore further items starting from the current index
        for i in range(start, len(items)):
            # Skip if item is larger than the remaining needed quantity
            if items[i] > remaining:
                continue

            # Choose the item
            path.append(items[i])
            # Recurse with updated remaining quantity
            backtrack(i, remaining - items[i], path)
            # Undo the choice (backtrack)
            path.pop()

    # Start backtracking from index 0 with full target remaining
    backtrack(0, target, [])

    return result

# === Example Usage ===
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
    Forms teams where the combined skills of the team members cover all required skills
    using a backtracking approach.
    
    Args:
        employees: List of dictionaries, each containing 'name' and 'skills' for an employee.
        required_skills: List of skills that the team must collectively cover.

    Returns:
        A list of teams, where each team is represented as a list of employee names.
    """
    result = []  # List to store all valid teams

    def backtrack(start, team, skills_covered):
        """
        Recursive helper function that explores possible teams using backtracking.

        Args:
            start: The current index in employees list to consider next (to avoid duplicate selections).
            team: List of employee names currently selected in the team.
            skills_covered: Set of skills already covered by the current team.
        """
        # Base case: If all required skills are covered, add the current team to the results
        if skills_covered == set(required_skills):
            result.append(team[:])  # Append a copy of the current team
            return
        
        # Explore further employees starting from the current index
        for i in range(start, len(employees)):
            employee = employees[i]
            
            # Update the set of skills if this employee is added
            new_skills = skills_covered.union(employee["skills"])
            
            # Only proceed if this employee adds at least one new skill
            if new_skills != skills_covered:
                team.append(employee["name"])  # Choose the employee
                backtrack(i + 1, team, new_skills)  # Explore further with the updated team and skills
                team.pop()  # Undo the choice (backtrack) to try other combinations

    # Start backtracking with an empty team and no skills covered
    backtrack(0, [], set())
    return result  # Return all the valid teams found

# === Example Usage ===
employees = [
    {"name": "Alice", "skills": ["Python", "SQL"]},
    {"name": "Bob", "skills": ["Java", "SQL"]},
    {"name": "Charlie", "skills": ["Python", "Java"]}
]
required_skills = ["Python", "SQL", "Java"]

print(form_teams(employees, required_skills))

# Output: [['Alice', 'Bob', 'Charlie']] (One possible team)

#  Time Complexity: O(2^n), where n is the number of employees.
#  Space Complexity: O(n) for the recursion stack.

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
    """
    Checks if the current arrangement satisfies the given restrictions.

    Args:
        arrangement (List[str]): Current seating arrangement.
        restrictions (List[Tuple[str, str]]): Pairs of attendees who should not sit next to each other.

    Returns:
        bool: True if the arrangement is valid, False otherwise.
    """
    for (a, b) in restrictions:
        # Check if both attendees are in the arrangement and they are sitting next to each other
        if a in arrangement and b in arrangement and abs(arrangement.index(a) - arrangement.index(b)) == 1:
            return False  # Invalid if restricted pair sits side-by-side
    return True  # Valid if no restricted pair sits next to each other

def arrange_seats(attendees, restrictions, arrangement=[]):
    """
    Arranges the seats of attendees based on restrictions using backtracking.

    Args:
        attendees (List[str]): List of all attendees.
        restrictions (List[Tuple[str, str]]): Pairs of attendees who cannot sit together.
        arrangement (List[str], optional): Current partial arrangement (defaults to empty list).

    Returns:
        List[str] or None: A valid seating arrangement if possible, otherwise None.
    """
    # Base case: if all attendees are placed
    if len(arrangement) == len(attendees):
        # Check if the full arrangement is valid
        return arrangement if valid(arrangement, restrictions) else None

    # Try placing each attendee who hasn't been placed yet
    for attendee in attendees:
        if attendee not in arrangement:
            # Choose (place attendee in the next seat)
            arrangement.append(attendee)

            # Explore further arrangement recursively
            result = arrange_seats(attendees, restrictions, arrangement)
            if result:
                return result  # If a valid result is found, return it immediately

            # Undo the choice (backtrack)
            arrangement.pop()

    # If no valid arrangement found, return None
    return None

# === Example Usage ===
attendees = ["Alice", "Bob", "Charlie"]
restrictions = [("Alice", "Bob")]  # Alice and Bob cannot sit together
seats = 3

print(arrange_seats(attendees, restrictions))
# Output might be: ['Alice', 'Charlie', 'Bob'] or ['Bob', 'Charlie', 'Alice']

# Time Complexity:
# Worst Case: 
# O(N!), where N is the number of attendees.
# Space Complexity:
# O(N) due to recursion depth.
