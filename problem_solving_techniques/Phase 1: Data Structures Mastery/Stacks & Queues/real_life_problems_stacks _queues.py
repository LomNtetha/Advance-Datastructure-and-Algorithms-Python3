"""
1. 
Text Editor Undo/Redo (Stack)

📌 Problem Statement:
A simple text editor allows users to perform the following operations:
1. **Write (text)** - Adds new text to the editor.
2. **Undo** - Removes the most recently added text (LIFO - Last In, First Out).
3. **Redo** - Restores the last undone text.

The operations follow a stack-based approach:
- The `undo_stack` stores all the actions (text additions) for undo operations.
- The `redo_stack` stores undone actions, which can be reapplied using redo.
- Any new text input clears the redo stack to maintain consistency.

### Example Usage:
#### Input Operations:

A text editor allows users to type, undo, and redo actions. The undo follows a LIFO (Last In, First Out) structure.
"""
class TextEditor:
    def __init__(self):
        self.text = ""  # Stores the current text content
        self.undo_stack = []  # Stack to track added text for undo operations
        self.redo_stack = []  # Stack to track undone text for redo operations

    def write(self, text):
        """Adds text to the editor and clears the redo stack."""
        self.undo_stack.append(text)  # Save the action in undo stack
        self.redo_stack.clear()  # New action invalidates redo history
        self.text += text  # Append new text
        print(f"Current Text: {self.text}")

    def undo(self):
        """Removes the last added text (LIFO) and stores it in redo stack."""
        if self.undo_stack:
            last_action = self.undo_stack.pop()  # Get the last action
            self.redo_stack.append(last_action)  # Store it in redo stack
            self.text = self.text[:-len(last_action)]  # Remove last added text
            print(f"After Undo: {self.text}")
        else:
            print("Undo stack is empty. Nothing to undo.")

    def redo(self):
        """Restores the last undone text."""
        if self.redo_stack:
            last_undone = self.redo_stack.pop()  # Get last undone text
            self.undo_stack.append(last_undone)  # Push it back to undo stack
            self.text += last_undone  # Restore the text
            print(f"After Redo: {self.text}")
        else:
            print("Redo stack is empty. Nothing to redo.")

    def get_text(self):
        """Returns the current text."""
        return self.text

# Example Usage
def main():
    editor = TextEditor()
    editor.write("Hello ")
    editor.write("World!")
    editor.undo()
    editor.redo()

if __name__ == "__main__":
    main()



# Time Complexity: O(1)
# Space Complexity: O(N)

"""
2. Call Center (Queue)

📌 Problem Statement:
A call center manages incoming calls using a **First In, First Out (FIFO)** approach. 
This ensures that the first caller in the queue is assisted before newer calls.

### Operations:
1. **Receive Call (call_id)** - Adds a call to the queue.
2. **Answer Call** - Removes and returns the first call from the queue.
3. **Get Pending Calls** - Retrieves a list of all calls waiting in the queue.

### Example Usage:
#### Input Operations:
call_center.receive_call("Call 1") call_center.receive_call("Call 2") call_center.receive_call("Call 3") print(call_center.answer_call()) # "Call 1" print(call_center.get_pending_calls()) # ["Call 2", "Call 3"]

#### Output:
Received Call: Call 1 Received Call: Call 2 Received Call: Call 3 Answered Call: Call 1 Pending Calls: ['Call 2', 'Call 3']
"""

from collections import deque

class CallCenter:
    def __init__(self):
        self.queue = deque()  # Queue to store incoming calls

    def receive_call(self, call_id):
        """Adds a call to the queue."""
        self.queue.append(call_id)
        print(f"Received Call: {call_id}")

    def answer_call(self):
        """Answers the oldest call (FIFO) and removes it from the queue."""
        if self.queue:
            answered_call = self.queue.popleft()
            print(f"Answered Call: {answered_call}")
            return answered_call
        print("No calls in queue.")
        return None

    def get_pending_calls(self):
        """Returns a list of pending calls."""
        pending_calls = list(self.queue)
        print(f"Pending Calls: {pending_calls}")
        return pending_calls

# Direct Execution without main() function
call_center = CallCenter()
call_center.receive_call("Call 1")
call_center.receive_call("Call 2")
call_center.receive_call("Call 3")

call_center.answer_call()  # Should remove "Call 1"
call_center.get_pending_calls()  # Should show ["Call 2", "Call 3"]

