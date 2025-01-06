
while True:
    user_action = input("Type add or show, edit, complete or exit: ")

    match user_action.strip():                          # strip remove spaces
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open("../todos.txt",'r') as file:      # open a file in read mode (r)
                todos = file.readlines()                # save the items into todos list
            
            todos.append(todo.capitalize())             #Capitalize the first string from user input and append at the todos list
            
            with open("../todos.txt",'w') as file:      # open a file in write mode (w)
                file.writelines(todos)                  #overwrite the file with the todos list updated

        case 'show':
            with open("../todos.txt", "r") as file:
                todos = file.readlines()

            #new_todos = [item.strip('\n') for item in todos] #remove the \n from the todos list if exists - list compreensions
            for index,item in enumerate(todos):
                item = item.strip('\n')                     # remove the break line from the item (read mode) to avoid double break lines (1 from the file, other from the for loop)
                row = f"{index+1}-{item}"                   # concatenate varaibles with strings using F"String
                print(row)                                  # show the items
        
        case 'edit':
            number = int(input("Number of the TODO to edit: "))
            number = number - 1
            
            with open("../todos.txt", "r") as file:         # open a file in read mode (r)
                todos = file.readlines()                    #load all data from the file into a list called todos[]

            new_todo = input("Enter the new Todo: ") + "\n" # Get he input from the user and add a break line "\n" 
            todos[number] = new_todo.capitalize()           # In batch, put the first charachter of each string in upper case 

            with open("../todos.txt",'w') as file:          # open a file in write mode (w)
                file.writelines(todos)                      #overwrite the file with the todos list updated

        case 'complete':
            number = int(input("Number of the TODO to Complete: "))# receive the item number to be removed from user
            
            with open("../todos.txt", "r") as file:     # open a file in read mode (r)
                todos = file.readlines()                #load all data from the file into a list called todos[]
            index = number -1                           # create and load a variable with the item index to be removed

            todo_to_remove = todos[index].strip('\n')   # save the item that will be removed
            
            todos.pop(index)                            #remove from the list the item choosen by the user

            with open("../todos.txt",'w') as file:      # open a file in write mode (w)
                file.writelines(todos)                  #overwrite the file with the todos list updated

            message = f"The item {todo_to_remove} was removed from the list"
            print(message)

        case 'exit':
            break
        case _:
            print("Hey, you have entered a wrong option")
print ("Bye")