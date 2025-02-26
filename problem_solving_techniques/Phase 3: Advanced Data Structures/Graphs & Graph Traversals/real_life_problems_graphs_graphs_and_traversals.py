"""
Problem 1: Social Network Friend Recommendation
Problem Statement: Given a social network represented as a graph, recommend friends for a user based on mutual friends. 
If two users are not directly connected but share mutual friends, recommend them as potential friends.

Example Input:
graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Charlie', 'David'],
    'Charlie': ['Alice', 'Bob'],
    'David': ['Bob']
}
"""
from collections import defaultdict, deque

def recommend_friends(graph, user):
    """
    Recommends friends for a user based on mutual friends.
    :param graph: Adjacency list representation of the social network.
    :param user: The user for whom friends are to be recommended.
    :return: List of recommended friends.
    """
    # Dictionary to store the count of mutual friends for recommended friends
    recommended = defaultdict(int)
    # Set to keep track of visited users to avoid revisiting
    visited = set()
    # Queue for BFS traversal
    queue = deque([user])
    # Mark the starting user as visited
    visited.add(user)

    # Perform BFS to explore friends of friends
    while queue:
        current_user = queue.popleft()
        # Iterate through the current user's friends
        for friend in graph.get(current_user, []):
            if friend not in visited:
                # Mark the friend as visited
                visited.add(friend)
                # Add the friend to the queue for further exploration
                queue.append(friend)
                # Check mutual friends of the current friend
                for mutual_friend in graph.get(friend, []):
                    # If the mutual friend is not the user and not already a friend, recommend them
                    if mutual_friend not in visited and mutual_friend not in graph[user]:
                        recommended[mutual_friend] += 1

    # Sort recommended friends by the number of mutual friends (descending order)
    return sorted(recommended.keys(), key=lambda x: recommended[x], reverse=True)

# Example usage
graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Charlie', 'David'],
    'Charlie': ['Alice', 'Bob'],
    'David': ['Bob']
}
print(recommend_friends(graph, 'Alice'))  # Output: ['David']

# Time Complexity: O(V + E), where V is the number of users and E is the number of friendships.
# Space Complexity: O(V), for storing visited nodes and the queue.
"""
Problem 2: Flight Route Planning
Problem Statement: Given a graph of flight routes, find the shortest path (minimum number of stops) between two airports.

Example Input:

graph = {
    'JFK': ['LAX', 'ATL'],
    'LAX': ['JFK', 'ATL'],
    'ATL': ['JFK', 'LAX', 'ORD'],
    'ORD': ['ATL']
}
"""
from collections import deque

def shortest_flight_path(graph, start, end):
    """
    Finds the shortest path (minimum stops) between two airports.
    :param graph: Adjacency list representation of flight routes.
    :param start: Starting airport.
    :param end: Destination airport.
    :return: List representing the shortest path.
    """
    # If the start and end are the same, return the start as the path
    if start == end:
        return [start]

    # Queue for BFS traversal, storing tuples of (current node, path so far)
    queue = deque([(start, [start])])
    # Set to keep track of visited airports
    visited = set()

    # Perform BFS to find the shortest path
    while queue:
        current, path = queue.popleft()
        # Explore neighbors of the current airport
        for neighbor in graph.get(current, []):
            if neighbor == end:
                # If the destination is found, return the complete path
                return path + [neighbor]
            if neighbor not in visited:
                # Mark the neighbor as visited
                visited.add(neighbor)
                # Add the neighbor to the queue with the updated path
                queue.append((neighbor, path + [neighbor]))

    # If no path is found, return None
    return None

# Example usage
graph = {
    'JFK': ['LAX', 'ATL'],
    'LAX': ['JFK', 'ATL'],
    'ATL': ['JFK', 'LAX', 'ORD'],
    'ORD': ['ATL']
}
print(shortest_flight_path(graph, 'JFK', 'ORD'))  # Output: ['JFK', 'ATL', 'ORD']

