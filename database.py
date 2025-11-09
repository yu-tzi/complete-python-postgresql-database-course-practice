task_list = []


def add_task(task, date):
    task_list.append({"task": task, "date": date})


def get_tasks():
    return task_list
