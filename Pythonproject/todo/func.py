def task_add(todos):
    '''Help to add task to todos list '''
    with open('todos.txt', 'w') as file:
        file.writelines(todos)

def get_todos():
    with open("todos.txt", 'r') as file:
        todos = file.readlines()
    return todos

def write_todo(todos):
    with open("todos.txt", 'w') as file:
        file.writelines(todos)

def check_task_in_list(todos,elem):
    game=[i.lower().strip() for i in todos]
    if elem.lower() in game:
        return game.index(elem.lower())
    else:
        return False


