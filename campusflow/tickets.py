from priority import calculate_priority

def create_ticket(title, category, urgency, affected_user):

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
    

    if affected_user < 1: 
        raise ValueError("There must be atleast one person affected")
    
    priority = calculate_priority(urgency, affected_user)

