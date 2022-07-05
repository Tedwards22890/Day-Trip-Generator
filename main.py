import random

#Generates random activities
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

#Basis of choosing activities. Allows process to be redone if user is unhappy with selecton
def schedule_destination():
    print("Let's go through your day to determine what you'll be doing!")
    dest = destination ()
    choice = input(f"Your destination is {dest}! Is this okay (y/n): ")
    while (choice != "y"):
        dest = destination ()
        choice = input(f"Your destination is {dest}! Is this okay (y/n): ")
    else:
        print("How exciting!!\n")
    return dest
    
def schedule_restaurant():
    rest=restaurant()
    choice = input(f"Your restaurant is {rest}! Is this okay (y/n): ")
    while (choice != "y"):
        rest=restaurant()
        choice = input(f"Your restaurant is {rest}! Is this okay (y/n): ")
    else:
        print("Sounds yummy!\n")
    return rest

def schedule_tranport():
    tran=transport()
    choice = input(f"Your mode of tranportation is {tran}! Is this okay (y/n): ")
    while (choice != "y"):
        tran=transport()
        choice = input(f"Your mode of transportation is {tran}! Is this okay (y/n): ")
    else:
        print("Sounds like a good trip!\n")
    return tran

def Schedule_entertainment():
    ent=entertainment()
    choice = input(f"For entertainment, is {ent}! Is this okay (y/n): ")
    while (choice != "y"):
        ent=entertainment()
        choice = input(f"For entertainment, is {ent}! Is this okay (y/n): ")
    else:
        print("Sounds fun!\n")
    return ent

#Begins the first setup
print("Welcome to your Day Planner!")
dest= schedule_destination()
rest = schedule_restaurant()
tran = schedule_tranport()
ent =Schedule_entertainment()

#confirms if user is happy with scheduled activities
print(f"Alright, looks like we have a full day planned out! Let's see we got:")
print(f"Destination: {dest}\nRestaurant: {rest}\nTransportation: {tran}\nentertainment: {ent}")
choice =input("Does this look okay(y/n): ")
while (choice != "y"):
    print("Uh-oh, looks like we need to change something. Let's try again.")
    dest= schedule_destination()
    rest = schedule_restaurant()
    tran = schedule_tranport()
    ent =Schedule_entertainment()
    print(f"Let's see if this is more to your liking. Let's see we got:")
    print(f"Destination: {dest}\nRestaurant: {rest}\nTransportation: {tran}\nentertainment: {ent}")
    choice =input("Does this look okay(y/n): ")
print(f"Wonderful! Remember to keep this information so you know what you're doing:")
print(f"You're going to head to {dest} by {tran}. While you're there you'll eat at {rest} and for fun you'll stop by the {ent}!")
print("Have a great day!")