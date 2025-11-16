import sqlite3

connection = sqlite3.connect("database.db")
task_list = []


def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, date TEXT)"
        )


def add_task(task, date):
    with connection:
        # don't use f"INSERT INTO tasks (task, date) VALUES ('{task}', '{date}');" it might cause SQL injection
        connection.execute(
            # sqlite3 will replace the ? with the values in the tuple
            "INSERT INTO tasks (task, date) VALUES (?, ?);",
            (task, date),
        )


def get_tasks():
    return task_list
