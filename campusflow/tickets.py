from priority import calculate_priority

def create_ticket(title, category, urgency, affected_users):

    title = title.strip()
    
    if title == "" :
        raise ValueError("Empty Text")

   
    categories = ("Network", "Hardware", "Software", "Other")
    category = category.title()

    if category not in categories:
        raise ValueError("Supplied Category is invalid")
    
    urgencies = ["low", "medium", "high"]
    urgency = urgency.lower()

    if urgency not in urgencies:
        raise ValueError("Urgencies level does not exist")
    

    if not isinstance(affected_users, int) or isinstance(affected_users, bool)or affected_users < 1 :
        raise ValueError("Incorrect input; user must be atleast 1 written in number")
    
    priority = calculate_priority(urgency, affected_users)

    my_ticket = {
    "id": "T001",
    "title": title,
    "category": category,
    "urgency": urgency,
    "affected_users": affected_users,
    "priority": priority,
    "status": "open",
    "assigned_to": None
    }

    return my_ticket


# print(create_ticket("", "network", "high", 15))
# print(create_ticket("Wi-Fi is down", "finance", "high", 15))
# print(create_ticket("Wi-Fi is down", "network", "high", "five"))
# print(create_ticket("Wi-Fi is down", "network", "high", True))


def generate_ticket_id(records):
    for record in records:
        ticket_id = record["id"]
        numbers = []
        for id in ticket_id:
            numbers.append(int(id[1:]))
        
        max_id = max(numbers)

        new_id = "T" + str(max_id + 1)

        return new_id
