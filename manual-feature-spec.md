# Feature Specification: Duplicate Monster Check

## Purpose
Prevent accidentally creating the same moster twice, while still allowing the same name at different difficulty levels.

## Expected Behavior
After the user enters a valid name and difficulty, the program checks saved_monsters for a monster with the same name (regardless of case) and difficulty. If one alrady exists, the program prints a message and returns to the "Would you like to create a monster?" prompt without saving anything. If the monster does not exist, it is created as usual.

## Test Cases
1. Create "Goblin" (easy), then "goblin" (easy).
  - Expected: "Moster already exists" message, and new monster is not saved.
2. Create "Goblin" (easy), then "Goblin" (hard).
  - Expected: both saved; summary shows both monsters.