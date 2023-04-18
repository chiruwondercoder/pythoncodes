import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type your to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter Todo")
add_button = PySimpleGUI.Button(button_text="Add", button_color="green")

window = PySimpleGUI.Window('My Todo App', layout=[[label, input_box, add_button]])
window.read()
window.close()

