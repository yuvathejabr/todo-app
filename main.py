from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %H:%M:%S")
print("Right time now", now)
while True:
    user_input = input('Enter add, edit, show, done or exit : ')
    user_input = user_input.strip()

    if user_input.startswith("add"):
        todo = input('Enter a Todo : ') + '\n'
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_input.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item.title()}"
            print(row)

    elif user_input.startswith("edit"):
        number = int(input("Enter a number to be edit : "))
        new_todo = input("Enter a Todo : ")
        todos = get_todos()
        todos[number-1] = new_todo + '\n'
        write_todos(todos)

    elif user_input.startswith("done"):
        number = int(input('Enter a number which has been done : '))
        index = number - 1
        todos = get_todos()

        todo_remove = todos[index].strip('\n')
        todos.pop(index)

        write_todos(todos)

        message = f"Todo {todo_remove} has remove from the todos list"
        print(message)

    elif user_input.startswith("exit"):
        break
    else:
        print("Hey, you enter unknown commands")

print('Bye...!')
