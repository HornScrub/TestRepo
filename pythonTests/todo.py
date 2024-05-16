# This program is a simple To-Do list application.
# This will help me practice fundamental concepts like data structures, user input validation, and basic file handling.

################################################################

# Features

#   1) Add Tasks
#   2) View Tasks
#   3) Mark Tasks as Completed
#   4) Remove Tasks
#   5) Save Tasks to File
#   6) Load Tasks from File

################################################################

# Function Definitions

# add_task(list aList) - This function will take in a list and append a single dictionary based on user input, returning the list 
def add_task(aList: list):
    while True:
        # Prompt use to enter task description
        description = input("Enter task description you want to add: ")

        if description:
            break # Input is good to go
        else:
            print("Please enter valid task description!")

    # Create task dictionary. We will assign the completed status to False as default
    new_task = {"description": description, "completed": False}

    # Add the new task to the list
    aList.append(new_task)

# view_tasks(list aList) - This function will take in a list and print each task in the list, with an 'X' if the task is completed and an 'O' if the task is not completed.
def view_tasks(aList: str):
    # Iterate through the list and print each task
    for task in aList:
        completed = bool(task["completed"])
        if completed:
            statusStr = 'X'
        else:
            statusStr = 'O'

        print(statusStr, " - ", task["description"], sep='')

# mark_completed(list aList) - This function takes in a list and will change the value of bool value of a user input key from True to False
def mark_completed(aList: list):

    aDescription = input("Enter task description you want to mark completed: ")

    # Iterate through the list and find the task with the matching description
    for task in aList:
        if task["description"] == aDescription:
            task["completed"] = True
            changed = True
            # This break statement will end the for loop prematurely if we find a successful match.
            break
    else:
        print("Task not found.")

# remove_task(list aList, str aDescription) - This function takes in a list and will remove the task with the matching description
def remove_task(aList: list):

    aDescription = input("Enter task description: ")

    # Iterate through the list and find the task with the matching description
    for task in aList:
        if task["description"] == aDescription:
            aList.remove(task)
            print("Task removed.")
            break
    else:
        print("Task not found.")

# save_tasks(list aList, str aFileName) - This function takes in a list and a file name and will save the list to the file
def save_tasks(aList: list, aFileName: str):
    # Open the file for writing
    file = open(aFileName, "w")

    # Iterate through the list and write each task to the file
    for task in aList:
            file.write(task["description"] + " " + str(task["completed"]) + "\n")
        
     # Close the file
    file.close()

# load_tasks(str aFileName) - This function creates a list of dictionaries from info stored in a text file and returns a list of dictionaries
def load_tasks(aFileName: str):
    try:
        # Open the file for reading
        with open(aFileName, "r") as file:
            newToDoList = []
            
            # Read the file line by line
            for line in file:
                # Split the line into a list of words
                words = line.rsplit(maxsplit=1)
                # Convert string prepresentation of "completed" to a boolean value
                completed = True if words[1] == "True" else False
                # Create a new task dictionary
                new_task = {"description": words[0], "completed": completed}
                # Add the new task to the list
                newToDoList.append(new_task)
    except FileNotFoundError:
        #If the file doesn't exist, create a new file and return an empty list
        with open(aFileName, "w") as file:
            return []
    except IndexError:
        #If the file does exist and has nothing in it, return an empty list
            return[]

    return newToDoList


def main():
    # Print the welcome message
    print("Welcome to your To-Do list!\n\n")

    # Load the task file, or create a new empty one if it doesn't exist
    toDoFile = "ToDoList.txt"
    toDoList = load_tasks(toDoFile)

    print(toDoList)


    # Prompt the user to enter a command
    command = '0'
    while command != '5':
        # Stage the To-Do List
        print("To-Do List:")
        if not toDoList:
            print("Your list is empty!\n")
        else:
            view_tasks(toDoList)
        command = input("1) Add Task\t2) Mark Task as Completed\n3) Remove Task\t4) Save Changes\n5) Quit Program\n\nEnter choice to continue: ")
        if command == '1':
            add_task(toDoList)
            print("Task added.")
        elif command == '2':
            mark_completed(toDoList)
        elif command == '3':
            remove_task(toDoList)
        elif command == '4':
            print(toDoList)
            save_tasks(toDoList, toDoFile)
            print("Changes saved.")
    
    print("Goodbye!")


# __name__ is a built-in variable in Python. When a Python script is executed, Python sets the __name__ variable to '__main__' if the script is being run as the main program. If it is being imported as a module into another script, '__name__' is set to the name of the module (todo.py).
# This 'if __name__ == '__main__':' condition checks if the current script is being run as the main program. If it is, it executes the code inside the block, i.e. main(), the todo.py. If we were to import this script into another script, we don't necessarily want it running immediately, so this code keeps it from running until the script asks it to run.

if __name__ == '__main__':
    main()
