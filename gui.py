import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")
input_label = PySimpleGUI.InputText(tooltip="Enter Todo")
add_button = PySimpleGUI.Button("add")

window = PySimpleGUI.Window('My To Do App', layout=[[label], [input_label, add_button]])
window.read()
window.close()
