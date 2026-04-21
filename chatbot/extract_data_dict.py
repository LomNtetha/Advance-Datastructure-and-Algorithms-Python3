"""🧩 Question 1: Extract User Intent from Chatbot Payload
📘 Problem

You are given a chatbot request payload. Extract the user's intent name."""

# 📥 Input
payload = {
    "message": {
        "nlp": {
            "intents": [
                {"name": "greet", "confidence": 0.98}
            ]
        }
    }
}
# 📤 Output
"greet"
# ✅ Solution
def get_intent(payload):
    try:
        # Access nested data step by step:
        # payload → message → nlp → intents → first item → name
        result = payload["message"]["nlp"]["intents"][0]["name"]
        
        # Return the extracted intent name
        return result

    except (KeyError, IndexError, TypeError):
        # KeyError → missing dictionary key
        # IndexError → intents list is empty
        # TypeError → unexpected data type (e.g., None instead of dict/list)
        
        # Return None if anything goes wrong
        return None
    
payload = {
    "message": {
        "nlp": {
            "intents": [
                {"name": "greet", 
                "confidence": 0.98
                }
            ]
        }
    }
}
print(get_intent(payload))

def get_intent(payload):
    result = None

    if "message" in payload:
        message = payload["message"]

        if "nlp" in message:
            nlp = message["nlp"]

            if "intents" in nlp and nlp["intents"]:
                intents = nlp["intents"]

                if "name" in intents[0]:
                    result = intents[0]["name"]

    return result

"""
Get all intents names 
"""

def get_all_intent(payload):
    result = []
    for intent in payload["message"]["nlp"]["intents"]:
        result.append(intent["name"])
    return result

payload = {
    "message": {
        "nlp": {
            "intents": [
                {"name": "greet", "confidence": 0.98},
                {"name": "help", "confidence": 0.85},
                {"name": "order", "confidence": 0.60},
                {"name": "bye", "confidence": 0.40},
                {"name": "fallback", "confidence": 0.20}
            ]
        }
    }
}

print(get_all_intent(payload)) # sample output [('greet', 0.98), ('help', 0.85), ('order', 0.6), ('bye', 0.4), ('fallback', 0.2)]

def get_all_intents_plain(payload):

    result  = ""

    for intent in payload["message"]["nlp"]["intents"]:

        result += f"{intent["name"]}: {intent["confidence"]}\n"

    return result


payload = {
    "message": {
        "nlp": {
            "intents": [
                {"name": "greet", "confidence": 0.98},
                {"name": "help", "confidence": 0.85},
                {"name": "order", "confidence": 0.60},
                {"name": "bye", "confidence": 0.40},
                {"name": "fallback", "confidence": 0.20}
            ]
        }
    }
}
print(get_all_intents_plain(payload)) 
# sample output
# greet: 0.98
# help: 0.85
# order: 0.6
# bye: 0.4
# fallback: 0.2

def get_order_intent(payload):
    for intent in payload["message"]["nlp"]["intents"]:
        if intent["name"] == "order":
            print(f"{intent['name'].capitalize()}: {intent['confidence']}")  # output  Order: 0.6


"""✅Get the highest confidence intent (best practice)

Even if the list is not sorted:"""

def get_best_intent(payload):
    try:
        intents = payload["message"]["nlp"]["intents"]
        
        if not intents:
            return None

        # Find intent with highest confidence
        best = max(intents, key=lambda i: i.get("confidence", 0))
        
        return best.get("name")

    except (KeyError, TypeError):
        return None
    
"""🧩 Question 2: Get User Message Text
📘 Problem

Extract the text the user sent."""

# 📥 Input
payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"text": {"body": "Hello bot"}}
                ]
            }
        }]
    }]
}

# 📤 Output
"Hello bot"

def get_all_messages(payload):

    result = []

    messeges = payload["entry"][0]["changes"][0]["value"]["messages"]

    for msg in messeges:
        result.append(msg["text"]["body"])
    return result


payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"text": {"body": "Hello bot"}},
                    {"text": {"body": "How are you?"}},
                    {"text": {"body": "Order pizza"}}
                ]
            }
        }]
    }]
}

print(get_all_messages(payload))

