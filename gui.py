import functions
import PySimpleGUI



label = PySimpleGUI.Text("Type your to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter Todo", key="todo")
add_button = PySimpleGUI.Button(button_text="Add", button_color="green")
exit_button = PySimpleGUI.Exit(button_text="Exit")

window = PySimpleGUI.Window('My Todo App', layout=[[label],
                            [input_box, add_button],
                                                   [exit_button]], font=("Helvatica", 15))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case PySimpleGUI.WINDOW_CLOSED:
            break
    match event:
        case "Exit":
            break









window.close()








