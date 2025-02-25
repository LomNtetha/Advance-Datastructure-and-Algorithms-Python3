"""
Problem 1: Task Scheduler
Statement: You are given a list of tasks with dependencies represented as a linked list. Each task points to the task that must be completed before it. Implement a task scheduler that processes tasks in the correct order.

Example Input:

# Task A -> Task B -> Task C -> None
# Task A must be completed before Task B, and Task B before Task C.
"""
class TaskNode:
    def __init__(self, name):
        self.name = name
        self.next = None

def schedule_tasks(head):
    """
    Processes tasks in the correct order based on dependencies.
    Time Complexity: O(n), where n is the number of tasks.
    Space Complexity: O(1), as we are using constant extra space.
    """
    current = head
    while current:
        print(f"Processing task: {current.name}")
        current = current.next

# Example Usage
task_a = TaskNode("Task A")
task_b = TaskNode("Task B")
task_c = TaskNode("Task C")
task_a.next = task_b
task_b.next = task_c

schedule_tasks(task_a)
# Output:
# Processing task: Task A
# Processing task: Task B
# Processing task: Task C

"""
Problem 2: Browser History Management
Statement: Implement a browser history using a linked list. Each node represents a visited URL, and you should support operations like visiting a new URL, going back, and going forward.

Example Input:
# Visit: "google.com" -> "facebook.com" -> "youtube.com"
# Go back once, then go forward once.

"""
class BrowserHistoryNode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage):
        self.current = BrowserHistoryNode(homepage)

    def visit(self, url):
        """
        Visits a new URL and updates the browser history.
        Time Complexity: O(1).
        Space Complexity: O(1).
        """
        new_node = BrowserHistoryNode(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node

    def back(self, steps):
        """
        Moves back in the browser history by the given number of steps.
        Time Complexity: O(steps).
        Space Complexity: O(1).
        """
        for _ in range(steps):
            if self.current.prev:
                self.current = self.current.prev

    def forward(self, steps):
        """
        Moves forward in the browser history by the given number of steps.
        Time Complexity: O(steps).
        Space Complexity: O(1).
        """
        for _ in range(steps):
            if self.current.next:
                self.current = self.current.next

    def print_history(self):
        """
        Prints the current browser history.
        Time Complexity: O(n), where n is the number of visited URLs.
        Space Complexity: O(1).
        """
        current = self.current
        while current:
            print(current.url, end=" -> " if current.prev else "")
            current = current.prev
        print()

# Example Usage
history = BrowserHistory("google.com")
history.visit("facebook.com")
history.visit("youtube.com")
history.back(1)
history.forward(1)
history.print_history()  # Output: youtube.com -> facebook.com -> google.com

"""
Problem 3: Music Playlist
Statement: Implement a music playlist using a circular linked list. Each node represents a song, and the playlist should loop back to the first song after the last song.

Example Input:
# Playlist: Song A -> Song B -> Song C -> (loops back to Song A)
"""
class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class MusicPlaylist:
    def __init__(self):
        self.head = None

    def add_song(self, title):
        """
        Adds a song to the playlist.
        Time Complexity: O(n), where n is the number of songs.
        Space Complexity: O(1).
        """
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
            new_song.next = self.head  # Circular link
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_song
            new_song.next = self.head

    def play(self):
        """
        Plays the playlist in a loop.
        Time Complexity: O(n), where n is the number of songs.
        Space Complexity: O(1).
        """
        if not self.head:
            print("Playlist is empty!")
            return
        current = self.head
        while True:
            print(f"Now playing: {current.title}")
            current = current.next
            if current == self.head:
                break

# Example Usage
playlist = MusicPlaylist()
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")
playlist.play()
# Output:
# Now playing: Song A
# Now playing: Song B
# Now playing: Song C

"""
Problem 4: Undo Functionality in a Text Editor
Statement: Implement an undo functionality for a text editor using a linked list. Each node represents a state of the text, and you can undo to the previous state.

Example Input:
# Text states: "Hello" -> "Hello World" -> "Hello World!"
# Undo once.
"""
class TextStateNode:
    def __init__(self, text):
        self.text = text
        self.prev = None

class TextEditor:
    def __init__(self):
        self.current_state = None

    def add_text(self, text):
        """
        Adds a new text state to the editor.
        Time Complexity: O(1).
        Space Complexity: O(1).
        """
        new_state = TextStateNode(text)
        new_state.prev = self.current_state
        self.current_state = new_state

    def undo(self):
        """
        Reverts to the previous text state.
        Time Complexity: O(1).
        Space Complexity: O(1).
        """
        if self.current_state and self.current_state.prev:
            self.current_state = self.current_state.prev

    def get_current_text(self):
        """
        Returns the current text state.
        Time Complexity: O(1).
        Space Complexity: O(1).
        """
        return self.current_state.text if self.current_state else ""

# Example Usage
editor = TextEditor()
editor.add_text("Hello")
editor.add_text("Hello World")
editor.add_text("Hello World!")
editor.undo()
print(editor.get_current_text())  # Output: Hello 

"""
Problem 5: Train Route Management
Statement: Represent a train route as a linked list, where each node is a station. Implement functionality to add a station, remove a station, and display the route.

Example Input:
# Route: Station A -> Station B -> Station C

"""
class StationNode:
    def __init__(self, name):
        self.name = name
        self.next = None

class TrainRoute:
    def __init__(self):
        self.head = None

    def add_station(self, name):
        """
        Adds a station to the train route.
        Time Complexity: O(n), where n is the number of stations.
        Space Complexity: O(1).
        """
        new_station = StationNode(name)
        if not self.head:
            self.head = new_station
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_station

    def remove_station(self, name):
        """
        Removes a station from the train route.
        Time Complexity: O(n), where n is the number of stations.
        Space Complexity: O(1).
        """
        if not self.head:
            return
        if self.head.name == name:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.name == name:
                current.next = current.next.next
                return
            current = current.next

    def display_route(self):
        """
        Displays the train route.
        Time Complexity: O(n), where n is the number of stations.
        Space Complexity: O(1).
        """
        current = self.head
        while current:
            print(current.name, end=" -> " if current.next else "")
            current = current.next
        print()

# Example Usage
route = TrainRoute()
route.add_station("Station A")
route.add_station("Station B")
route.add_station("Station C")
route.display_route()  # Output: Station A -> Station B -> Station C
route.remove_station("Station B")
route.display_route()  # Output: Station A -> Station C

"""
Problem 6: Reservation System
Statement: Implement a reservation system for a restaurant using a linked list. Each node represents a reservation, and you should support operations like adding a reservation, canceling a reservation, and displaying all reservations.

Example Input:
# Reservations: "Alice, 7 PM" -> "Bob, 8 PM" -> "Charlie, 9 PM"
"""
class ReservationNode:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.next = None

class ReservationSystem:
    def __init__(self):
        self.head = None

    def add_reservation(self, name, time):
        """
        Adds a reservation to the system.
        Time Complexity: O(n), where n is the number of reservations.
        Space Complexity: O(1).
        """
        new_reservation = ReservationNode(name, time)
        if not self.head:
            self.head = new_reservation
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_reservation

    def cancel_reservation(self, name):
        """
        Cancels a reservation by name.
        Time Complexity: O(n), where n is the number of reservations.
        Space Complexity: O(1).
        """
        if not self.head:
            return
        if self.head.name == name:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.name == name:
                current.next = current.next.next
                return
            current = current.next

    def display_reservations(self):
        """
        Displays all reservations.
        Time Complexity: O(n), where n is the number of reservations.
        Space Complexity: O(1).
        """
        current = self.head
        while current:
            print(f"{current.name}, {current.time}")
            current = current.next

# Example Usage
system = ReservationSystem()
system.add_reservation("Alice", "7 PM")
system.add_reservation("Bob", "8 PM")
system.add_reservation("Charlie", "9 PM")
system.display_reservations()
# Output:
# Alice, 7 PM
# Bob, 8 PM
# Charlie, 9 PM
system.cancel_reservation("Bob")
system.display_reservations()
# Output:
# Alice, 7 PM
# Charlie, 9 PM
"""
Problem 7: Transaction Log
Statement: Implement a transaction log using a linked list. Each node represents a transaction, and you should support operations like adding a transaction, reversing the log (to undo transactions), and displaying the log.

Example Input:

python
Copy
# Transactions: "Deposit $100" -> "Withdraw $50" -> "Deposit $200"
"""
class TransactionNode:
    def __init__(self, description):
        self.description = description
        self.next = None

class TransactionLog:
    def __init__(self):
        self.head = None

    def add_transaction(self, description):
        """
        Adds a transaction to the log.
        Time Complexity: O(n), where n is the number of transactions.
        Space Complexity: O(1).
        """
        new_transaction = TransactionNode(description)
        if not self.head:
            self.head = new_transaction
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_transaction

    def reverse_log(self):
        """
        Reverses the transaction log (to undo transactions).
        Time Complexity: O(n), where n is the number of transactions.
        Space Complexity: O(1).
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display_log(self):
        """
        Displays the transaction log.
        Time Complexity: O(n), where n is the number of transactions.
        Space Complexity: O(1).
        """
        current = self.head
        while current:
            print(current.description)
            current = current.next

# Example Usage
log = TransactionLog()
log.add_transaction("Deposit $100")
log.add_transaction("Withdraw $50")
log.add_transaction("Deposit $200")
log.display_log()
# Output:
# Deposit $100
# Withdraw $50
# Deposit $200
log.reverse_log()
log.display_log()
# Output:
# Deposit $200
# Withdraw $50
# Deposit $100
"""
Problem 8: Social Media Feed
Statement: Implement a social media feed using a linked list. Each node represents a post, and you should support operations like adding a post, deleting a post, and displaying the feed in reverse chronological order.

Example Input:
# Posts: "Post 1" -> "Post 2" -> "Post 3"
"""
class PostNode:
    def __init__(self, content):
        self.content = content
        self.next = None

class SocialMediaFeed:
    def __init__(self):
        self.head = None

    def add_post(self, content):
        """
        Adds a post to the feed.
        Time Complexity: O(1), as we add at the head.
        Space Complexity: O(1).
        """
        new_post = PostNode(content)
        new_post.next = self.head
        self.head = new_post

    def delete_post(self, content):
        """
        Deletes a post by content.
        Time Complexity: O(n), where n is the number of posts.
        Space Complexity: O(1).
        """
        if not self.head:
            return
        if self.head.content == content:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.content == content:
                current.next = current.next.next
                return
            current = current.next

    def display_feed(self):
        """
        Displays the feed in reverse chronological order.
        Time Complexity: O(n), where n is the number of posts.
        Space Complexity: O(1).
        """
        current = self.head
        while current:
            print(current.content)
            current = current.next

# Example Usage
feed = SocialMediaFeed()
feed.add_post("Post 1")
feed.add_post("Post 2")
feed.add_post("Post 3")
feed.display_feed()
# Output:
# Post 3
# Post 2
# Post 1
feed.delete_post("Post 2")
feed.display_feed()
# Output:
# Post 3
# Post 1

"""
Problem 9: Call Log Management
Statement: Implement a call log using a linked list. Each node represents a call, and you should support operations like adding a call, deleting the oldest call, and displaying the call log.

Example Input:
# Calls: "Call 1" -> "Call 2" -> "Call 3"

"""
class CallNode:
    def __init__(self, details):
        self.details = details
        self.next = None

class CallLog:
    def __init__(self):
        self.head = None

    def add_call(self, details):
        """
        Adds a call to the log.
        Time Complexity: O(n), where n is the number of calls.
        Space Complexity: O(1).
        """
        new_call = CallNode(details)
        if not self.head:
            self.head = new_call
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_call

    def delete_oldest_call(self):
        """
        Deletes the oldest call from the log.
        Time Complexity: O(1).
        Space Complexity: O(1).
        """
        if self.head:
            self.head = self.head.next

    def display_log(self):
        """
        Displays the call log.
        Time Complexity: O(n), where n is the number of calls.
        Space Complexity: O(1).
        """
        current = self.head
        while current:
            print(current.details)
            current = current.next

# Example Usage
log = CallLog()
log.add_call("Call 1")
log.add_call("Call 2")
log.add_call("Call 3")
log.display_log()
# Output:
# Call 1
# Call 2
# Call 3
log.delete_oldest_call()
log.display_log()
# Output:
# Call 2
# Call 3

"""
Problem 10: File System Navigation
Statement: Implement a file system navigation system using a linked list. Each node represents a directory, and you should support operations like navigating to the next directory, going back to the previous directory, and displaying the current path.

Example Input:
# Path: "Home" -> "Documents" -> "Projects"
"""
class DirectoryNode:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

class FileSystem:
    def __init__(self):
        self.current = None

    def navigate_to(self, name):
        """
        Navigates to a new directory.
        Time Complexity: O(1).
        Space Complexity: O(1).
        """
        new_directory = DirectoryNode(name)
        if self.current:
            self.current.next = new_directory
            new_directory.prev = self.current
        self.current = new_directory

    def go_back(self):
        """
        Navigates back to the previous directory.
        Time Complexity: O(1).
        Space Complexity: O(1).
        """
        if self.current and self.current.prev:
            self.current = self.current.prev

    def display_path(self):
        """
        Displays the current path.
        Time Complexity: O(n), where n is the number of directories.
        Space Complexity: O(1).
        """
        path = []
        current = self.current
        while current:
            path.append(current.name)
            current = current.prev
        print(" -> ".join(reversed(path)))

# Example Usage
fs = FileSystem()
fs.navigate_to("Home")
fs.navigate_to("Documents")
fs.navigate_to("Projects")
fs.display_path()  # Output: Home -> Documents -> Projects
fs.go_back()
fs.display_path()  # Output: Home -> Documents