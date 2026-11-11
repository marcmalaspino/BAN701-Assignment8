# Feature Specification: Weapons and Moves

## Purpose
Give each monster a weapon and special moves that modify its combat stats, making monsters more distinct.

## Expected Behavior
- A "weapons" list (sword, bow, axe, staff, dagger) and a "moves" dictionary are defined at the top of the file. Each move maps to an attack bonus and defense bonus, e.g., "Power Strike": {"attack:: 3, "defense": 0}.
- When a monster is generated, it receives one random weapon and two different random moves.
- Move bonuses are listed separately from the base stats. They do not change HP, attack, or defense. Total Power also remains the same.
- Bonuses do not scale with difficulty.
- The monster display and the end-of-session summary show the weapon, the moves, and each move's bonuses.
- Existing code style and comments are preserved.

## Test Cases
1. Generate a monster
  - Expected: Weapon is in the wapons list; exactly 2 distinct moves are both from the moves dictionary.
2. Create 2 monsters, then end the session.
  - Expected: The summary lists each monster's weapon and moves.