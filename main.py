def get_todos(filepath):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def add_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, edit, exit, complete or show:")
    if user_action.startswith('add'):
        todo = user_action[4:]


        todos = get_todos("files/todos.txt")

        todos.append(todo + '\n')

        add_todos('files/todos.txt', todos)

    elif user_action.startswith('show'):


        todos = get_todos("files/todos.txt")

        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            item = item.capitalize()
            print(f"{index + 1} - {item}",)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[4:])

            todos = get_todos("files/todos.txt")

            todos[number - 1] = input("Enter new todo: ") + "\n"

            add_todos('files/todos.txt', todos)


        except ValueError:
            print("Your command is not valid")
            user_action = input("Type add, show, edit, complete or exit:")
            user_action = user_action.strip()
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1


            todos = get_todos("files/todos.txt")

            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            add_todos('files/todos.txt', todos)

            message = f'Todo "{todo_to_remove}" was removed from the list.'
            print(message)
        except IndexError:
            print("There is no such item in the todo.")
            continue
    elif user_action.startswith('exit'):
        break



