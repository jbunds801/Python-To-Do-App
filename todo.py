todo_list = []


def welcome():
    print("-" * 20)
    print("Thanks for using our ToDo App!")
    name = input("Enter your name to log in: ").strip()
    print("-" * 20)
    print(f"Welcome {name}!")


def view_tasks():
    if not todo_list:
        print("Nothing in the list. Please add tasks")
    else:
        for task in todo_list:
            print(f"-{task}")


def add_tasks():
    task = input("Add task: ").strip()
    if task:
        todo_list.append(task)
        print("Task Added!")
    else:
        print("No task entered. Please try again")


def remove_tasks():
    try:
        task = input("remove task: ").strip()
        todo_list.remove(task)
    except ValueError:
        print("That task doesn't exsist, try again.")
    else:
        print("Task removed!")
    finally:
        print("Current tasks:")
        view_tasks()


welcome()

while True:
    print("-" * 20)
    print("What would you like to do:")
    choice = input("'View', 'add', 'remove' tasks, or 'exit'?: ").strip().lower()
    print("-" * 20)
    if choice == "view":
        view_tasks()
    elif choice == "add":
        add_tasks()
    elif choice == "remove":
        remove_tasks()
    elif choice == "exit":
        print("Bye bye! Please log back in to start over")
        print("-" * 20)
        break
    else:
        print("Invalid entry: Please try again")
       