import functions
import PySimpleGUI



label = PySimpleGUI.Text("Type your to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter Todo", key="todo")
add_button = PySimpleGUI.Button(button_text="Add", button_color="green")
exit_button = PySimpleGUI.Exit(button_text="Exit")
edit_button =PySimpleGUI.Button(button_text="Edit", button_color="blue")
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key="todos",
                               enable_events=True, size=[45, 10])

window = PySimpleGUI.Window('My Todo App', layout=[[label],
                            [input_box, add_button], [list_box, edit_button],
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
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case PySimpleGUI.WINDOW_CLOSED:
            break

        case "Exit":
            break









window.close()








