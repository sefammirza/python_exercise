print("Welcome to my first game!")
name = input("what is your name?")
age = int(input("what is your age?"))

health = 10

if age >= 18:
    print("You are old enough to play!")
    
    wants_to_play = input("Do you want to play?").lower()
    if wants_to_play == "yes":
        print("You are staring with", health, "health")
        print("Let's play!")
        left_or_right = input("First choice... Left or Right (left/right)?")
        if left_or_right  == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")
            
            if ans == "around":
                print("You went around and reached the the other side of the lake")
                
            elif ans == "across":
                print("You managef to get across, but were bit by a fish and lost 5 health")
                health -= 5
                
            ans = input("You notice a hause and a river. which do you go to (river/hause)?")
            if ans =="hause":
                print("You go to the house and are greted by the owner...He doesn't like you lose 5 health")
                health -= 5   
                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived...You win.. ")
                
            else:
                print("You fell in the river and lost...")
                

            
        else:
            print("You fell down and lost...")
    else:
        print("Cya...")
        
else:
    print("You are not old enough to play...")