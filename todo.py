tasks=[]
while True:
    print("\n\t\tTo-Do List\t\t\n")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Exit")

    choice=input("\nEnter Your choice:")
    if choice== "1":
        task=input("Enter the task:")
        tasks.append(task)
        print("Task added successfully")
    elif choice=="2":
        if len(tasks)==0:
            print("No tasks available:")
        else:
            print("Your tasks are:\n")
            for i in tasks:
                print(i)
                print("\n")
    elif choice=="3":
        print("Thank you for using To-Do List")
        break
    else:
        print("Invalid choice")
