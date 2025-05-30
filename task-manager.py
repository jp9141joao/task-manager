import time
import os

# Function to add a new task to the task list
def Add_Task(Task_List):
    os.system('cls')  # Clear the console screen (for Windows)
    Task = str(input('Enter the task you want to add\nExample: "Go to the market"\nR: '))
    Deadline = str(input('\nEnter the deadline to complete the task\nExample: "10 days" or "05/10/2023"\nR: '))
    Task_List.append([Task, Deadline])  # Add the task and deadline as a list to Task_List
    print('Task added successfully!')
    time.sleep(3)  # Pause for 3 seconds to let user see the message

# Function to delete a task from the active task list and move it to the deleted tasks list
def Delete_Task(Task_List, Deleted_Tasks_List):
    os.system('cls')  # Clear the screen
    if len(Task_List) == 0:
        print('Add at least one task to be able to delete!')
        time.sleep(3)
        return

    Task_Number = int(input('Enter the number of the task you want to delete\nR: '))
    # Validate if the input number is valid
    while Task_Number > len(Task_List) or Task_Number <= 0:
        Task_Number = int(input('\nInvalid number! Enter again the number of the task to delete\nR: '))

    Confirm = int(input(f'\nAre you sure you want to delete the task "{Task_List[Task_Number-1][0]}"?\n1- Yes\n2- No\nR: '))
    # Validate confirmation input
    while Confirm != 1 and Confirm != 2:
        Confirm = int(input(f'\nInvalid option!\nAre you sure you want to delete the task "{Task_List[Task_Number-1][0]}"?\n1- Yes\n2- No\nR: '))

    if Confirm == 1:
        # Move the task from active list to deleted list
        Deleted_Tasks_List.append(Task_List[Task_Number-1])
        Task_List.pop(Task_Number-1)
        print('Task deleted successfully!')
        time.sleep(3)

# Function to mark a task as completed, moving it to the completed tasks list
def Complete_Task(Task_List, Completed_Tasks_List):
    os.system('cls')  # Clear the screen
    if len(Task_List) == 0:
        print('Add at least one task to be able to complete it!')
        time.sleep(3)
        return

    Task_Number = int(input('Enter the number of the task you want to complete: '))
    while Task_Number > len(Task_List) or Task_Number <= 0:
        Task_Number = int(input('Invalid number! Enter again the number of the task to complete\nR: '))

    Confirm = int(input(f'\nAre you sure you want to complete the task "{Task_List[Task_Number-1][0]}"?\n1- Yes\n2- No\nR: '))
    while Confirm != 1 and Confirm != 2:
        Confirm = int(input(f'\nInvalid option!\nAre you sure you want to complete the task "{Task_List[Task_Number-1][0]}"?\n1- Yes\n2- No\nR: '))
    
    if Confirm == 1:
        Completed_Tasks_List.append(Task_List[Task_Number-1])
        Task_List.pop(Task_Number-1)
        print('Task completed successfully!')
        time.sleep(3)

# Function to display all active tasks
def View_Tasks(Task_List):
    os.system('cls')
    if len(Task_List) == 0:
        print('Add at least one task to be able to view it!')
        time.sleep(3)
        return

    print('* List of Active Tasks *')
    for i in range(len(Task_List)):
        print(f'{i+1}) Name: {Task_List[i][0]} | Deadline: {Task_List[i][1]}')
    
    Continue = int(input('\nEnter 1 to go back\nR: '))
    while Continue != 1:
        Continue = int(input('\nInvalid option! Enter 1 to go back\nR: '))

# Function to display all deleted tasks
def View_Deleted_Tasks(Deleted_Tasks_List):
    os.system('cls')
    if len(Deleted_Tasks_List) == 0:
        print('Delete at least one task to be able to view it!')
        time.sleep(3)
        return

    print('* List of Deleted Tasks *')
    for i in range(len(Deleted_Tasks_List)):
        print(f'{i+1}) {Deleted_Tasks_List[i][0]}')
    
    Continue = int(input('\nEnter 1 to go back\nR: '))
    while Continue != 1:
        Continue = int(input('\nInvalid option! Enter 1 to go back\nR: '))

# Function to display all completed tasks
def View_Completed_Tasks(Completed_Tasks_List):
    os.system('cls')
    if len(Completed_Tasks_List) == 0:
        print('Complete at least one task to be able to view it!')
        time.sleep(3)
        return

    print('* List of Completed Tasks *')
    for i in range(len(Completed_Tasks_List)):
        print(f'{i+1}) {Completed_Tasks_List[i][0]}')
    
    Continue = int(input('\nEnter 1 to go back\nR: '))
    while Continue != 1:
        Continue = int(input('\nInvalid option! Enter 1 to go back\nR: '))