# Time Complexity: O(V + E), where V is the number of airports and E is the number of routes.
# Space Complexity: O(V), for storing visited nodes and the queue.
"""
Problem 3: Course Prerequisite Scheduling
Problem Statement: Given a list of courses and their prerequisites, determine if it is possible to complete all courses without cyclic dependencies.

Example Input:
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
"""

from collections import defaultdict, deque

def can_finish_courses(num_courses, prerequisites):
    """
    Determines if all courses can be finished given prerequisites.
    :param num_courses: Total number of courses.
    :param prerequisites: List of prerequisite pairs.
    :return: True if possible, False otherwise.
    """
    # Build the graph and in-degree count for each course
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    # Populate the graph and in-degree array
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Initialize a queue with courses that have no prerequisites
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    # Counter to track the number of completed courses
    completed = 0

    # Perform BFS (Kahn's algorithm for topological sorting)
    while queue:
        course = queue.popleft()
        completed += 1
        # Reduce the in-degree of neighboring courses
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            # If a course has no more prerequisites, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all courses are completed, return True
    return completed == num_courses

# Example usage
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(can_finish_courses(4, prerequisites))  # Output: True

# Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
# Space Complexity: O(V + E), for storing the graph and in-degree array.

# Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
# Space Complexity: O(V + E), for storing the graph and in-degree array.
"""
Problem 4: Delivery Route Optimization
Problem Statement: Given a graph representing delivery locations and distances, find the shortest path for a delivery truck 
to visit all locations and return to the starting point.

Example Input:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
"""
from itertools import permutations

def shortest_delivery_route(graph):
    """
    Finds the shortest delivery route visiting all locations and returning to the start.
    :param graph: Adjacency matrix representation of distances.
    :return: Minimum distance and the optimal route.
    """
    n = len(graph)
    # Initialize minimum distance to infinity
    min_distance = float('inf')
    # Variable to store the optimal route
    optimal_route = []

    # Generate all possible permutations of routes
    for route in permutations(range(1, n)):
        current_distance = 0
        current_node = 0
        # Calculate the total distance for the current route
        for next_node in route:
            current_distance += graph[current_node][next_node]
            current_node = next_node
        # Add the distance to return to the starting point
        current_distance += graph[current_node][0]

        # Update the minimum distance and optimal route if a better route is found
        if current_distance < min_distance:
            min_distance = current_distance
            optimal_route = [0] + list(route) + [0]

    return min_distance, optimal_route

# Example usage
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(shortest_delivery_route(graph))  # Output: (80, [0, 1, 3, 2, 0])

# Time Complexity: O((n-1)!), where n is the number of locations.
# Space Complexity: O(n), for storing the optimal route.
"""
Problem 5: Network Packet Routing
Problem Statement: Given a network topology represented as a graph, find the shortest path for a packet to travel 
from a source node to a destination node.

Example Input:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
"""
import heapq

def dijkstra_shortest_path(graph, start, end):
    """
    Finds the shortest path using Dijkstra's algorithm.
    :param graph: Adjacency list representation of the network.
    :param start: Source node.
    :param end: Destination node.
    :return: Shortest distance and path.
    """
    # Initialize distances to infinity for all nodes
    distances = {node: float('inf') for node in graph}
    # Distance to the start node is 0
    distances[start] = 0
    # Priority queue to store (distance, node) pairs
    priority_queue = [(0, start)]
    # Dictionary to store the previous node in the shortest path
    previous_nodes = {node: None for node in graph}

    # Perform Dijkstra's algorithm
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the destination is reached, reconstruct the path
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            return current_distance, path[::-1]

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If a shorter path is found, update the distance and previous node
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                previous_nodes[neighbor] = current_node

    # If no path is found, return infinity and an empty path
    return float('inf'), []

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijkstra_shortest_path(graph, 'A', 'D'))  # Output: (4, ['A', 'B', 'C', 'D'])

