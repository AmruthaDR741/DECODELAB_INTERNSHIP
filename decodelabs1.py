# DecodeLabs - Project 1
# TO-DO LIST PROGRAM

# Memory (List acts like a Database Table)
tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # ========== INPUT + PROCESS ==========
    if choice == "1":
        task_name = input("Enter task name: ")

        # Creating dictionary (Table Row)
        task = {
            "id": len(tasks) + 1,
            "task": task_name
        }

        # INSERT INTO (append)
        tasks.append(task)

        print("Task added successfully!")

    # ========== OUTPUT ==========
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for t in tasks:
                print(f"{t['id']}. {t['task']}")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")