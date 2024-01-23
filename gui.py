import PySimpleGUI
import functions

label = PySimpleGUI.Text("Type in a to-do")
input_label = PySimpleGUI.InputText(tooltip="Enter Todo", key="todo")
add_button = PySimpleGUI.Button("add")

window = PySimpleGUI.Window('My To Do App',
                            layout=[[label], [input_label, add_button]],
                            font=('Helvetica', 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case PySimpleGUI.WIN_CLOSED:
            break


window.close()