def get_all_messages_plain(payload):

    result = ""

    messages = payload["entry"][0]["changes"][0]["value"]["messages"]

    for msg in messages:

        result += f"{msg["text"]["body"]}\n"

    return result

payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"text": {"body": "Hello bot"}},
                    {"text": {"body": "How are you?"}},
                    {"text": {"body": "Order pizza"}}
                ]
            }
        }]
    }]
}

print(get_all_messages_plain(payload))

# ✅ Solution
def get_message_text(payload):
    try:
        # Navigate the nested structure step by step:
        # payload → entry (list) → first item → changes (list) → first item
        # → value → messages (list) → first message → text → body
        result = payload["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        
        # Return the extracted user message text
        return result

    except (KeyError, IndexError, TypeError):
        # KeyError: missing key in dict
        # IndexError: list is empty (no entry/changes/messages)
        # TypeError: unexpected type (e.g., None instead of dict/list)
        
        # Return None if the expected structure is not present
        return None
    
# Perfect — for a dynamic webhook, you want something that:

# Won’t crash if some keys/lists are missing

# Can handle multiple entries/changes/messages

# Is readable and debuggable

# Here’s a robust, dynamic solution with comments:
    
def get_message_text(payload):
    """
    Safely extract the text the user sent from a dynamic webhook payload.
    Returns the first message text if present, otherwise None.
    """
    try:
        # Get the 'entry' list, or empty if missing
        entries = payload.get("entry", [])
        if not entries:
            return None

        # Get the first 'entry' and its 'changes' list
        changes = entries[0].get("changes", [])
        if not changes:
            return None

        # Get the first 'change' and its 'value'
        value = changes[0].get("value", {})
        if not value:
            return None

        # Get the 'messages' list
        messages = value.get("messages", [])
        if not messages:
            return None

        # Get the first message's text body
        text = messages[0].get("text", {})
        return text.get("body")

    except (TypeError):
        # If any part is not a dict/list as expected
        return None
    
"""🧩 Question 3: Extract Phone Number
📘 Problem

Return sender's phone number."""

# 📥 Input
payload = {
    "entry": [{
        "changes": [{
            "value": {
                "contacts": [
                    {"wa_id": "26612345678"}
                ]
            }
        }]
    }]
}

# 📤 Output
"26612345678"

# ✅ Solution
def get_phone(payload):
    try:
        # Navigate the nested structure step by step:
        # payload → entry (list) → first item → changes (list) → first item
        # → value → contacts (list) → first contact → wa_id (phone number)
        return payload["entry"][0]["changes"][0]["value"]["contacts"][0]["wa_id"]

    except (KeyError, IndexError):
        # KeyError: a dictionary key is missing
        # IndexError: a list is empty (no entry/changes/contacts)
        # Return None if the expected structure is not present
        return None
payload = {
    "entry": [{
        "changes": [{
            "value": {
                "contacts": [
                    {"wa_id": "26612345678"}
                ]
            }
        }]
    }]
}

print(get_phone(payload))  # Output: "26612345678"

def get_sender_phone(payload):
    """
    Safely extract the sender's phone number from a webhook payload.
    Returns the phone number as string if present, otherwise None.
    """
    try:
        # Get the 'entry' list
        entries = payload.get("entry", [])
        if not entries:
            return None

        # Get the first 'entry' and its 'changes' list
        changes = entries[0].get("changes", [])
        if not changes:
            return None

        # Get the first 'change' and its 'value'
        value = changes[0].get("value", {})
        if not value:
            return None

        # Get the 'contacts' list
        contacts = value.get("contacts", [])
        if not contacts:
            return None

        # Get the first contact's phone number (wa_id)
        contact = contacts[0]
        return contact.get("wa_id")

    except (TypeError):
        # If any part is not a dict/list as expected
        return None
payload = {
    "entry": [{
        "changes": [{
            "value": {
                "contacts": [
                    {"wa_id": "26612345678"}
                ]
            }
        }]
    }]
}

print(get_sender_phone(payload))  # Output: "26612345678"
    
"""🧩 Question 4: Get All Messages Texts
📘 Problem

Return all message texts as a list."""

# 📥 Input
payload = {
    "messages": [
        {"text": {"body": "Hi"}},
        {"text": {"body": "How are you?"}}
    ]
}

# 📤 Output
["Hi", "How are you?"]

# ✅ Solution
def get_all_messages_texts(payload):
    """
    Return all message texts from the payload as a list.
    If no messages or text bodies are found, returns an empty list.
    """
    messages_texts = []

    try:
        # Get the 'messages' list from payload
        messages = payload.get("messages", [])

        # Loop through each message
        for msg in messages:
            # Get the text body if it exists
            body = msg.get("text", {}).get("body")
            if body:
                messages_texts.append(body)

    except (TypeError):
        # In case payload is not a dict or messages is not a list
        pass

    return messages_texts
payload = {
    "messages": [
        {"text": {"body": "Hi"}},
        {"text": {"body": "How are you?"}}
    ]
}

print(get_all_messages_texts(payload))
# Output: ["Hi", "How are you?"]

# dynamic, production-ready version
def get_all_messages_from_webhook(payload):
    """
    Extract all message texts from a nested webhook payload.
    Returns a list of message bodies.
    """
    all_texts = []

    try:
        # Loop through each entry
        for entry in payload.get("entry", []):
            # Loop through each change in the entry
            for change in entry.get("changes", []):
                value = change.get("value", {})
                # Loop through each message in messages list
                for msg in value.get("messages", []):
                    # Get the text body safely
                    body = msg.get("text", {}).get("body")
                    if body:
                        all_texts.append(body)

    except (TypeError):
        # In case payload structure is not as expected
        pass

    return all_texts

payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"text": {"body": "Hi"}},
                    {"text": {"body": "How are you?"}}
                ]
            }
        }]
    }]
}