# Function to modify an existing task (either its name or deadline)
def Modify_Task(Task_List):
    os.system('cls')
    if len(Task_List) == 0:
        print('Add at least one task to be able to modify it!')
        time.sleep(3)
        return

    Task_Number = int(input('Enter the number of the task you want to modify\nR: '))
    while Task_Number > len(Task_List) or Task_Number <= 0:
        Task_Number = int(input('\nInvalid number! Enter again the number of the task to modify\nR: '))

    Confirm = int(input(f'\nAre you sure you want to modify the task "Name: {Task_List[Task_Number-1][0]} | Deadline: {Task_List[Task_Number-1][1]}"?\n1- Yes\n2- No\nR: '))
    while Confirm != 1 and Confirm != 2:
        Confirm = int(input(f'\nInvalid option!\nAre you sure you want to modify the task "Name: {Task_List[Task_Number-1][0]} | Deadline: {Task_List[Task_Number-1][1]}"?\n1- Yes\n2- No\nR: '))

    if Confirm == 2:
        return
    
    # Ask what the user wants to modify: name or deadline
    Modify_Type = int(input('\nWhat do you want to modify?\n1- Name\n2- Deadline\nR: '))
    while Modify_Type != 1 and Modify_Type != 2:
        Modify_Type = int(input('\nInvalid option!\nEnter again what you want to modify\n1- Name\n2- Deadline\nR: '))
    
    if Modify_Type == 1:
        New_Value = str(input('\nEnter the new name for the task\nExample: "Go to the market"\nR: '))
        Task_List[Task_Number-1][0] = New_Value
    else:
        New_Value = str(input('\nEnter the new deadline for the task\nExample: "10 days" or "05/10/2023"\nR: '))
        Task_List[Task_Number-1][1] = New_Value

    print('Task modified successfully!')
    time.sleep(3)

# Function to recover a deleted task back to the active tasks list
def Recover_Deleted_Task(Task_List, Deleted_Tasks_List):
    os.system('cls')
    if len(Task_List) == 0:
        print('Add a task first!')
        time.sleep(3)
        return
    
    if len(Deleted_Tasks_List) == 0:
        print('Delete a task first to be able to recover it!')
        time.sleep(3)
        return

    Task_Number = int(input('Enter the number of the deleted task you want to recover\nR: '))
    while Task_Number > len(Deleted_Tasks_List) or Task_Number <= 0:
        Task_Number = int(input('\nInvalid number! Enter again the number of the deleted task you want to recover\nR: '))

    # Move the task from deleted list back to active list
    Task_List.append(Deleted_Tasks_List[Task_Number-1])
    Deleted_Tasks_List.pop(Task_Number-1)

    print('Task recovered successfully!')
    time.sleep(3)

# Function to recover a completed task back to the active tasks list
def Recover_Completed_Task(Task_List, Completed_Tasks_List):
    os.system('cls')
    if len(Task_List) == 0:
        print('Add a task first!')
        time.sleep(3)
        return
    
    if len(Completed_Tasks_List) == 0:
        print('Complete a task first to be able to recover it!')
        time.sleep(3)
        return

    Task_Number = int(input('Enter the number of the completed task you want to recover\nR: '))
    while Task_Number > len(Completed_Tasks_List) or Task_Number <= 0:
        Task_Number = int(input('\nInvalid number! Enter again the number of the completed task you want to recover\nR: '))

    # Move the task from completed list back to active list
    Task_List.append(Completed_Tasks_List[Task_Number-1])
    Completed_Tasks_List.pop(Task_Number-1)

    print('Task recovered successfully!')
    time.sleep(3)

# Main function to control the program flow with a menu
def Main():
    Task_List = []
    Completed_Tasks_List = []
    Deleted_Tasks_List = []

    while True:
        os.system('cls')  # Clear the screen before showing menu
        Option = int(input(
            '* Menu *\n'
            '1- Add task\n'
            '2- Delete task\n'
            '3- Complete a task\n'
            '4- View active tasks\n'
            '5- View deleted tasks\n'
            '6- View completed tasks\n'
            '7- Modify a task\n'
            '8- Recover a deleted task\n'
            '9- Recover a completed task\n'
            '10- Exit\nR: '
        ))

        if Option == 10:
            print('Program ended!')
            break
        elif Option == 1:
            Add_Task(Task_List)
        elif Option == 2:
            Delete_Task(Task_List, Deleted_Tasks_List)
        elif Option == 3:
            Complete_Task(Task_List, Completed_Tasks_List)
        elif Option == 4:
            View_Tasks(Task_List)
        elif Option == 5:
            View_Deleted_Tasks(Deleted_Tasks_List)
        elif Option == 6:
            View_Completed_Tasks(Completed_Tasks_List)
        elif Option == 7:
            Modify_Task(Task_List)
        elif Option == 8:
            Recover_Deleted_Task(Task_List, Deleted_Tasks_List)
        elif Option == 9:
            Recover_Completed_Task(Task_List, Completed_Tasks_List)

Main()