# Time Complexity: O(1)
# Space Complexity: O(N)
"""
3. Stock Span Problem (Stack)

📌 Problem Statement:
A stock trading system tracks the **span** of a stock, which is defined as the number of consecutive days 
(including today) where the stock price is **less than or equal to** today's price. 
This helps in analyzing stock trends.

### Explanation:
- If today’s price is higher than the previous day's, the span is **increased** by including the previous day's span.
- We use a **stack** to keep track of previous prices and their spans.

### Example Usage:
#### Input:
stock_spanner.next(100) stock_spanner.next(80) stock_spanner.next(60) stock_spanner.next(70) stock_spanner.next(60) stock_spanner.next(75) stock_spanner.next(85)

#### Output:
Stock Price: 100, Span: 1 Stock Price: 80, Span: 1 Stock Price: 60, Span: 1 Stock Price: 70, Span: 2 Stock Price: 60, Span: 1 Stock Price: 75, Span: 4 Stock Price: 85, Span: 6
"""

class StockSpanner:
    def __init__(self):
        self.stack = []  # Stack to store (price, span)

    def next(self, price):
        """
        Returns the span of the stock price.
        The span represents how many consecutive days (including today) 
        the price was less than or equal to the current price.
        """
        span = 1  # Default span is 1 (current day)
        
        # Pop elements from the stack while the top element's price is less than or equal to the current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]  # Add the span of previous lower prices
        
        # Push the current price and calculated span onto the stack
        self.stack.append((price, span))
        
        print(f"Stock Price: {price}, Span: {span}")  # Debug output
        return span

# Direct Execution without main() function
stock_spanner = StockSpanner()
stock_spanner.next(100)  # Output: 1
stock_spanner.next(80)   # Output: 1
stock_spanner.next(60)   # Output: 1
stock_spanner.next(70)   # Output: 2
stock_spanner.next(60)   # Output: 1
stock_spanner.next(75)   # Output: 4
stock_spanner.next(85)   # Output: 6
# Time Complexity: O(N)
# Space Complexity: O(N)

"""
5. Railway Ticket Counter (Queue)

📌 Problem Statement:
At a railway station, passengers are served **on a first-come, first-served basis**.  
This means the **first passenger to arrive gets their ticket processed first** (FIFO: First In, First Out).  

### Operations:
1. **Issue Ticket (passenger_name)** - Adds a passenger to the queue.
2. **Serve Passenger** - Removes and returns the first passenger in the queue.
3. **Get Waiting Passengers** - Returns a list of passengers still waiting.

### Example Usage:
#### Input:
ticket_counter.issue_ticket("Alice") ticket_counter.issue_ticket("Bob") ticket_counter.issue_ticket("Charlie") ticket_counter.serve_passenger() # "Alice" ticket_counter.get_waiting_passengers() # ["Bob", "Charlie"]

#### Output:
Ticket Issued: Alice Ticket Issued: Bob Ticket Issued: Charlie Served Passenger: Alice Waiting Passengers: ['Bob', 'Charlie']
"""

from collections import deque

class TicketCounter:
    def __init__(self):
        self.queue = deque()  # Queue for ticket processing

    def issue_ticket(self, passenger_name):
        """Adds a passenger to the queue for ticket processing."""
        self.queue.append(passenger_name)
        print(f"Ticket Issued: {passenger_name}")

    def serve_passenger(self):
        """Serves the first passenger in line (FIFO) and removes them from the queue."""
        if self.queue:
            served_passenger = self.queue.popleft()
            print(f"Served Passenger: {served_passenger}")
            return served_passenger
        print("No passengers in queue.")
        return None

    def get_waiting_passengers(self):
        """Returns a list of passengers still waiting in the queue."""
        waiting_passengers = list(self.queue)
        print(f"Waiting Passengers: {waiting_passengers}")
        return waiting_passengers

# Direct Execution without main() function
ticket_counter = TicketCounter()
ticket_counter.issue_ticket("Alice")
ticket_counter.issue_ticket("Bob")
ticket_counter.issue_ticket("Charlie")

ticket_counter.serve_passenger()  # Should remove "Alice"
ticket_counter.get_waiting_passengers()  # Should show ["Bob", "Charlie"]

