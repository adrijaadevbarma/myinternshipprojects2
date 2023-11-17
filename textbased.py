import time

score = 0

def introduction():
    global score
    print("Welcome to the Text-based Adventure Game!")
    time.sleep(1)
    print("You wake up in a dense forest, unsure of how you got there.")
    time.sleep(1)
    print("You see three paths leading in different directions.")
    time.sleep(1)
    print("Your adventure begins!")
def make_choice():
    print("\nChoose your path:")
    print("1. Take the left path.")
    print("2. Take the middle path.")
    print("3. Take the right path.")
    choice = input("Enter 1, 2, or 3: ")
    return choice

def left_path():
    global score
    print("\nYou chose the left path.")
    time.sleep(1)
    print("You encounter a talking squirrel with a riddle.")
    time.sleep(1)
    print("Solve the riddle to gain a reward.")

    riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
    print(riddle)
    answer = input("\nYour answer: ").lower()

    if answer == "an echo":
        print("\nThe squirrel is impressed! You gain 10 points.")
        score += 10
    else:
        print("\nIncorrect. The correct answer was 'an echo'.")

    print("You continue your journey.")
    time.sleep(1)

def middle_path():
    global score
    print("\nYou chose the middle path.")
    time.sleep(1)
    print("You find a mysterious potion on the ground.")
    time.sleep(1)
    print("Do you want to drink the potion or leave it?")
    
    print("1. Drink the potion.")
    print("2. Leave the potion.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nThe potion grants you temporary invisibility. You sneak past potential dangers.")
        score += 5
    elif choice == "2":
        print("\nYou decide not to risk it. You continue your journey cautiously.")
    else:
        print("\nInvalid input. Please try again.")
        middle_path()

def right_path():
    global score
    print("\nYou chose the right path.")
    time.sleep(1)
    print("You come across a bridge guarded by a troll.")
    time.sleep(1)
    print("To pass, you need to answer the troll's question.")

    troll_question = "What has keys but can't open locks?"
    troll_answer = input("\nYour answer: ").lower()

    if troll_answer == "a piano":
        print("\nThe troll is amused and lets you pass. You gain 15 points.")
        score += 15
    else:
        print("\nThe troll is not pleased. You need to find another way around.")
        return

    print("You cross the bridge and continue your journey.")
    time.sleep(1)

def conclusion():
    print("\nCongratulations on completing the Text-based Adventure Game!")
    print("Your final score is:", score)

def main():
    introduction()

    while True:
        choice = make_choice()

        if choice == "1":
            left_path()
            break
        elif choice == "2":
            middle_path()
            break
        elif choice == "3":
            right_path()
            break
        else:
            print("\nInvalid input. Please try again.")

    conclusion()

if __name__ == "__main__":
    main()