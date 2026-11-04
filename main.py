#Assignment 8 - Git Development with AI

import random

#Dictionary to store monster difficulty and stat multiplier.
difficulty_level = {"easy": 1, "intermediate": 2, "hard": 3}

#List to store all created monsters so program can let user know
#how many were created during program.
saved_monsters = []

#List to store the monster's stats.
stats = ["hp", "attack", "defense"]

#Generates monsters with the user's given name and difficulty.
#Stats are generated randomly from 1-10, and scaled by the multiplier
#based on difficulty. "Easy" monster stats range from 1-10, "Hard" from 3-30.
def generate_monster(name, difficulty):
    multiplier = difficulty_level[difficulty]
    monster = {"name": name}

    for stat in stats:
        monster[stat] = random.randint(1,10) * multiplier

    return monster

def main():

    #Repeats until the user answers "n". Any answer other than y/n
    #re-prompts instead of creating a monster by accident.
    while True: 

        create = input("Would you like to create a monster? (y/n): ").lower()
        
        if create == "n":
            break
        elif create != "y":
            print("Please enter y or n.\n")
            continue

        name = input("Enter a name: ")
        difficulty = input("Enter a difficulty (easy, intermediate, hard): ").lower()

        monster = generate_monster(name, difficulty)
        saved_monsters.append(monster)

        print("\nHere is your monster!:\n")
        print("Name: ", monster["name"])
        print("Difficulty: ", difficulty.capitalize())
        print("Stats:" )

        for stat in stats:
            print(f" {stat.upper()}: {monster[stat]}")


    print(f"\nYou created {len(saved_monsters)} monster(s).")
    print("See you next time!")

#Main guard so main() only runs when the file is executed directly.
if __name__ == "__main__":

    print("Welcome to the Monster Generator")
    print("Create and store monsters!")
    print("*****************************************\n")

    main()


