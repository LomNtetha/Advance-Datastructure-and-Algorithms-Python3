"""
Problem 1: Social Network Friend Recommendation
Problem Statement
You are given a social network represented as a graph, where each node represents a user, and edges represent friendships between users. 
Your task is to recommend new friends for a given user based on mutual friends. Specifically:

If two users are not directly connected but share mutual friends, recommend them as potential friends.

The recommendation should prioritize users with the most mutual friends.

Example Input
graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Charlie', 'David'],
    'Charlie': ['Alice', 'Bob'],
    'David': ['Bob']
}
Example Output
For the input above, the recommended friends for Alice are:

['David']
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
Problem Statement
You are given a graph representing flight routes between airports. Each node in the graph represents an airport, and edges represent direct flights between airports. Your task is to find the shortest path (minimum number of stops) between two given airports. If there are multiple paths with the same number of stops, any of them can be returned. If no path exists, return None.

Example Input
python
Copy
graph = {
    'JFK': ['LAX', 'ATL'],
    'LAX': ['JFK', 'ATL'],
    'ATL': ['JFK', 'LAX', 'ORD'],
    'ORD': ['ATL']
}
Example Output
For the input above, the shortest path from JFK to ORD is:

['JFK', 'ATL', 'ORD']
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
Problem Statement
You are given a list of courses and their prerequisites. Each course is represented by a unique integer, and the prerequisites are 
given as a list of pairs [a, b], where a is a course that depends on b (i.e., b is a prerequisite for a). 
Your task is to determine if it is possible to complete all courses without encountering any cyclic dependencies. 
If a cycle exists in the prerequisite graph, it means there is a circular dependency, making it impossible to complete all courses.

Example Input
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

Example Output
For the input above, the output is:
True

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
Problem Statement
You are given a graph representing delivery locations and the distances between them. Each node in the graph represents a delivery location, 
and the edges represent the distances between locations. Your task is to find the shortest possible route for a delivery truck to visit all 
locations exactly once and return to the starting point. This problem is known as the Traveling Salesman Problem (TSP).

Example Input
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
Example Output
For the input above, the shortest route is:
(80, [0, 1, 3, 2, 0])
80 is the total distance of the shortest route.

[0, 1, 3, 2, 0] is the sequence of locations visited, starting and ending at location 0.


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
Problem Statement
You are given a network topology represented as a graph, where each node represents a router or a network device, and edges represent 
connections between them with associated weights (e.g., latency, distance, or cost). Your task is to find the shortest path for a packet to 
travel from a source node to a destination node. The shortest path is defined as the path with the minimum total weight.

Example Input
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
Example Output
For the input above, the shortest path from 'A' to 'D' is:

(4, ['A', 'B', 'C', 'D'])
4 is the total weight (cost) of the shortest path.

['A', 'B', 'C', 'D'] is the sequence of nodes in the shortest path.
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
Problem Statement
You are given a starting URL of a website. Your task is to crawl the website by following all the links on the page and build a graph of 
interconnected pages. Each node in the graph represents a webpage, and edges represent hyperlinks from one page to another. T
he goal is to explore the website structure and represent it as a graph.

Example Input

start_url = "https://example.com"
Example Output
For the input above, the output might look like:

{
    'https://example.com': ['https://example.com/about', 'https://example.com/contact'],
    'https://example.com/about': ['https://example.com'],
    'https://example.com/contact': ['https://example.com']
}

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
Problem Statement
You are given a population represented as a graph, where each node represents an individual, and edges represent interactions between individuals. 
Your task is to simulate the spread of a disease through this population. The simulation should start with one or more infected individuals 
and propagate the disease based on interactions. Each interaction has a certain probability of transmitting the disease.

Example Input
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
Example Output
For the input above, starting with 'A' as the infected individual and an infection probability of 0.5, the output might look like:
{'A', 'B', 'C', 'D'}
This means all individuals in the population have been infected.
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
Problem Statement
You are given a road network represented as a graph, where each node represents an intersection, and edges represent roads connecting 
these intersections. Your task is to optimize traffic light timings at each intersection to minimize congestion. The goal is to assign 
traffic light phases (e.g., red, green) to intersections such that no two connected intersections have conflicting green 
lights at the same time. This problem is essentially a graph coloring problem, where each color represents a unique traffic light phase.

Example Input
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
Example Output
For the input above, the optimized traffic light phases might look like:

{'A': 0, 'B': 1, 'C': 1, 'D': 0}
0 and 1 represent two distinct traffic light phases (e.g., 0 = green for north-south traffic, 1 = green for east-west traffic).

Intersections 'A' and 'D' are assigned phase 0, while intersections 'B' and 'C' are assigned phase 1.
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
Problem Statement
You are given a graph representing users and their movie ratings. Each node in the graph represents a user, and the edges 
represent similarity between users based on their movie ratings. Your task is to recommend movies to a target user 
based on the preferences of similar users. Specifically:

If a movie has been highly rated by users similar to the target user but has not been rated by the target user, recommend it.

The recommendation should prioritize movies with the highest weighted ratings from similar users.

Example Input
graph = {
    'Alice': {'Movie1': 5, 'Movie2': 3},
    'Bob': {'Movie1': 4, 'Movie3': 2},
    'Charlie': {'Movie2': 5, 'Movie3': 4}
}
Example Output
For the input above, if the target user is 'Alice', the recommended movies might look like:
['Movie3']
'Movie3' is recommended because it has been rated highly by 'Bob' and 'Charlie', who are similar to 'Alice'.

Explanation
Graph Representation:

The graph is represented as a dictionary where each key is a user, and the value is another dictionary of movie ratings.

For example, 'Alice': {'Movie1': 5, 'Movie2': 3} means Alice has rated 'Movie1' with a score of 5 and 'Movie2' with a score of 3.
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

"""
Problem 11: User Similarity Detection
Problem Statement: Given a graph of users and their movie ratings, determine if two users are similar based on their movie ratings. 
Use Cosine Similarity to calculate the similarity score between two users. If the similarity score is above a certain threshold (e.g., 0.7), 
consider them similar.

