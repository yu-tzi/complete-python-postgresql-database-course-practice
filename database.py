import sqlite3

connection = sqlite3.connect("database.db")
connection.row_factory = sqlite3.Row
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
    cursor = connection.execute("SELECT * FROM tasks;")
    # connection.execute returns a cursor object
    # a cursor is used to iterate over the results of a query

    # get single row
    # cursor.fetchone() # get first row and move the cursor to the next row
    # cursor.fetchone() # get second row and move the cursor to the next row

    # get all rows
    return cursor  # return the cursor to the caller to iterate over and the single data is a tuple if connection.row_factory = sqlite3.Row is not set
