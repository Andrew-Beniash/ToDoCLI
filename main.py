while True:
    user_action = input("Type add, edit, exit, complete or show:")
    if 'add' in user_action:
        todo = user_action[4:]
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    if 'show' in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            item = item.capitalize()
            print(f"{index + 1} - {item}",)

    if 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos[number - 1] = input("Enter new todo: ") + "\n"

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    if 'complete' in user_action:
        number = int(input("Number of the todo to complete: "))
        index = number - 1
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f'Todo "{todo_to_remove}" was removed from the list.'
        print(message)
    if 'exit' in user_action:
        break


print("Bye!")

