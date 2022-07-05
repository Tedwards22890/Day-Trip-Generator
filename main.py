import random

def destination():
    destinations=["Adirondack Mountains","New York City","Albany"]
    return destinations[random.randint(0,2)]

def restaurant():
    restaurants=["Applebees","Jollibee","NY Pizza"]
    return restaurants[random.randint(0,2)]    

def transport():
    transports=["Bus","Car","Train"]
    return transports[random.randint(0,2)]

def entertainment():
    entertainments=["Theatre","Water Park","Fair"]
    return entertainments[random.randint(0,2)]

def schedule():
    print("Let's go through your day to determine what you'll be doing!")
    dest = destination ()
    choice = input(f"Your destination is {dest}! Is this okay (y/n): ")
    if (choice != "y"):
        dest = destination ()
        choice = (f"Your destination is {dest}! Is this okay (y/n): ")
    


print("Welcome to your Day Planner!")
schedule()