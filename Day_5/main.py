todos = []

while True:
    user_action = input("Type add or show, edit, complete or exit: ")

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case 'show':
            for index,item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the TODO to edit: "))
            number = number - 1
            new_todo = input("Enter the new Todo: ")
            todos[number] = new_todo.capitalize()

        case 'complete':
            number = int(input("Number of the TODO to Complete: "))
            todos.pop(number - 1)

        case 'exit':
            break
        case _:
            print("Hey, you have entered a wrong option")
print ("Bye")