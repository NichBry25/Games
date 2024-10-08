import random

##### DICTIONARIES

# This dicitionary is used to assign a name to every location in the game.
game_map = {
    1:"Market", 2:"City Hall", 3:"Cinema", 4:"Hotel",
    5:"Residency", 6:"The Central", 7:"Fountain", 8:"Highway",
    9:"Police", 10:"Mall", 11:"Restaurant", 12:"Museum",
    13:"Bank", 14:"Barhub", 15:"Hospital", 16:"Church"
}
# This dictionary is used to assign an empty value to every location in the game.
item_in_map = {
        1:None, 2:None, 3:None, 4:None,
        5:None, 6:None, 7:None, 8:None,
        9:None, 10:None, 11:None, 12:None,
        13:None, 14:None, 15:None, 16:None
    }

##### MAIN CODE

#This is always executed first when the game is ran.
battery_life = 7 # Assigns the battery_life of the player to 7.
powercell_count = 0 # Powercell count starts at 0.
player_zone = 6 # The player always start at position 6, which is The Central.
iterations = 0 # This tracks how many turns the player needs to finish the game.

#This function takes the empty value dictionary before, and assigns randomly a value between 0-3.
def generate_item(item_in_map):
    items = [0] * 5 + [1] * 5 + [2] * 6 #Even though it is random, the total number of 0's, 1's, and 2's are always the same.
    item_in_map[6] = None
    random.shuffle(items)
    for location in item_in_map:
        if location != 6:
            item_in_map[location] = items.pop(0) #Assigning a random value, except for the 6th location because it is the starting point.
    return item_in_map

#This is the main game function.
def move_to_zone(zone):
    global battery_life 
    global powercell_count
    global iterations
    print("It's time to move!")
    zone_before = zone
    print(f"You are in {game_map[zone_before]}\n")
    movement = int(input("Where are you moving to? "))
    #This if-elif checks if there is valid movement. If the player goes to the same place they are at, then no movements are going to be executed.
    if zone_before == movement:
        print("You are in the same spot. Move again.")
        move_to_zone(zone)
    elif zone_before != movement:
        try:
            print(f"You are now in: {game_map[movement]}")
            battery_life -= 1
            iterations += 1 
            zone_now = movement
            match generated_items.get(zone_now):
                case 0: #0's are hazardous items.
                    print("Oops! You are short-circuited!\n")
                    battery_life -= 1
                    item_in_map[zone] = None
                    return zone_now
                case 1: #1's are beneficial items.
                    print("Yay! You got a battery pack!\n")
                    battery_life += 1
                    item_in_map[zone] = None
                    return zone_now
                case 2: #2's are target items. It is going to be tracked using the "powercell_count".
                    print(f"You got a powercell in {game_map[movement]}!\n")
                    powercell_count += 1
                    item_in_map[zone] = None
                    return zone_now
                case None: #When the player goes to a place they already visit, there is going to be nothing there to take.
                    print(f"This is an empty zone. Go back! \n")
                    zone = zone_now
                    return zone_now
        except:
            print("You are moving to another non-existent location. Try again.")
            move_to_zone(zone)
    
#This function displays the attributes of the player in a specific time in the game.
#The function shows how many powercells have been taken and how many battery life they have left.
def display_attributes():
    global powercell_count
    global battery_life
    if powercell_count > 1:
        print(f"You have collected {powercell_count} powercells.\n")
    else:
        print(f"You have collected {powercell_count} powercell.\n")
    print(f"You have {battery_life} battery life left.")

##### EXECUTE CODE

if __name__ == "__main__":
    print("---------- WELCOME TO ROBOT INVASION! ---------- \n")
    print("You start in The Central. This is your map! Goodluck!\n")
    print(
"  Market(01)  -  City Hall(02)  -  Cinema(03)  -  Hotel(04)   \n"
"      |               |                |               |      \n"
"Residency(05) - The Central(06) - Fountain(07)   - Highway(08)\n"
"      |               |                |               |      \n"
"  Police(09)  -     Mall(10)    - Restaurant(11) - Museum(12) \n"
"      |               |                |               |      \n"
"   Bank(13)   -    Barhub(14)   -  Hospital(15)  - Church(16) \n"
)
    generated_items = generate_item(item_in_map) #Stores the generated item map in "generated_items".
    gameplay = True #The game starts.
    while gameplay == True:  
        print("[1] - Play")
        print("[2] - Check Attributes")
        option = int(input("What do you want to do? "))  
        match option:
            case 1:
                while battery_life > 0 and powercell_count != 5:  #It is always going to be valid if the game hasn't ended yet.
                    player_zone = move_to_zone(player_zone)
                    break
                if powercell_count == 5:
                    print("YOU WON! GREAT JOB, ADVENTURER!") #If you got 5 powercells in total.
                    if iterations <= 6:
                        print("Score: 3 STARS!")
                    elif iterations <= 8:
                        print("Score: 2 STARS!")
                    elif iterations <= 10:
                        print("Score: 1 STARS!")
                    else: print("We think you can do better tho!")
                    gameplay = False
                elif battery_life == 0:
                    print("You died! Try again next time :)") #If you ran out of battery life.
                    print("Always pay attention to places you've been to. Don't waste your battery!")
                    gameplay = False
            case 2:
                display_attributes()
            case _:
                print("Your choice is non-existent.")
                quit()