print(get_all_messages_from_webhook(payload))
# Output: ["Hi", "How are you?"]

"""🧩 Question 5: Count Messages by Type
📘 Problem

Count how many messages of each type (text, image, etc.)
"""
# 📥 Input
payload = {
    "messages": [
        {"type": "text"},
        {"type": "image"},
        {"type": "text"}
    ]
}

# 📤 Output
{"text": 2, "image": 1}

# ✅ Solution
def count_messages_by_type(payload):
    """
    Count how many messages of each type in the payload.
    Returns a dictionary like {"text": 2, "image": 1}.
    """
    counts = {}

    try:
        # Get the messages list safely
        messages = payload.get("messages", [])

        # Loop through each message
        for msg in messages:
            msg_type = msg.get("type")
            if msg_type:
                # Increment the count for this type
                counts[msg_type] = counts.get(msg_type, 0) + 1

    except (TypeError):
        # In case payload structure is unexpected
        pass

    return counts

payload = {
    "messages": [
        {"type": "text"},
        {"type": "image"},
        {"type": "text"}
    ]
}

print(count_messages_by_type(payload))
# Output: {"text": 2, "image": 1}

# dynamic, production-ready version
def count_messages_by_type_webhook(payload):
    """
    Count how many messages of each type in a nested webhook payload.
    Returns a dictionary like {"text": 2, "image": 1}.
    Handles multiple entries, changes, and messages dynamically.
    """
    counts = {}

    try:
        # Loop through each entry
        for entry in payload.get("entry", []):
            # Loop through each change in the entry
            for change in entry.get("changes", []):
                value = change.get("value", {})
                # Loop through each message in messages list
                for msg in value.get("messages", []):
                    msg_type = msg.get("type")
                    if msg_type:
                        # Increment the count for this type
                        counts[msg_type] = counts.get(msg_type, 0) + 1

    except (TypeError):
        # In case payload structure is not as expected
        pass

    return counts
payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"type": "text"},
                    {"type": "image"},
                    {"type": "text"}
                ]
            }
        }]
    }]
}

print(count_messages_by_type_webhook(payload))
# Output: {"text": 2, "image": 1}

"""🧩 Question 6: Find All URLs in Payload
📘 Problem

Extract all URLs from a nested JSON."""