Example Input
graph = {
    'Alice': {'Movie1': 5, 'Movie2': 3},
    'Bob': {'Movie1': 4, 'Movie3': 2},
    'Charlie': {'Movie2': 5, 'Movie3': 4}
}

Example Output
For the input above, the similarity between 'Alice' and 'Bob' might look like:

Similarity between Alice and Bob: 0.92
A similarity score of 0.92 indicates that 'Alice' and 'Bob' are highly similar.
"""

import math

def cosine_similarity(user1_ratings, user2_ratings):
    """
    Calculates the cosine similarity between two users based on their movie ratings.
    
    :param user1_ratings: Dictionary of movie ratings for user 1.
    :param user2_ratings: Dictionary of movie ratings for user 2.
    :return: Cosine similarity score between the two users.
    """
    # Find common movies rated by both users
    common_movies = set(user1_ratings.keys()) & set(user2_ratings.keys())
    
    # If there are no common movies, return 0 (no similarity)
    if not common_movies:
        return 0.0
    
    # Calculate the dot product and magnitudes
    dot_product = sum(user1_ratings[movie] * user2_ratings[movie] for movie in common_movies)
    magnitude1 = math.sqrt(sum(user1_ratings[movie] ** 2 for movie in common_movies))
    magnitude2 = math.sqrt(sum(user2_ratings[movie] ** 2 for movie in common_movies))
    
    # Avoid division by zero
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    # Calculate cosine similarity
    similarity = dot_product / (magnitude1 * magnitude2)
    return similarity

def are_users_similar(graph, user1, user2, threshold=0.7):
    """
    Determines if two users are similar based on their movie ratings.
    
    :param graph: Dictionary representing users and their movie ratings.
    :param user1: The first user.
    :param user2: The second user.
    :param threshold: Similarity threshold (default is 0.7).
    :return: True if users are similar, False otherwise.
    """
    # Get the movie ratings for the two users
    user1_ratings = graph.get(user1, {})
    user2_ratings = graph.get(user2, {})
    
    # Calculate cosine similarity
    similarity = cosine_similarity(user1_ratings, user2_ratings)
    
    # Check if the similarity score is above the threshold
    return similarity >= threshold

# Example usage
graph = {
    'Alice': {'Movie1': 5, 'Movie2': 3},
    'Bob': {'Movie1': 4, 'Movie3': 2},
    'Charlie': {'Movie2': 5, 'Movie3': 4}
}

# Check if Alice and Bob are similar
user1 = 'Alice'
user2 = 'Bob'
if are_users_similar(graph, user1, user2):
    print(f"{user1} and {user2} are similar.")
else:
    print(f"{user1} and {user2} are not similar.")

# Output: Alice and Bob are similar.