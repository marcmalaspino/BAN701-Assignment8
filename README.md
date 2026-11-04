# BAN701-Assignment8
Assignment 8 for BAN 701

## Description
A simple Python program that generates random fantasy monsters. The user chooses a name and difficulty, and the program creates a monster with random HP, Attack, and Defense stats scaled by the chosen difficulty.

## Initial Version
- Asks the user if they want to create a monster, and repeats until the ansewr is "n". Invalid input re-prompts the question.
- Accepts a custom name and a diffuctly (easy, intermediate, hard).
- Uses a function to generate random stats, scaled by a difficulty multiplier.
- Prints each monster's name, difficulty, and stats.
- Stores monsters in a list during the session and reports how many were created.

AI use in this initial stage: I wrote the program myself, but used Claude to review my draft for typos, bugs, etc. No extra code/comments were added based on Claude's review.

## AI Tool Used
Claude (Anthropic)

## AI Assistance
- Stage 1: I asked Claude to review for bugs, typos, and syntax errors. I fixed what it pointed out.
- Stage 2: I asked Claude review for logic, display/format improvements, and user functionality improvements. I specifically prompted to extend/improve what already existed and not to revamp the entire program.

## New/Modified Features
- Difficulty validation: Unrecognized difficulty no longer crashes the program. The user sees an error message and is re-prompted for input.
- Difficutly storage: Difficulty is now stored in the monster dictionary, allowing for display in the end of session summary.
- End-of-session summary: When the user exits, all mosters created during the session are listed with their stats, difficulty, and total power.

## Evaluation of AI Output
Claude suggested input validation for difficulty and name, storing the difficulty in the monster dictionary, and displaying the saved monsters at the end of the program. I chose to include all of these suggestions becuase they were simple extensions of what the program already included instead of a full revamp and also prevented unwanted crashes. Claude also suggested to output the monsters to a JSON file - I opted not to use this suggestion, as it changed/added entirely new features to the program, which no longer felt like "mine."

## How to Run the Program

### Requirements
- Python

### Steps
1. Clone the repository:
```

git clone https://github.com/marcmalaspino/BAN701-Assignment8
```

2. Run the program:
```

python main.py
```

3. Follow the prompts in the terminal