# Time Complexity: O(1)
# Space Complexity: O(N)
"""
5. Car Parking System (Stack)
Problem Statement: 
Car Parking System (Using Stack)
A parking lot follows a Last-In-First-Out (LIFO) approach, meaning that the last car parked must leave first. 
We will simulate this behavior using a stack data structure.

You are required to implement a class ParkingLot that simulates this system. The class should support the following actions:

Park a car: A car can be parked in the lot only if there is enough space. If there is space available, 
the car will be parked and added to the stack.

Leave the parking lot: The last car that was parked must leave first. This can be done by removing the car from the top of the stack. 
If there are no cars in the parking lot, a message should indicate that it's empty.

Requirements:
The parking lot has a specific capacity (maximum number of cars it can hold).
The cars should be represented by their names or identifiers (e.g., "Car1", "Car2").
A stack data structure should be used to manage the parked cars.
"""
class ParkingLot:
    def __init__(self, capacity):
        # Initialize the parking lot with given capacity and an empty stack
        self.stack = []  # Stack to store parked cars
        self.capacity = capacity  # Maximum capacity of the parking lot

    def park(self, car):
        """Parks a car if space is available."""
        if len(self.stack) < self.capacity:
            self.stack.append(car)  # Add the car to the stack (park the car)
            return f"{car} parked"
        return "Parking lot full"  # If parking lot is full, return message

    def leave(self):
        """Removes the last parked car (LIFO behavior)."""
        if self.stack:
            # Remove the last car from the stack and return the message
            return f"{self.stack.pop()} left the parking"
        return "No cars in parking"  # If no cars are in the parking lot, return this message


# Example Input and Output:

# Create a parking lot with a capacity of 3
parking_lot = ParkingLot(3)

# Park 3 cars
print(parking_lot.park("Car1"))  # Output: Car1 parked
print(parking_lot.park("Car2"))  # Output: Car2 parked
print(parking_lot.park("Car3"))  # Output: Car3 parked

# Try to park a 4th car (parking lot full)
print(parking_lot.park("Car4"))  # Output: Parking lot full

# Let the cars leave
print(parking_lot.leave())  # Output: Car3 left the parking
print(parking_lot.leave())  # Output: Car2 left the parking
print(parking_lot.leave())  # Output: Car1 left the parking

# Try to remove a car when parking lot is empty
print(parking_lot.leave())  # Output: No cars in parking


# Time Complexity: O(1)
# Space Complexity: O(N)
"""
6. Browser Back/Forward Navigation (Stack)
📌 Scenario:
A web browser stores visited pages, allowing users to navigate back and forward using stack data structures.

Problem Statement:
When you visit a new page, it should be stored in the back_stack for potential backward navigation.
If you navigate back, the current page should move to the forward_stack and the browser should show the last page visited.
If you navigate forward, the browser should go back to a page from the forward_stack.
"""
class BrowserHistory:
    def __init__(self):
        # Initialize the back and forward stacks, and the current page
        self.back_stack = []  # Stack for back navigation
        self.forward_stack = []  # Stack for forward navigation
        self.current_page = None  # Current page in the browser

    def visit(self, url):
        """Navigates to a new URL."""
        if self.current_page:
            self.back_stack.append(self.current_page)  # Save current page to back stack
        self.forward_stack.clear()  # Clear forward history on new visit
        self.current_page = url  # Set current page to the new URL

    def back(self):
        """Goes back to the previous page."""
        if self.back_stack:
            self.forward_stack.append(self.current_page)  # Save current page to forward stack
            self.current_page = self.back_stack.pop()  # Pop from back stack and set as current page
        return self.current_page  # Return the current page

    def forward(self):
        """Goes forward to the next page."""
        if self.forward_stack:
            self.back_stack.append(self.current_page)  # Save current page to back stack
            self.current_page = self.forward_stack.pop()  # Pop from forward stack and set as current page
        return self.current_page  # Return the current page

# Example Input and Output:

# Create a browser history object
browser_history = BrowserHistory()

# Visiting URLs
browser_history.visit("Page1")
browser_history.visit("Page2")
browser_history.visit("Page3")

print(browser_history.back())  # Output: Page2 (goes back to the previous page)
print(browser_history.back())  # Output: Page1 (goes back to the previous page)
print(browser_history.forward())  # Output: Page2 (goes forward to the next page)
print(browser_history.visit("Page4"))  # Output: None (new page visit clears forward history)
print(browser_history.back())  # Output: Page3 (goes back to the previous page)



