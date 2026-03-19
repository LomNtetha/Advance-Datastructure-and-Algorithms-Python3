# 📥 Input (User Messages Sequence)
messages = [
    "Hi",
    "Lomkile",
    "Bread",
    "2"
]
# 📤 Expected Output (Final Step)
{
    "order": {
        "name": "Lomkile",
        "product": "Bread",
        "quantity": 2
    }
}
"""💬 Expected Bot Behavior
Step	User Input	Bot Response"""

# 1	"Hi"	"What is your name?"
# 2	"Lomkile"	"What product do you want?"
# 3	"Bread"	"How many?"
# 4	"2"	Return final JSON

"""🧠 Key Concept

You must store user progress like:"""

{
    "state": "ASK_NAME",
    "data": {}
}
# ✅ Solution
def chatbot():
    # Store state and collected data
    session = {
        "state": "START",
        "data": {}
    }
    
    def handle_message(message):
        state = session["state"]
        
        # Step 1: Ask name
        if state == "START":
            session["state"] = "ASK_NAME"
            return "What is your name?"
        
        elif state == "ASK_NAME":
            session["data"]["name"] = message
            session["state"] = "ASK_PRODUCT"
            return "What product do you want?"
        
        elif state == "ASK_PRODUCT":
            session["data"]["product"] = message
            session["state"] = "ASK_QUANTITY"
            return "How many?"
        
        elif state == "ASK_QUANTITY":
            try:
                qty = int(message)
            except ValueError:
                return "Please enter a valid number"
            
            session["data"]["quantity"] = qty
            
            # Final response
            result = {
                "order": session["data"]
            }
            
            # Reset session (optional)
            session["state"] = "START"
            session["data"] = {}
            
            return result
    
    return handle_message
# 🧪 Example Run
bot = chatbot()

print(bot("Hi"))        # What is your name?
print(bot("Lomkile"))   # What product do you want?
print(bot("Bread"))     # How many?
print(bot("2"))         # Final JSON


"""🧩 Challenge 1: Multi-Step with Validation & Retry
📘 Problem

Build a chatbot that:

Ask for email

Validate email format

If invalid → ask again

Then ask for age

Age must be a number ≥ 18

Return final JSON"""

# 📥 Input
messages = [
    "Hi",
    "wrong-email",
    "user@email.com",
    "15",
    "25"
]
# 📤 Output
{
    "user": {
        "email": "user@email.com",
        "age": 25
    }
}
# ✅ Solution
import re

def chatbot():
    session = {"state": "START", "data": {}}
    
    def is_valid_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)
    
    def handle(msg):
        state = session["state"]
        
        if state == "START":
            session["state"] = "ASK_EMAIL"
            return "Enter your email"
        
        elif state == "ASK_EMAIL":
            if not is_valid_email(msg):
                return "Invalid email, try again"
            session["data"]["email"] = msg
            session["state"] = "ASK_AGE"
            return "Enter your age"
        
        elif state == "ASK_AGE":
            if not msg.isdigit() or int(msg) < 18:
                return "Age must be 18+"
            session["data"]["age"] = int(msg)
            
            result = {"user": session["data"]}
            session["state"] = "START"
            session["data"] = {}
            
            return result
    
    return handle

"""🧩 Challenge 2: Multi-Product Order (Loop Until Done)
📘 Problem

User can add multiple products:

Ask product name

Ask quantity

Ask "add another? (yes/no)"

Loop until "no"
"""
# 📥 Input
messages = [
    "Hi",
    "Bread",
    "2",
    "yes",
    "Milk",
    "1",
    "no"
]
# 📤 Output
{
    "order": [
        {"product": "Bread", "qty": 2},
        {"product": "Milk", "qty": 1}
    ]
}
# ✅ Solution
def chatbot():
    session = {"state": "START", "items": [], "current": {}}
    
    def handle(msg):
        state = session["state"]
        
        if state == "START":
            session["state"] = "ASK_PRODUCT"
            return "Enter product"
        
        elif state == "ASK_PRODUCT":
            session["current"]["product"] = msg
            session["state"] = "ASK_QTY"
            return "Enter quantity"
        
        elif state == "ASK_QTY":
            session["current"]["qty"] = int(msg)
            session["items"].append(session["current"])
            session["current"] = {}
            session["state"] = "ASK_MORE"
            return "Add another? (yes/no)"
        
        elif state == "ASK_MORE":
            if msg.lower() == "yes":
                session["state"] = "ASK_PRODUCT"
                return "Enter product"
            else:
                result = {"order": session["items"]}
                session["state"] = "START"
                session["items"] = []
                return result
    
    return handle
