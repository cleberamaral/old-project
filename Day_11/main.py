def get_todos():
    with open("../todos.txt", 'r') as file_local:  # open a file in read mode (r)
        todos_local = file_local .readlines()  # save the items into todos list
    return todos_local


while True:
    user_action = input("Type add or show, edit, complete or exit: ")
    user_action.strip()

    if user_action.startswith("add"):  # strip remove spaces
        try:
            todo = user_action[4:].strip() + "\n"

            todos = get_todos()  # save the items into todos list

            todos.append(todo.capitalize())  # Capitalize the first string from user input and append at the todos list

            with open("../todos.txt", 'w') as file:  # open a file in write mode (w)
                file.writelines(todos)  # overwrite the file with the todos list updated
        except ValueError:
            print("Invalid input")

    elif user_action.startswith("show"):

        todos = get_todos()  # save the items into todos list

        # new_todos = [item.strip('\n') for item in todos] #remove the \n from the todos list if exists - list compreensions
        for index, item in enumerate(todos):
            item = item.strip(
                '\n')  # remove the break line from the item (read mode) to avoid double break lines (1 from the file, other from the for loop)
            row = f"{index + 1}-{item}"  # concatenate varaibles with strings using F"String
            print(row)  # show the items

    elif user_action.startswith("edit"):
        try:
            number = user_action[4:].strip()
            number = int(number) - 1

            todos = get_todos()  # save the items into todos list

            new_todo = input("Enter the new Todo: ") + "\n"  # Get he input from the user and add a break line "\n"
            todos[number] = new_todo.capitalize()  # In batch, put the first charachter of each string in upper case

            with open("../todos.txt", 'w') as file:  # open a file in write mode (w)
                file.writelines(todos)  # overwrite the file with the todos list updated

        except ValueError:
            print("Invalid input")
            continue

    elif user_action.startswith("complete"):
        try:
            number = user_action[8:].strip()

            todos = get_todos()  # save the items into todos list

            index = int(number) - 1  #create and load a variable with the item index to be removed

            todo_to_remove = todos[index].strip('\n')  # save the item that will be removed

            todos.pop(index)  # remove from the list the item choosen by the user

            with open("../todos.txt", 'w') as file:  # open a file in write mode (w)
                file.writelines(todos)  # overwrite the file with the todos list updated

            message = f"The item {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with the given number")
            continue
        except ValueError:
            print("Wrong input")
            continue

    elif 'exit' in user_action:
        break

    else:
        print("Hey, you have entered a wrong option")
print("Bye")