from database import create_table, add_task, get_tasks

menu = """Pleas select one of the following options:
1. Add a new task
2. View all tasks
3. Exit the app

Your Selection:
"""

welcome_message = "Welcome to the Todo App!"
exit_message = "Thank you for using the Todo App. Bye!"


def prompt_new_task():
    task = input("Enter the new task: ")
    date = input("Enter the date: ")
    add_task(task=task, date=date)


def view_all_tasks():
    task_list = get_tasks()
    for task in task_list:
        print(f"Task: {task['task']}, Date: {task['date']}")


# execution starts here

print(welcome_message)
create_table()

user_input = input(menu)
while user_input != "3":
    if user_input == "1":
        prompt_new_task()
        user_input = input(menu)
    elif user_input == "2":
        view_all_tasks()
        user_input = input(menu)
    else:
        print("Invalid selection. Please try again.")
        user_input = input(menu)

print(exit_message)
