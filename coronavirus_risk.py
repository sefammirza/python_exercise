age = input("Are you a cigarette addict older than 75 years old?: ")
chronic = input("Do you have a severe chronic disease?: ")
immune =  input("Is your immune system too weak?: ")

if age == "yes":
    age = True
elif age == "no":
    age = False
else:
    print("You have entered the wrong value.")
    
if chronic == "yes":
    chronic = True
elif chronic == "no":
    chronic = False
else:
    print("You have entered the wrong value.")

if immune == "yes":
    immune = True
elif immune == "no":
    immune = False
else:
    print("You have entered the wrong value.")
    
result = chronic or immune or age 
if result == True:
    print("You are in risky group")
else:
    print("You are not in risky group")
    
    