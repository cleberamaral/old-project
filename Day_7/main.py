
while True:
    user_action = input("Type add or show, edit, complete or exit: ")

    match user_action.strip():# strip remove spaces
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            file = open("todos.txt",'r')
            todos = file.readlines()
            file.close()
            todos.append(todo.capitalize())
            file = open("todos.txt",'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            #new_todos = [item.strip('\n') for item in todos] #remove the \n from the todos list if exists - list compreensions
            for index,item in enumerate(todos):
                item = item.strip('\n')
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