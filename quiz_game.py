import os
import sys
import time
import random

# ----------------- Typewriter print -----------------
def tprint(text, delay=0.05, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

# ----------------- House from score -----------------
def house_from_score(score_percent):
    if score_percent == 0:
        return "Lanister"
    elif score_percent == 20:
        return "Tygerian"
    elif score_percent == 40:
        return "Baratheon"
    elif score_percent == 60:
        return "Dragon"
    elif score_percent == 80:
        return "Stark"
    elif score_percent == 100:
        return "Khal"

# ----------------- Update table in one file -----------------
def update_table(filename, house, name):
    houses = ["Lanister", "Tygerian", "Baratheon", "Dragon", "Stark", "Khal"]

    # If file does not exist, create header
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            header = "House of | " + " | ".join(houses) + " |"
            f.write(header + "\n")

    # Read existing table
    with open(filename, "r") as f:
        lines = f.readlines()

    # Process existing rows
    table = []
    for line in lines[1:]:  # skip header
        row = [cell.strip() for cell in line.strip().split("|")[1:-1]]
        table.append(row)

    # Find first empty row for this house
    col_index = houses.index(house)
    placed = False
    for row in table:
        if row[col_index] == "":
            row[col_index] = name
            placed = True
            break

    # If all rows are filled, add new row
    if not placed:
        new_row = [""] * len(houses)
        new_row[col_index] = name
        table.append(new_row)

    # Write back to file
    with open(filename, "w") as f:
        header = "House of | " + " | ".join(houses) + " |"
        f.write(header + "\n")
        for i, row in enumerate(table):
            line = f"{i+1}." + " | " + " | ".join([cell if cell != "" else " " for cell in row]) + " |"
            f.write(line + "\n")

    tprint(f"Saved {name} under {house} in {filename}!")

question = "Guess five one digit numbers"
score = 0
guesses = []
answers = [random.randint(0, 9) for _ in range(5)]

tprint(" ------------------------------")
tprint("| You want to play! Let's play |")
tprint(" ------------------------------")
name=input("Enter your name: ")
tprint(question)

for i in range(5):
    while True:
        try:
            g = int(input(f"{i+1}. Enter number (0-9): "))
            if 0 <= g <= 9:
                guesses.append(g)
                if g == answers[i]:
                    score += 1
                break
            else:
                tprint("Invalid number. Enter in between 0 to 9.")
        except ValueError:
            tprint("Please enter a valid number.")

score_percent = score / 5 * 100

tprint("----------------------------------")
tprint("Let's check out how perfect you are")
tprint(f"You scored {score_percent}%")
tprint("\nYour Results:")
tprint("Index | Guess | Answer | Match")
tprint("----------------------------------")
for i in range(5):
    match = "✔️" if guesses[i] == answers[i] else "❌"
    tprint(f"  {i+1}   |   {guesses[i]}    |   {answers[i]}     |  {match}")

tprint("----------------------------------")
if score_percent == 0:
    tprint("Ha Ha Ha! Idiot little imp\nI'm pretty sure you belong to Lannister\nYou might hear the phrase 'Idiot like a Lannister'")
elif score_percent == 20:
    tprint("Well, it's not so easy game\nI appreciate at least you are not a bastard")
elif score_percent == 40:
    tprint("Umm! You don't think so much, just hit the button\nBut this time you got lucky")
elif score_percent == 60:
    tprint("Good job bud\nYou are better than average")
elif score_percent == 80:
    tprint("Ah! Too close\nJust one move away to the crown\nBut I know you can never make it\nBecause you take time to think and move\nBut this time you won't get such enough time\nSAD!")
elif score_percent == 100:
    tprint("You win, I lose\nYou are my Khal now!")
house = house_from_score(score_percent)
update_table("quiz_game.txt", house, name)