# 📥 Input
payload = {
    "data": {
        "images": [
            {"url": "http://img1.com"},
            {"url": "http://img2.com"}
        ],
        "profile": {"avatar": "http://avatar.com"}
    }
}
# 📤 Output
["http://img1.com", "http://img2.com", "http://avatar.com"]
# ✅ Solution
def find_all_urls(payload):
    """
    Recursively extract all URLs (strings starting with http/https) from a nested JSON.
    Returns a list of URLs.
    """
    urls = []

    def extract(obj):
        # If the current object is a dictionary, loop through its values
        if isinstance(obj, dict):
            for value in obj.values():
                extract(value)
        # If the current object is a list, loop through its items
        elif isinstance(obj, list):
            for item in obj:
                extract(item)
        # If the current object is a string, check if it's a URL
        elif isinstance(obj, str):
            if obj.startswith("http://") or obj.startswith("https://"):
                urls.append(obj)  # Add URL to the list

    # Start recursion with the original payload
    extract(payload)

    # Return all found URLs
    return urls
payload = {
    "data": {
        "images": [
            {"url": "http://img1.com"},
            {"url": "http://img2.com"}
        ],
        "profile": {"avatar": "http://avatar.com"}
    }
}

print(find_all_urls(payload))
# Output: ["http://img1.com", "http://img2.com", "http://avatar.com"]

def parse_webhook_payload(payload):
    """
    Parse a dynamic webhook payload safely.
    
    Extracts:
    - All message texts
    - Sender phone numbers
    - Counts of message types
    - All URLs in the payload

    Returns a dictionary with:
    {
        "texts": [...],
        "phones": [...],
        "type_counts": {...},
        "urls": [...]
    }
    """
    texts = []
    phones = []
    type_counts = {}
    urls = []

    # Helper function to recursively find all URLs in nested JSON
    def extract_urls(obj):
        if isinstance(obj, dict):
            for value in obj.values():
                extract_urls(value)
        elif isinstance(obj, list):
            for item in obj:
                extract_urls(item)
        elif isinstance(obj, str):
            if obj.startswith("http://") or obj.startswith("https://"):
                urls.append(obj)

    try:
        # Loop through each entry in the payload
        for entry in payload.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})

                # ---- Extract messages ----
                for msg in value.get("messages", []):
                    # Get message text
                    body = msg.get("text", {}).get("body")
                    if body:
                        texts.append(body)

                    # Get message type and count
                    msg_type = msg.get("type")
                    if msg_type:
                        type_counts[msg_type] = type_counts.get(msg_type, 0) + 1

                # ---- Extract sender phone numbers ----
                for contact in value.get("contacts", []):
                    wa_id = contact.get("wa_id")
                    if wa_id:
                        phones.append(wa_id)

                # ---- Extract URLs from the current value ----
                extract_urls(value)

    except (TypeError):
        # If payload structure is not as expected, skip
        pass

    return {
        "texts": texts,
        "phones": phones,
        "type_counts": type_counts,
        "urls": urls
    }

payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"text": {"body": "Hi"}, "type": "text"},
                    {"text": {"body": "Check this image"}, "type": "image"}
                ],
                "contacts": [
                    {"wa_id": "26612345678"}
                ],
                "images": [
                    {"url": "http://img1.com"}
                ],
                "profile": {"avatar": "http://avatar.com"}
            }
        }]
    }]
}

result = parse_webhook_payload(payload)
print(result)
"""
🧩 Question 7: Get Latest Message
📘 Problem

Return the most recent message based on timestamp."""

# 📥 Input
payload = {
    "messages": [
        {"text": "Hi", "timestamp": 100},
        {"text": "Hello", "timestamp": 200}
    ]
}
# 📤 Output
"Hello"
# ✅ Solution
def get_latest_message(payload):
    """
    Return the most recent message text based on timestamp.
    If no messages exist, returns None.
    """
    try:
        # Get the messages list safely
        messages = payload.get("messages", [])
        if not messages:
            return None  # No messages present

        # Find the message with the maximum timestamp
        latest_msg = max(messages, key=lambda m: m.get("timestamp", 0))

        # Return the text of the latest message
        return latest_msg.get("text")

    except (TypeError):
        # In case payload is not a dict or messages is not a list
        return None
payload = {
    "messages": [
        {"text": "Hi", "timestamp": 100},
        {"text": "Hello", "timestamp": 200}
    ]
}

