
# Personal Mini-Toolkit - PLP Week 8
# A collection of three useful Python tools.

import random

# Store tasks for the To-Do List
tasks = []


# Tool 1: Simple Calculator
# Performs basic mathematical operations.
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter your choice: ")

    if operation == "1":
        print(f"Result: {num1 + num2}")
    elif operation == "2":
        print(f"Result: {num1 - num2}")
    elif operation == "3":
        print(f"Result: {num1 * num2}")
    elif operation == "4":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Sorry, division by zero is not allowed.")
    else:
        print("Invalid operation. Please try again.")


# Tool 2: To-Do List
# Allows users to add, view and remove tasks.
def todo_list():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter your task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully!")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour Tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter task number to remove: "))
                    if 1 <= task_number <= len(tasks):
                        removed = tasks.pop(task_number - 1)
                        print(f"Task '{removed}' removed successfully!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


# Tool 3: Number Guessing Game
# Challenges users to guess a randomly selected number.
def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- NUMBER GUESSING GAME ---")
    print("I have selected a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed correctly in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid whole number.")


# Main menu: Runs until the user chooses to quit.
def main():
    print("Welcome to My Personal Mini-Toolkit!")

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            print("Thank you for using My Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


# Start the program.
if __name__ == "__main__":
    main()