# Time Complexity: O((V + E) log V), where V is the number of nodes and E is the number of edges.
# Space Complexity: O(V), for storing distances and the priority queue.
"""
Problem 6: Website Crawling
Problem Statement: Given a starting URL, crawl a website by following all links on the page and build a graph of interconnected pages.

Example Input:
start_url = "https://example.com"
"""
import requests
from bs4 import BeautifulSoup
from collections import defaultdict, deque

def crawl_website(start_url, max_pages=10):
    """
    Crawls a website and builds a graph of interconnected pages.
    :param start_url: The starting URL for crawling.
    :param max_pages: Maximum number of pages to crawl.
    :return: Graph of interconnected pages.
    """
    # Dictionary to store the graph of interconnected pages
    graph = defaultdict(list)
    # Set to keep track of visited URLs to avoid revisiting
    visited = set()
    # Queue for BFS traversal of URLs
    queue = deque([start_url])
    # Mark the starting URL as visited
    visited.add(start_url)

    # Perform BFS to crawl the website
    while queue and len(visited) < max_pages:
        current_url = queue.popleft()
        try:
            # Fetch the content of the current URL
            response = requests.get(current_url)
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find all anchor tags with href attributes (links)
            for link in soup.find_all('a', href=True):
                next_url = link['href']
                # Ensure the URL is absolute and not already visited
                if next_url.startswith('http') and next_url not in visited:
                    # Mark the URL as visited
                    visited.add(next_url)
                    # Add the URL to the queue for further crawling
                    queue.append(next_url)
                    # Add the link to the graph
                    graph[current_url].append(next_url)
        except requests.RequestException:
            # Handle any request errors (e.g., timeout, invalid URL)
            continue

    return graph

# Example usage
start_url = "https://example.com"
print(crawl_website(start_url, max_pages=5))

# Time Complexity: O(N * M), where N is the number of pages and M is the number of links per page.
# Space Complexity: O(N), for storing visited URLs and the graph.
"""
Problem 7: Disease Spread Simulation
Problem Statement: Simulate the spread of a disease in a population represented as a graph, 
where nodes are individuals and edges represent interactions.

Example Input:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
"""

from collections import deque

def simulate_disease_spread(graph, start_node, infection_probability=0.5):
    """
    Simulates the spread of a disease in a population graph.
    :param graph: Adjacency list representation of the population.
    :param start_node: The initially infected individual.
    :param infection_probability: Probability of spreading the disease.
    :return: Set of infected individuals.
    """
    # Set to store infected individuals
    infected = set([start_node])
    # Queue for BFS traversal of the population
    queue = deque([start_node])

    # Perform BFS to simulate disease spread
    while queue:
        current_node = queue.popleft()
        # Iterate through the neighbors of the current individual
        for neighbor in graph.get(current_node, []):
            # If the neighbor is not infected and the infection spreads, infect them
            if neighbor not in infected and random.random() < infection_probability:
                infected.add(neighbor)
                # Add the infected neighbor to the queue for further spreading
                queue.append(neighbor)

    return infected

# Example usage
import random
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
print(simulate_disease_spread(graph, 'A'))  # Output: Random subset of nodes

# Time Complexity: O(V + E), where V is the number of individuals and E is the number of interactions.
# Space Complexity: O(V), for storing infected individuals and the queue.
"""
Problem 8: Power Grid Failure Analysis
Problem Statement: Given a power grid represented as a graph, identify critical nodes whose failure would disconnect the grid.

Example Input:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
"""
def find_critical_nodes(graph):
    """
    Identifies critical nodes in a power grid.
    :param graph: Adjacency list representation of the power grid.
    :return: List of critical nodes.
    """
    def dfs(node, visited):
        """
        Helper function to perform DFS traversal.
        :param node: Current node being visited.
        :param visited: Set to keep track of visited nodes.
        """
        visited.add(node)
        # Explore all neighbors of the current node
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, visited)

    # List to store critical nodes
    critical_nodes = []
    # Iterate through each node in the graph
    for node in graph:
        visited = set()
        # Create a copy of the graph without the current node
        remaining_graph = {n: [neighbor for neighbor in neighbors if neighbor != node] for n, neighbors in graph.items()}
        # Start DFS from the first node in the remaining graph
        start_node = next(iter(remaining_graph))
        dfs(start_node, visited)
        # If not all nodes are visited, the current node is critical
        if len(visited) != len(graph) - 1:
            critical_nodes.append(node)

    return critical_nodes

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
print(find_critical_nodes(graph))  # Output: ['B', 'C']

