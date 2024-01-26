import PySimpleGUI
import functions
import time

PySimpleGUI.theme('black')
clock = PySimpleGUI.Text("", key='clock')
label = PySimpleGUI.Text("Type in a to-do")
input_label = PySimpleGUI.InputText(tooltip="Enter Todo", key="todo")
add_button = PySimpleGUI.Button("add")
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key="todos",
                               enable_events=True, size=[45, 10])
edit_btn = PySimpleGUI.Button("edit")
complete_btn = PySimpleGUI.Button("Complete")
exit_btn = PySimpleGUI.Button("Exit")

window = PySimpleGUI.Window('My To Do App',
                            layout=[[clock], [label],
                                    [input_label, add_button],
                                    [list_box, edit_btn, complete_btn],
                                    [exit_btn]],
                            font=('Helvetica', 12))
while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %H:%M:%S"))
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                PySimpleGUI.popup('Please select an item first.', font=('Helvetica', 12))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                PySimpleGUI.popup('Please select an item first', font=('Helvetica', 12))
        case "Exit":
            break
        case PySimpleGUI.WIN_CLOSED:
            break


window.close()
