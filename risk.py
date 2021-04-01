import os
import random

# Throw a dice
def throw():
    return random.randint(1, 6)


# Ask for a number
def askNumber():
    while True:
        try:
            # Store input
            tmp = int(input(""))

            # Check if input smaller than 1
            if tmp < 1:
                throw(Exception())
            else:
                return tmp
        except:
            print("/!\\ ENTER A VALID NUMBER /!\\")
            continue


# Attack
def attack(attacker, defender, automatic):
    # Initialize temporary variables
    currentAttack = attacker
    currentDefender = defender
    while True:
        # Throw dices
        attackerThrow = sorted(
            [
                throw(),
                (throw() if currentAttack > 1 else 0),
                (throw() if currentAttack > 2 else 0),
            ],
            reverse=True,
        )
        defenderThrow = sorted(
            [throw(), (throw() if currentDefender > 1 else 0)], reverse=True
        )

        # Attack begins
        print(
            "\n\n+----{ ATTACK BEGINS }\n| ("
            + str(currentAttack)
            + " vs "
            + str(currentDefender)
            + ")\n|"
        )

        # Display throws
        print(
            "+----{ THROWS }\n|\n| Attacker : "
            + str(attackerThrow)
            + "\n| Defender : "
            + str(defenderThrow)
            + "\n|"
        )

        # Attack begins
        print("+----{ ACTIONS }\n|")

        # First dice
        if attackerThrow[0] > defenderThrow[0]:
            print("| Defender lost 1")
            currentDefender -= 1
        else:
            print("| Attacker lost 1")
            currentAttack -= 1

        # Second dice
        # Check if a second attack is possible
        if currentAttack > 1 and currentDefender > 1:
            if attackerThrow[1] > defenderThrow[1]:
                print("| Defender lost 1")
                currentDefender -= 1
            else:
                print("| Attacker lost 1")
                currentAttack -= 1

        # Attack ends
        print(
            "|\n+----{ RESULTS }\n| Attackers:\t"
            + str(currentAttack)
            + "\n| Defenders:\t"
            + str(currentDefender)
            + "\n+-------------------+\n"
        )

        # Check if attacker still has soldiers
        if currentAttack < 1:
            print("\n * DEFENDER WON *\n")
            break

        # Check if defender still has soldiers
        if currentDefender < 1:
            print("\n * ATTACKER WON *\n")
            break
        if not automatic:
            # Check if attacker want to retrive
            nextAttack = input(
                "Press any key to continue attacking (Press x to retrive)\n"
            )
            if nextAttack == "x":
                print("Attacker retrived!")
                break


# Execution
try:
    os.system("clear")
    print(
        "\n\n\n\t#####   ##   #####   ##  ##\n\t#   #   ##   #       ## ##\n\t#####   ##   #####   ####\n\t# ##    ##       #   ## ##\n\t#  ##   ##   #####   ##  ##  \n\t\t\t\t\tv.2\n\n\n"
    )
    input("Press anywhere to start ")
    os.system("clear")
    while True:
        # Ask for atacker and defender units numbers
        print("Number of attackers --> ", end="")
        attackers = askNumber()
        print("\nNumber of defenders -->", end="")
        defenders = askNumber()

        # Ask if the attack should be automatic
        automatic = input(
            '\n\nPress any key to attack manually\n(Enter "auto" to attack automatically)\n--> '
        )
        automatic = (
            automatic == "A"
            or automatic == "a"
            or automatic == "Automatic"
            or automatic == "automatic"
            or automatic == "auto"
            or automatic == "Auto"
            or automatic == "AUTO"
        )
        os.system("clear")

        # Perform attack
        attack(attackers, defenders, automatic)

        # Wait for next attack
        input("Press any key to start next attack")
        os.system("clear")
except:
    os.system("clear")
