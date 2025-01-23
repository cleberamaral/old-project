todos = []

while True:
    user_action = input("Type add or show, or exit: ")
    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())

        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
        case _:
            print("Hey, you have entered a wrong option")

print ("Bye")