# Time Complexity: O(V * (V + E)), where V is the number of nodes and E is the number of edges.
# Space Complexity: O(V), for storing visited nodes.
"""
Problem 9: Traffic Light Optimization
Problem Statement: Given a road network represented as a graph, optimize traffic light timings to minimize congestion at intersections.

Example Input:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
"""
from collections import defaultdict, deque

def optimize_traffic_lights(graph):
    """
    Optimizes traffic light timings using graph coloring.
    :param graph: Adjacency list representation of the road network.
    :return: Dictionary of intersections and their assigned colors (timings).
    """
    # Dictionary to store the color (timing) of each intersection
    color = {}
    # Iterate through each intersection in the graph
    for node in graph:
        if node not in color:
            # Initialize a queue for BFS traversal
            queue = deque([node])
            # Assign the first color (0) to the starting intersection
            color[node] = 0
            # Perform BFS to assign colors to all intersections
            while queue:
                current = queue.popleft()
                # Assign alternating colors to neighbors
                for neighbor in graph.get(current, []):
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    # If a conflict is detected, assign a third color (2)
                    elif color[neighbor] == color[current]:
                        color[neighbor] = 2
    return color

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
print(optimize_traffic_lights(graph))  # Output: {'A': 0, 'B': 1, 'C': 1, 'D': 0}

# Time Complexity: O(V + E), where V is the number of intersections and E is the number of roads.
# Space Complexity: O(V), for storing colors and the queue
"""
Problem 10: Recommendation System for Movies
Problem Statement: Given a graph of users and their movie ratings, recommend movies to a user based on what similar users have liked.

Example Input:

graph = {
    'Alice': {'Movie1': 5, 'Movie2': 3},
    'Bob': {'Movie1': 4, 'Movie3': 2},
    'Charlie': {'Movie2': 5, 'Movie3': 4}
}
"""
from collections import defaultdict

def recommend_movies(graph, user):
    """
    Recommends movies to a user based on similar users' preferences.
    :param graph: Adjacency list representation of user-movie ratings.
    :param user: The user for whom movies are to be recommended.
    :return: List of recommended movies.
    """
    # Get the ratings of the target user
    user_ratings = graph.get(user, {})
    # Dictionary to store the recommendation scores for movies
    recommendations = defaultdict(int)

    # Iterate through all other users in the graph
    for other_user, ratings in graph.items():
        if other_user != user:
            # Calculate similarity between the target user and the other user
            similarity = sum(user_ratings.get(movie, 0) * rating for movie, rating in ratings.items())
            # Add weighted ratings to the recommendation scores
            for movie, rating in ratings.items():
                if movie not in user_ratings:
                    recommendations[movie] += similarity * rating

    # Sort recommended movies by their recommendation scores (descending order)
    return sorted(recommendations.keys(), key=lambda x: recommendations[x], reverse=True)

# Example usage
graph = {
    'Alice': {'Movie1': 5, 'Movie2': 3},
    'Bob': {'Movie1': 4, 'Movie3': 2},
    'Charlie': {'Movie2': 5, 'Movie3': 4}
}
print(recommend_movies(graph, 'Alice'))  # Output: ['Movie3']

# Time Complexity: O(U * M), where U is the number of users and M is the number of movies.
# Space Complexity: O(M), for storing recommendations.