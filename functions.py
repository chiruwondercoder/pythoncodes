def get_todos():
    with open("todos.txt", 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local