"""
🧩 Challenge 3: Conditional Branching (Delivery vs Pickup)
📘 Problem

Ask order type: delivery or pickup

If delivery → ask address

If pickup → skip address

Return JSON"""

# 📥 Input
messages = ["Hi", "delivery", "Maseru West"]
# 📤 Output
{
    "order": {
        "type": "delivery",
        "address": "Maseru West"
    }
}
# ✅ Solution
def chatbot():
    session = {"state": "START", "data": {}}
    
    def handle(msg):
        state = session["state"]
        
        if state == "START":
            session["state"] = "ASK_TYPE"
            return "Delivery or Pickup?"
        
        elif state == "ASK_TYPE":
            session["data"]["type"] = msg
            
            if msg.lower() == "delivery":
                session["state"] = "ASK_ADDRESS"
                return "Enter address"
            else:
                result = {"order": session["data"]}
                session["state"] = "START"
                session["data"] = {}
                return result
        
        elif state == "ASK_ADDRESS":
            session["data"]["address"] = msg
            result = {"order": session["data"]}
            
            session["state"] = "START"
            session["data"] = {}
            
            return result
    
    return handle
"""🧩 Challenge 4: Update Existing Data (Edit Step)
📘 Problem

User can review and edit before final submission.

Flow:

Ask name

Ask product

Show summary

Ask: "confirm or edit?"

If edit → restart"""

# 📥 Input
messages = [
    "Hi",
    "Lomkile",
    "Bread",
    "edit",
    "Lomkile",
    "Milk",
    "confirm"
]
# 📤 Output
{
    "order": {
        "name": "Lomkile",
        "product": "Milk"
    }
}
# ✅ Solution
def chatbot():
    session = {"state": "START", "data": {}}
    
    def handle(msg):
        state = session["state"]
        
        if state == "START":
            session["state"] = "ASK_NAME"
            return "Enter name"
        
        elif state == "ASK_NAME":
            session["data"]["name"] = msg
            session["state"] = "ASK_PRODUCT"
            return "Enter product"
        
        elif state == "ASK_PRODUCT":
            session["data"]["product"] = msg
            session["state"] = "CONFIRM"
            return f"Confirm {session['data']} or edit?"
        
        elif state == "CONFIRM":
            if msg.lower() == "edit":
                session["data"] = {}
                session["state"] = "ASK_NAME"
                return "Enter name again"
            else:
                result = {"order": session["data"]}
                session["state"] = "START"
                session["data"] = {}
                return result
    
    return handle
"""🧩 Challenge 5: Multi-User Session Handling (Advanced)
📘 Problem

Handle multiple users at the same time.
"""
# 📥 Input
messages = [
    ("user1", "Hi"),
    ("user2", "Hi"),
    ("user1", "Lomkile"),
    ("user2", "John")
]
# 📤 Output

# Each user maintains their own state independently.

# ✅ Solution
def chatbot():
    sessions = {}
    
    def handle(user_id, msg):
        if user_id not in sessions:
            sessions[user_id] = {"state": "START", "data": {}}
        
        session = sessions[user_id]
        
        if session["state"] == "START":
            session["state"] = "ASK_NAME"
            return "Enter name"
        
        elif session["state"] == "ASK_NAME":
            session["data"]["name"] = msg
            result = {"user": session["data"]}
            
            sessions[user_id] = {"state": "START", "data": {}}
            return result
    
    return handle