print(get_latest_message(payload))
# Output: "Hello"

# Perfect! Here’s a robust dynamic webhook version to get the latest message safely from a nested payload like WhatsApp webhooks, with full comments:

def get_latest_message_webhook(payload):
    """
    Return the most recent message text from a dynamic webhook payload.
    Handles multiple entries, changes, and messages.
    Returns None if no messages found.
    """
    latest_message = None
    latest_timestamp = -1  # Initialize to a very low value

    try:
        # Loop through all entries in the payload
        for entry in payload.get("entry", []):
            # Loop through all changes in each entry
            for change in entry.get("changes", []):
                value = change.get("value", {})

                # Loop through all messages in the current value
                for msg in value.get("messages", []):
                    timestamp = msg.get("timestamp", 0)
                    text = msg.get("text", {}).get("body")

                    # Update latest_message if this msg has a higher timestamp
                    if text and timestamp > latest_timestamp:
                        latest_timestamp = timestamp
                        latest_message = text

    except (TypeError):
        # In case the payload structure is unexpected
        return None

    return latest_message

payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"text": {"body": "Hi"}, "timestamp": 100},
                    {"text": {"body": "Hello"}, "timestamp": 200}
                ]
            }
        }]
    }]
}

print(get_latest_message_webhook(payload))
# Output: "Hello"

"""🧩 Question 8: Extract Buttons Titles
📘 Problem

Extract all button titles from interactive messages.
"""
# 📥 Input
payload = {
    "interactive": {
        "buttons": [
            {"title": "Yes"},
            {"title": "No"}
        ]
    }
}

# 📤 Output
["Yes", "No"]

# ✅ Solution
def get_buttons(payload):
    return [
        btn.get("title")
        for btn in payload.get("interactive", {}).get("buttons", [])
        if btn.get("title")
    ]
def get_button_titles(payload):
    """
    Extract all button titles from an interactive message payload.
    Returns a list of titles, or empty list if none found.
    """
    titles = []

    try:
        # Get the interactive section safely
        interactive = payload.get("interactive", {})

        # Get the list of buttons
        buttons = interactive.get("buttons", [])

        # Loop through each button and extract the title
        for button in buttons:
            title = button.get("title")
            if title:
                titles.append(title)

    except (TypeError):
        # If payload structure is unexpected
        pass

    return titles
payload = {
    "interactive": {
        "buttons": [
            {"title": "Yes"},
            {"title": "No"}
        ]
    }
}

print(get_button_titles(payload))
# Output: ["Yes", "No"]

# Here’s the full dynamic version for extracting all button titles from a nested webhook payload, with comments:

def get_all_button_titles_webhook(payload):
    """
    Extract all button titles from interactive messages in a dynamic webhook payload.
    Handles multiple entries and changes.
    Returns a list of button titles.
    """
    titles = []

    try:
        # Loop through each entry in the payload
        for entry in payload.get("entry", []):
            # Loop through each change in the entry
            for change in entry.get("changes", []):
                value = change.get("value", {})

                # Check if 'interactive' exists
                interactive = value.get("interactive", {})
                if not interactive:
                    continue

                # Loop through each button in the interactive section
                for button in interactive.get("buttons", []):
                    title = button.get("title")
                    if title:
                        titles.append(title)

    except (TypeError):
        # In case the payload structure is not as expected
        pass

    return titles
payload = {
    "entry": [{
        "changes": [{
            "value": {
                "interactive": {
                    "buttons": [
                        {"title": "Yes"},
                        {"title": "No"}
                    ]
                }
            }
        }]
    }]
}

print(get_all_button_titles_webhook(payload))
# Output: ["Yes", "No"]

"""🧩 Question 9: Validate Required Fields
📘 Problem

Check if required fields exist.
"""
# 📥 Input
payload = {
    "user": {"id": 1},
    "message": "Hello"
}
required = ["user.id", "message"]

# 📤 Output
True
# ✅ Solution
def validate_required_fields(payload, required_fields):
    """
    Check if all required fields exist in the payload.
    Supports nested fields using dot notation, e.g., "user.id".
    Returns True if all fields exist, False otherwise.
    """
    for field in required_fields:
        keys = field.split(".")  # Split nested keys
        current = payload

        # Traverse nested keys
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                # Field is missing
                return False

    # All required fields exist
    return 
