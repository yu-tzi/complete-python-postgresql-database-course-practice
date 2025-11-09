menu = """Pleas select one of the following options:
1. Add a new task
2. View all tasks
3. Exit the app

Your Selection:
"""

welcome_message = "Welcome to the Todo App!"
exit_message = "Thank you for using the Todo App. Bye!"

print(welcome_message)

user_input = input(menu)
while user_input != "3":
    if user_input == "1":
        print("You selected to add a new task.")
        user_input = input(menu)
    elif user_input == "2":
        print("You selected to view all tasks.")
        user_input = input(menu)
    else:
        print("Invalid selection. Please try again.")
        user_input = input(menu)

print(exit_message)
