#

#uswe_prompt = "Enter your todo list: "

#today_list = []

#while True:
    #todo = input(uswe_prompt)
    #today_list.append(todo)
   #print(today_list)

#how to find what methods you can use for the data type

# dir(str)['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# use help funtion to know the use of the method e.g help(str.capitlize) and so on.

print("Welcome to your TODO list!")

import functions
import time

now = time.strftime("%b %d %Y %H:%M:%S")
print("It is", now)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        #list slicing we can use to extract some content after specific index e.g. [4:]
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        with open("todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        print("This is your todo list!")

        todos = functions.get_todos()

        for index, item in enumerate(todos, start=1):
            item = item.strip("\n")
            print(f"{index}-{item.title()}")


    elif user_action.startswith("edit"):
        try:
            number_of_todo = int(user_action[5:])
            print(number_of_todo)
            number_of_todo = number_of_todo - 1


            todos = functions.get_todos()

            new_todo = input("Enter the new todo to add to the list! ")
            todos[number_of_todo] = new_todo + "\n"

            with open("todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("You have entered an invalid response, Please enter a number of TODO you want to edit!")
            continue

    elif user_action.startswith("complete"):
        try:
            number_of_complete = int(user_action[9:])

            todos = functions.get_todos()

            number_of_complete = number_of_complete - 1
            todo_to_remove = todos[number_of_complete].strip("\n")
            todos.pop(number_of_complete)

            with open("todos.txt", 'w')  as file:
                file.writelines(todos)

            message = f'Todo {todo_to_remove} was removed from the list'
            print(message)
        except IndexError:
            print("There is no TODO with the number you've entered. Please enter an valid number of TODO")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, you have entered an unknown response! Please enter the valid response!")

print("Bye!")