payload = {
    "user": {"id": 1},
    "message": "Hello"
}
required = ["user.id", "message"]

print(validate_required_fields(payload, required))
# Output: True

def validate_required_fields_webhook(payload, required_fields):
    """
    Validate that all required fields exist in a dynamic webhook payload.
    Supports nested fields using dot notation, e.g., "messages.0.text.body".
    Loops through all entries and changes.
    Returns True if all fields exist in at least one entry/change, False otherwise.
    """
    try:
        # Loop through all entries
        for entry in payload.get("entry", []):
            # Loop through all changes
            for change in entry.get("changes", []):
                value = change.get("value", {})

                # Check all required fields in the current value
                all_exist = True
                for field in required_fields:
                    keys = field.split(".")
                    current = value
                    for key in keys:
                        # Handle numeric keys for list indices
                        if key.isdigit():
                            idx = int(key)
                            if isinstance(current, list) and 0 <= idx < len(current):
                                current = current[idx]
                            else:
                                all_exist = False
                                break
                        else:
                            if isinstance(current, dict) and key in current:
                                current = current[key]
                            else:
                                all_exist = False
                                break
                    if not all_exist:
                        break

                # If all fields exist in this value, return True
                if all_exist:
                    return True

    except (TypeError, ValueError):
        # If payload structure is unexpected
        return False

    # None of the entries/changes had all required fields
    return False

payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"text": {"body": "Hello"}}
                ],
                "user": {"id": 1}
            }
        }]
    }]
}

required = ["messages.0.text.body", "user.id"]

print(validate_required_fields_webhook(payload, required))
# Output: True

"""🧩 Question 10: Group Messages by Sender
📘 Problem

Group messages by sender ID."""

# 📥 Input
payload = {
    "messages": [
        {"from": "A", "text": "Hi"},
        {"from": "B", "text": "Hello"},
        {"from": "A", "text": "How are you?"}
    ]
}

# 📤 Output
{
    "A": ["Hi", "How are you?"],
    "B": ["Hello"]
}

# ✅ Solution
def group_messages_by_sender(payload):
    """
    Group messages by sender ID.
    Returns a dictionary where keys are sender IDs and values are lists of messages.
    """
    grouped = {}  # Initialize empty dictionary to hold results

    try:
        # Get messages list safely
        messages = payload.get("messages", [])

        # Loop through each message
        for msg in messages:
            sender = msg.get("from")  # Get sender ID
            text = msg.get("text")    # Get message text

            if sender and text:
                # If sender already exists in dictionary, append the message
                # Otherwise, create a new list with this message
                if sender in grouped:
                    grouped[sender].append(text)
                else:
                    grouped[sender] = [text]

    except (TypeError):
        # If payload structure is unexpected
        pass

    return grouped
payload = {
    "messages": [
        {"from": "A", "text": "Hi"},
        {"from": "B", "text": "Hello"},
        {"from": "A", "text": "How are you?"}
    ]
}

print(group_messages_by_sender(payload))
# Output:
# {
#     "A": ["Hi", "How are you?"],
#     "B": ["Hello"]
# }

"""🧩 Question 11: Extract All Media IDs
📘 Problem

From a payload, extract all media IDs (image, video, audio)."""

# 📥 Input
payload = {
    "messages": [
        {"type": "image", "image": {"id": "img_1"}},
        {"type": "text"},
        {"type": "video", "video": {"id": "vid_1"}}
    ]
}

# 📤 Output
["img_1", "vid_1"]

# ✅ Solution
def get_media_ids(payload):
    """
    Extract media IDs from messages of type image, video, or audio.
    Returns a list of media IDs.
    """
    result = []  # Initialize list to store media IDs

    # Loop through each message safely
    for msg in payload.get("messages", []):
        msg_type = msg.get("type")  # Get message type

        # Check if the message is a media type we care about
        if msg_type in ["image", "video", "audio"]:
            # Access the media content corresponding to its type
            media = msg.get(msg_type, {})
            media_id = media.get("id")  # Get media ID

            if media_id:
                result.append(media_id)  # Add media ID to results

    return result
