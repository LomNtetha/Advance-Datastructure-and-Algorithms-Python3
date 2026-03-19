# 🧠 PART 1: Redis-Based Session Storage (Production-Ready)

"""🧩 Challenge 1: Store User Session in Redis
📘 Problem

When a user sends a message, store their session in Redis with:

state

data"""

# 📥 Input
user_id = "user_1"
message = "Hi"

# 📤 Output

# Redis should store:
{
    "state": "ASK_NAME",
    "data": {}
}

# ✅ Solution
import redis
import json

r = redis.Redis()

def handle(user_id, message):
    session = r.get(user_id)
    
    if session:
        session = json.loads(session)
    else:
        session = {"state": "START", "data": {}}
    
    if session["state"] == "START":
        session["state"] = "ASK_NAME"
        r.set(user_id, json.dumps(session))
        return "Enter name"
    
"""🧩 Challenge 2: Expire Session After Timeout
📘 Problem

Sessions should expire after 60 seconds of inactivity."""

# ✅ Solution
r.set(user_id, json.dumps(session), ex=60)  # expires in 60 seconds

# 👉 Key interview point: TTL (Time-To-Live)

"""🧩 Challenge 3: Resume Session from Redis
📘 Problem

User continues conversation — load state and continue."""

# 📥 Input
user_id = "user_1"
message = "Lomkile"

# 📤 Output
"What product do you want?"
# ✅ Solution
def handle(user_id, message):
    session = json.loads(r.get(user_id))
    
    if session["state"] == "ASK_NAME":
        session["data"]["name"] = message
        session["state"] = "ASK_PRODUCT"
        
        r.set(user_id, json.dumps(session), ex=60)
        return "What product?"
    
"""🧩 Challenge 4: Clear Session After Completion
📘 Problem

Once order is completed, remove session."""

# ✅ Solution
r.delete(user_id)

"""🧩 Challenge 5: Handle Missing/Corrupt Session
📘 Problem

If Redis data is corrupted or missing → reset safely."""

# ✅ Solution
def get_session(user_id):
    try:
        session = r.get(user_id)
        return json.loads(session) if session else {"state": "START", "data": {}}
    except:
        return {"state": "START", "data": {}}
    
# ⚡ PART 2: Event-Driven Architecture (Webhook Style)

"""🧩 Challenge 6: Parse Incoming Webhook
📘 Problem

Extract message text from webhook payload."""

# 📥 Input
payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"text": {"body": "Hi"}}
                ]
            }
        }]
    }]
}
# 📤 Output
"Hi"
# ✅ Solution
def parse_message(payload):
    return payload["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]

"""🧩 Challenge 7: Route Event to Handler
📘 Problem

Based on message type, call correct handler."""

# 📥 Input
msg = {"type": "image"}

# 📤 Output
"handle_image called"

# ✅ Solution
def route(msg):
    if msg["type"] == "text":
        return "handle_text called"
    elif msg["type"] == "image":
        return "handle_image called"
    
"""🧩 Challenge 8: Webhook → Process → Respond
📘 Problem

Full flow:

Receive webhook

Extract user + message

Process

Return response JSON"""

# 📥 Input
payload = {
    "from": "266123",
    "text": "Hi"
}
# 📤 Output
{
    "to": "266123",
    "reply": "Hello!"
}

# ✅ Solution
def webhook(payload):
    user = payload["from"]
    text = payload["text"]
    
    if text.lower() == "hi":
        reply = "Hello!"
    else:
        reply = "Unknown"
    
    return {
        "to": user,
        "reply": reply
    }

"""🧩 Challenge 9: Handle Duplicate Events (Idempotency)
📘 Problem

Prevent processing same message twice."""

# 📥 Input
message_id = "abc123"

# 📤 Output

# Process only once

# ✅ Solution
def handle(msg_id):
    if r.get(msg_id):
        return "Already processed"
    
    r.set(msg_id, "done", ex=300)
    return "Processed"

"""🧩 Challenge 10: Async Event Queue (Simulated)
📘 Problem

Instead of processing immediately, push to queue."""

# 📥 Input
payload = {"text": "Hi"}

# 📤 Output
# Stored in queue

# ✅ Solution
def enqueue(payload):
    r.lpush("queue", json.dumps(payload))