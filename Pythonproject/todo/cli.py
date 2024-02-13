# todo app with python
import func

print("Type :['add','show','edit','complete','remove','clear','exit']")
todos = []
while True:
    a = input('Enter what you want to do:')
    if a.lower().startswith('add'):
        with open("todos.txt", 'r') as file:
            todos = file.readlines()
            if len(a) > 4:
                todos.append(a[4:] + '\n')
                func.task_add(todos)
                print('task added successfully')
            else:
                print("Enter task like 'add playing game'")
                continue

            file.close()

    elif a.lower() == 'show':
        todo = func.get_todos()
        todog = [i.strip() for i in todo]
        for index, i in enumerate(todog):
            print(f"{index + 1} - {i}")

    elif 'edit' in a.lower():
        todos = func.get_todos()
        if len(a) > 5 and a.split(' ')[1].isnumeric() and int(a.split(' ')[1]) <= len(todos):
            num = int(a.split(' ')[1])
            task = input('Enter new Task: ') + '\n'
            todos[int(num) - 1] = task
            func.write_todo(todos)
        elif len(a) > 5 and a.split(' ')[1].isalnum():
            value = func.check_task_in_list(todos, a.split(' ', 1)[1])
            if value >= 0:
                todos[int(value)] = input('Enter new Task: ') + '\n'
                func.write_todo(todos)
            else:
                print("This task don't exist in lists")
        else:
            print("Enter in format 'edit 6' or enter like 'edit playing music'")
            continue

    elif a.lower().startswith('complete'):
        todo = func.read_file()
        try:
            if len(a) > 9 and a.split(' ')[1].isnumeric():
                num = int(a.split(' ')[1])
            elif len(a) > 9 and a.split(' ')[1].isalpha():
                value = func.check_task_in_list(todos, a.split(' ', 1)[1])
                num = value + 1
            else:
                num = int(input("Enter the number of task you have completed "))
            todo.pop(num - 1)
            func.write_file(todo)
        except:
            print('Enter valid number')


    elif 'remove' in a.lower():
        num = int(input("Enter the number of task you want to remove: "))
        todo = func.read_file()
        todo.pop(num - 1)
        func.write_file(todo)

    elif a == 'exit':
        break

    elif a == 'clear':
        open('todos.txt', 'w').close()

    else:
        print('Enter valid task name')