payload = {
    "messages": [
        {"type": "text", "text": {"body": "Hi"}},
        {"type": "image", "image": {"id": "img123"}},
        {"type": "video", "video": {"id": "vid456"}},
        {"type": "audio", "audio": {"id": "aud789"}}
    ]
}

print(get_media_ids(payload))
# Output: ["img123", "vid456", "aud789"]
"""🧩 Question 12: Extract First Available Language Code
📘 Problem

Return the first language code found in user profile."""

# 📥 Input
payload = {
    "user": {
        "profile": {
            "languages": [
                {"code": "en"},
                {"code": "fr"}
            ]
        }
    }
}
# 📤 Output
"en"
# ✅ Solution
def get_language(payload):
    try:
        return payload["user"]["profile"]["languages"][0]["code"]
    except (KeyError, IndexError):
        return None

def get_first_language_code(payload):
    """
    Return the first language code found in the user's profile.
    If no language code is found, returns None.
    """
    try:
        # Navigate safely to the languages list
        languages = payload.get("user", {}).get("profile", {}).get("languages", [])
        
        if not languages:
            return None  # No languages found

        # Return the code of the first language if it exists
        return languages[0].get("code")

    except (TypeError, IndexError, AttributeError):
        # If payload structure is unexpected
        return None
"""🧩 Question 13: Count Total Attachments
📘 Problem

Count all attachments across messages.
"""
# 📥 Input
payload = {
    "messages": [
        {"attachments": [1, 2]},
        {"attachments": [3]},
        {}
    ]
}
# 📤 Output
3
# ✅ Solution
def count_total_attachments(payload):
    """
    Count all attachments across messages in the payload.
    Returns an integer count.
    """
    total = 0  # Initialize counter

    # Loop through each message safely
    for msg in payload.get("messages", []):
        # Get attachments list, default to empty list if missing
        attachments = msg.get("attachments", [])
        # Add the number of attachments in this message
        total += len(attachments)

    return total
payload = {
    "messages": [
        {"attachments": [1, 2]},
        {"attachments": [3]},
        {}
    ]
}

print(count_total_attachments(payload))
# Output: 3
"""🧩 Question 14: Extract Unique Senders
📘 Problem

Return a list of unique sender IDs."""

# 📥 Input
payload = {
    "messages": [
        {"from": "A"},
        {"from": "B"},
        {"from": "A"}
    ]
}
# 📤 Output
["A", "B"]

# ✅ Solution
def get_unique_senders(payload):
    """
    Return a list of unique sender IDs from messages.
    """
    unique_senders = set()  # Use a set to avoid duplicates

    # Loop through each message safely
    for msg in payload.get("messages", []):
        sender = msg.get("from")
        if sender:
            unique_senders.add(sender)  # Add sender to set

    # Convert set to list before returning
    return list(unique_senders)

"""🧩 Question 15: Extract All Errors
📘 Problem

Extract all error messages from deeply nested payload."""

# 📥 Input
payload = {
    "status": {
        "errors": [
            {"message": "Invalid token"},
            {"message": "Expired session"}
        ]
    }
}

# 📤 Output
["Invalid token", "Expired session"]

# ✅ Solution
def get_errors(payload):
    """
    Extract all error messages from payload['status']['errors']
    Returns the result list.
    """
    # Compute the list of error messages
    result = [
        e.get("message")
        for e in payload.get("status", {}).get("errors", [])
        if e.get("message")
    ]
    
    # Return the result
    return result
payload = {
    "status": {
        "errors": [
            {"message": "Invalid token"},
            {"message": "Expired session"}
        ]
    }
}

print(get_errors(payload))
# Output: ["Invalid token", "Expired session"]
"""🧩 Question 16: Get Conversation ID Safely
📘 Problem

Extract conversation ID or return "UNKNOWN" if missing."""

# 📥 Input
payload = {
    "conversation": {
        "id": "conv_123"
    }
}
# 📤 Output
"conv_123"

# ✅ Solution
def get_conversation_id(payload):
    """
    Extract the conversation ID from the payload.
    Returns 'UNKNOWN' if the ID is missing.
    """
    # Safely get the conversation ID
    result = payload.get("conversation", {}).get("id", "UNKNOWN")
    
    # Return the result
    return result

