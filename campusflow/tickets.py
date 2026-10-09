from priority import calculate_priority

def create_ticket(title, category, urgency, affected_user):

    title = title.strip()
    
    if title == "" :
        while True:
            try: 
                title = input("Enter New Title: ")
                return
            except ValueError: 
                print("Empty Text")

    priority = calculate_priority(urgency, affected_user)


