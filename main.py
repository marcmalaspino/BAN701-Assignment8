#Assignment 8 - Git Development with AI

import random

#Dictionary to store monster difficulty and stat multiplier.
difficulty_level = {"easy": 1, "intermediate": 2, "hard": 3}

#List to store all created monsters so program can let user know
#how many were created during program.
saved_monsters = []

#List to store the monster's stats.
stats = ["hp", "attack", "defense"]

#List of weapons a monster can be given.
weapons = ["sword", "bow", "axe", "staff", "dagger"]

#Dictionary to store each move's attack bonus and defense bonus.
#Bonuses are listed separately and do not change the base stats.
moves = {
    "Power Strike": {"attack": 3, "defense": 0},
    "Shield Bash": {"attack": 1, "defense": 2},
    "Guard Up": {"attack": 0, "defense": 3},
    "Quick Slash": {"attack": 2, "defense": 1},
    "Rally Cry": {"attack": 2, "defense": 2}
}

#Generates monsters with the user's given name and difficulty.
#Stats are generated randomly from 1-10, and scaled by the multiplier
#based on difficulty. "Easy" monster stats range from 1-10, "Hard" from 3-30.
def generate_monster(name, difficulty):
    multiplier = difficulty_level[difficulty]

    #Stage 2: Difficulty is now stored inside the monster so the
    #end of session summary can display it later.
    monster = {"name": name, "difficulty": difficulty}

    for stat in stats:
        monster[stat] = random.randint(1,10) * multiplier

    #Gives the monster one random weapon and two different random moves.
    monster["weapon"] = random.choice(weapons)
    monster["moves"] = random.sample(list(moves), 2)

    return monster

#Loop to check for duplicate monsters given user input.
#Returns True/False depending if monster already exists.
def is_duplicate(name, difficulty):
    for m in saved_monsters:
        if name.lower() == m["name"].lower() and difficulty.lower() == m["difficulty"].lower():
            return True
    return False


def main():

    #Stage 2: Moved Welcome Message to within main()
    print("Welcome to the Monster Generator")
    print("Create and store monsters!")
    print("**************************\n")

    #Repeats until the user answers "n". Any answer other than y/n
    #re-prompts instead of creating a monster by accident.
    while True: 

        create = input("Would you like to create a monster? (y/n): ").lower()
        
        if create == "n":
            break
        elif create != "y":
            print("Please enter y or n.\n")
            continue

        name = input("Enter a name: ").strip()

        #Stage 2: Checks for blank name entry and re-prompts until user types something.
        if name == "":
            print("Name can't be blank.\n")
            continue

        difficulty = input("Enter a difficulty (easy, intermediate, hard): ").strip().lower()

        #Stage 2: Invalid difficulty entry used to crash the program.
        #This if statement now checks the dictionary first - if invalid,
        #it displays a message and restarts the loop
        if difficulty not in difficulty_level:
            print("Invalid entry. Please choose easy, intermediate, or hard\n")
            continue

        #Runs the duplicate check and either prints an error message
        #or continues program depending on returned value
        if is_duplicate(name, difficulty):
            print (f"{name} ({difficulty}) already exists.")
            continue

        monster = generate_monster(name, difficulty)
        saved_monsters.append(monster)

        print("\nHere is your monster!:\n")
        print("Name:", monster["name"])
        print("Difficulty:", difficulty.capitalize())
        print("Stats:" )

        for stat in stats:
            print(f" {stat.upper()}: {monster[stat]}")

        #Shows the monster's weapon and each move with its bonuses.
        print("Weapon:", monster["weapon"].capitalize())
        print("Moves:")
        for move in monster["moves"]:
            print(f" {move}: +{moves[move]['attack']} ATK, +{moves[move]['defense']} DEF")


    print(f"\nYou created {len(saved_monsters)} monster(s).")

    #Stage 2: Lists every monster created in the session, including stats an total power.
    #Skipped when the list is empty so the user doesn't see an empty heading.
    if saved_monsters:
        print("\nYour monsters:")
        for m in saved_monsters:
            total = sum(m[stat] for stat in stats)
            print(f"- {m['name']} ({m['difficulty'].capitalize()}): "
                  f"HP {m['hp']}, ATK {m['attack']}, DEF {m['defense']} | Total Power: {total}")

            #Weapon and moves are listed under each monster, separate from Total Power.
            print(f"    Weapon: {m['weapon'].capitalize()}")
            for move in m["moves"]:
                print(f"    Move: {move} (+{moves[move]['attack']} ATK, +{moves[move]['defense']} DEF)")

    print("\nSee you next time!")

#Main guard so main() only runs when the file is executed directly.
if __name__ == "__main__":
    main()