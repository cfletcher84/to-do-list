task_list = []

# Main menu will drive the apps navigation
# Will Except a Value error and pass message to try again.

def main_menu():
    while True:
        try:
            print(f"\nWelcome to the To-Do App!\n\n\nPlease select from the following options:\
              \n\n1. Add a new task.\n2. Delete a task.\n3. View Tasks\
              \n4. Quit the application.")
            user_navigation = int(input("What would you like to do? Select 1-4 : "))
            if user_navigation == 4:
                print("Thank you for using the app!")
                break
            elif user_navigation == 3:
                view_task()
            elif user_navigation == 2:
                del_task()
            elif user_navigation == 1:
                add_task()
        except ValueError:
            print("That was not a number, please select again.")

# Fuction add_task will add the desired task to users list.
# User will be able to add multiple tasks as well as none if desired.
# Function will navigate user back to main menu if no additional tasks are added.

def add_task():
    user_task = input("\nAdding a task!\n\nWhat task would you like to add? : ")
    task_list.append(user_task)
    print(f"You added {user_task} to your list!")
    another_task = input("Would you like to add more? (Y to add more, N to return to the main menu.) : ")
    if another_task == "N":
        print(f"\nSending you back to main menu!")
    elif another_task == "Y":
        add_task()
    elif another_task != "N" and another_task != "Y":
        print("You chose an invalid option. Try again")
        another_task = input("\nPress \"Y\" to add another task or \"N\" to go to the main menu? : ")
        if another_task == "Y":
            add_task()
        else:
            main_menu()
    else:
        main_menu()

# Fuction del_task will remove the desired task from users list.
# User will be able to remove multiple tasks as well as none if desired.
# Function will navigate user back to main menu if no additional tasks are not removed.



def del_task():
    user_task = input(f"Here are your current tasks:\n{task_list}\
        \nWhat would you like to remove? : ")
    if user_task not in task_list:
        print(f"\n{user_task} does not exist in your list! Returning to main menu")
        main_menu()
    else:
        task_list.remove(user_task)
        print(f"You removed {user_task} from your list!")
        another_task = input("Would you like to remove more? (Y to add more, N to return to the main menu.) : ")
        if another_task == "N":
            print("Returning you to the main menu!")
        elif another_task == "Y":
            del_task()
        elif another_task != "N" and another_task != "Y":
            print("You chose an invalid option. Try again")
            another_task = input("\nPress \"Y\" to remove another task or \"N\" to go to the main menu? : ")
            if another_task == "Y":
                del_task()
            else:
                main_menu()




def view_task():
    print(f"\nYou have the following tasks to complete!\n{task_list}")

main_menu()