# Time Complexity: O(1)
# Space Complexity: O(N)

"""
7.Printer Job Queue (Queue)
A printer processes jobs in FIFO (First-In-First-Out) order, meaning the first job added to the queue is processed first.

Problem Statement:
A queue is used to simulate the order in which printer jobs are processed.
Jobs are added to the queue and processed one by one in the order they arrive
"""

from collections import deque

class PrinterQueue:
    def __init__(self):
        # Initialize the printer queue using deque (double-ended queue)
        self.queue = deque()  # Queue to store print jobs

    def add_job(self, job):
        """Adds a print job to the queue."""
        self.queue.append(job)  # Add the job to the end of the queue

    def print_job(self):
        """Processes the first job in the queue."""
        if self.queue:
            return f"Printing: {self.queue.popleft()}"  # Print the first job and remove from queue
        return "No jobs in queue"  # If no jobs in the queue, return this message

# Example Input and Output:

# Create a printer job queue
printer_queue = PrinterQueue()

# Add jobs to the queue
printer_queue.add_job("Document1")
printer_queue.add_job("Document2")
printer_queue.add_job("Document3")

print(printer_queue.print_job())  # Output: Printing: Document1
print(printer_queue.print_job())  # Output: Printing: Document2
print(printer_queue.print_job())  # Output: Printing: Document3
print(printer_queue.print_job())  # Output: No jobs in queue


# Time Complexity: O(1)
# Space Complexity: O(N)
"""
8. Expression Evaluation (Stack)
📌 Scenario: Mathematical expressions such as 2 + (3 * 5) require correct evaluation of operators and operands, respecting parentheses. For this, we can use stacks to ensure that parentheses and operators are handled correctly in the expression. We will focus on validating whether the parentheses in an expression are balanced before performing actual evaluations.

Given an expression with various types of parentheses (round (), curly {}, and square []), you need to determine if the parentheses are balanced (i.e., every opening parenthesis has a corresponding closing parenthesis, and they are properly nested).

Problem:
Write a function is_balanced(expression) that checks if an expression has balanced parentheses. The expression may contain numbers, operators, and multiple types of parentheses.

Requirements:
Balanced Parentheses: An expression is considered balanced if:

Every opening parenthesis ((, {, [) has a corresponding closing parenthesis (), }, ]).
The parentheses are properly nested, meaning the innermost pair is closed first.
There are no unmatched parentheses.
Input: A string expression containing numbers, operators, and parentheses of any type.

Output: Return True if the parentheses are balanced, otherwise return False.."""


def is_balanced(expression):
    """Checks if an expression has balanced parentheses."""
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

# Example Input and Output:

expression = "2 + (3 * 5)"
print(f"Input Expression: {expression}")
result = is_balanced(expression)
print(f"Is the expression balanced? {result}")  # Output: True

expression = "2 + (3 * 5"
print(f"\nInput Expression: {expression}")
result = is_balanced(expression)
print(f"Is the expression balanced? {result}")  # Output: False

# Time Complexity: O(N)
# Space Complexity: O(N)

"""
9. Task Scheduler (Queue)
A CPU scheduler processes tasks in FIFO (First-In-First-Out) order, meaning the first task to be added is the first to be executed.

Problem Statement:
Use a queue to simulate the scheduling of tasks.
Tasks are added to the queue and executed one by one in the order they arrive.
"""

from collections import deque

class TaskScheduler:
    def __init__(self):
        # Initialize the task queue
        self.queue = deque()

    def add_task(self, task):
        """Adds a task to the queue."""
        self.queue.append(task)  # Add the task to the end of the queue

    def execute_task(self):
        """Executes the first task."""
        if self.queue:
            return f"Executing: {self.queue.popleft()}"  # Execute and remove the first task from the queue
        return "No tasks in queue"  # If no tasks are in the queue, return this message

# Example Input and Output:

# Create a task scheduler object
task_scheduler = TaskScheduler()

# Add tasks to the queue
task_scheduler.add_task("Task1")
task_scheduler.add_task("Task2")
task_scheduler.add_task("Task3")

print(task_scheduler.execute_task())  # Output: Executing: Task1
print(task_scheduler.execute_task())  # Output: Executing: Task2
print(task_scheduler.execute_task())  # Output: Executing: Task3
print(task_scheduler.execute_task())  # Output: No tasks in queue