"""
🧩 Question 17: Extract All Texts from Mixed Content
📘 Problem

Messages may contain text, image captions, or missing data. Extract all text-like content."""

# 📥 Input
payload = {
    "messages": [
        {"text": {"body": "Hello"}},
        {"image": {"caption": "Nice pic"}},
        {"text": {"body": "Bye"}}
    ]
}
# 📤 Output
["Hello", "Nice pic", "Bye"]

# ✅ Solution
def get_all_texts(payload):
    """
    Extract all text-like content from messages, including text bodies and image captions.
    Returns a list of strings.
    """
    result = []  # Initialize the result list

    # Loop through each message safely
    for msg in payload.get("messages", []):
        # Extract text body if exists
        text_body = msg.get("text", {}).get("body")
        if text_body:
            result.append(text_body)

        # Extract image caption if exists
        image_caption = msg.get("image", {}).get("caption")
        if image_caption:
            result.append(image_caption)

    return result

"""🧩 Question 18: Filter Messages by Keyword
📘 Problem

Return messages containing a specific keyword."""

# 📥 Input
payload = {
    "messages": [
        {"text": "hello world"},
        {"text": "bye world"},
        {"text": "hello bot"}
    ]
}
keyword = "hello"

# 📤 Output
["hello world", "hello bot"]

# ✅ Solution
def filter_messages_by_keyword(payload, keyword):
    """
    Return a list of messages containing the specified keyword.
    """
    result = []  # Initialize list to store matching messages

    # Loop through each message in the payload safely
    for msg in payload.get("messages", []):
        text = msg.get("text")  # Get the message text
        if text and keyword in text:
            result.append(text)  # Add message to result if it contains the keyword

    # Return the final list of messages matching the keyword
    return result

payload = {
    "messages": [
        {"text": "hello world"},
        {"text": "bye world"},
        {"text": "hello bot"}
    ]
}
keyword = "hello"

print(filter_messages_by_keyword(payload, keyword))
# Output: ["hello world", "hello bot"]
"""🧩 Question 19: Extract Metadata Timestamps
📘 Problem

Extract all timestamps from metadata fields."""

# 📥 Input
payload = {
    "messages": [
        {"metadata": {"timestamp": 111}},
        {"metadata": {"timestamp": 222}}
    ]
}
# 📤 Output
[111, 222]

def extract_timestamps(payload):
    """
    Extract all timestamps from metadata fields in the messages.
    """
    timestamps = []  # Initialize an empty list to store timestamps

    # Loop through each message in the payload safely
    for msg in payload.get("messages", []): #if none return empty list
        metadata = msg.get("metadata", {})  # Get metadata dict, default to empty if missing
        timestamp = metadata.get("timestamp")  # Get the timestamp from metadata
        if timestamp is not None:  # Only add it if timestamp exists
            timestamps.append(timestamp)  # Add timestamp to the result list

    # Return the final list of timestamps
    return timestamps


# Example usage
payload = {
    "messages": [
        {"metadata": {"timestamp": 111}},
        {"metadata": {"timestamp": 222}}
    ]
}

print(extract_timestamps(payload))  # Output: [111, 222]


"""🧩 Question 20: Build Reply Mapping
📘 Problem

Map message ID to reply text."""

# 📥 Input
payload = {
    "messages": [
        {"id": "1", "text": "Hi"},
        {"id": "2", "text": "Hello"}
    ]
}
# 📤 Output
{
    "1": "Hi",
    "2": "Hello"
}
# ✅ Solution
def build_reply_mapping(payload):
    """
    Map each message ID to its text content.
    Returns a dictionary {id: text}.
    """
    result = {}  # Initialize the result dictionary

    # Loop through each message safely
    for msg in payload.get("messages", []):
        msg_id = msg.get("id")
        text = msg.get("text")
        if msg_id and text:
            result[msg_id] = text  # Add ID → text mapping

    return result
payload = {
    "messages": [
        {"id": "1", "text": "Hi"},
        {"id": "2", "text": "Hello"}
    ]
}

print(build_reply_mapping(payload))
# Output: {"1": "Hi", "2": "Hello"}