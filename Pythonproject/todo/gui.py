import PySimpleGUI as sg
from func import *
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt','w') as file:
        pass

sg.theme('LightGreen2')
clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
edit_button = sg.Button('Edit')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=get_todos(), key='todos', enable_events=True, size=[45, 10])
Exit_button = sg.Button('Exit')
complete_button = sg.Button('Complete')
window = sg.Window('My To-Do App',
                   layout=[[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button],
                           [Exit_button]],
                   font=('Helvetica', 12))
while True:
    event, value = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    if event == 'Add':
        todos = get_todos()
        todos.append(value['todo'] + '\n')
        task_add(todos)
        window['todo'].update(value='')
        window['todos'].update(values=todos)
    elif event == 'Edit':
        try:
            todos = get_todos()
            elem = todos.index(value['todos'][0])
            todos[elem] = value['todo'] + '\n'
            task_add(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup('Please select the item for edit', font=('Helvetica', 10))
    elif event == 'Complete':
        try:
            todo_to_complete = value['todos'][0]
            todos = get_todos()
            todos.remove(todo_to_complete)
            window['todo'].update(value='')
            task_add(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup('Please select the item to complete', font=('Helvetica', 10))

    elif event == 'todos':
        window['todo'].update(value=value['todos'][0].strip())
    elif event == 'Exit':
        break
    elif event == sg.WIN_CLOSED:
        break

window.close()
