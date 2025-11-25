# habit tracker

def load_habits():
    habits = {}
    try:
        with open("habits.txt", "r") as f:
            for line in f:
                name, status = line.strip().split(",")
                habits[name] = status
    except FileNotFoundError:
        pass
    return habits

def save_habits(habits):
    with open("habits.txt", "w") as f:
        for habit, status in habits.items():
            f.write(f"{habit},{status}\n")

def show_progress(habits):
    if not habits:
        print("No habits to track yet.")
        return
    done = sum(1 for status in habits.values() if status == "done")
    total = len(habits)
    percentage = (done / total) * 100
    print(f"Progress: {done}/{total} habits completed ({percentage:.2f}%)")

def main():
    habits = load_habits()
    while True:
        print("\n1. View Habits\n2. Add Habit\n3. Mark Habit as done\n5. Delete Habit\n6. Reset All Habits\n7. Show Progress Percentage\n8. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            if not habits:
                print("No habits found.")
            else:
                for habit, status in habits.items():
                    print(f"{habit}: {'DONE' if status == 'done' else 'NOT DONE YET'}")

        elif choice == "2":
            name = input("Enter your habit name: ")
            habits[name] = "Not done"
            print(f"Added '{name}' to your habit list.")

        elif choice == "3":
            name = input("Enter habit name to mark as done: ")
            if name in habits:
                habits[name] = "done"
                print(f"'{name}' marked as completed!")
            else:
                print("Habit not found.")

        elif choice == "5":
            name = input("Enter habit name to delete: ")
            if name in habits:
                del habits[name]
                print(f"'{name}' deleted from your habit list.")
            else:
                print("Habit not found.")

        elif choice == "6":
            if habits:
                for habit in habits:
                    habits[habit] = "Not done"
                print("All habits have been reset to 'Not done'.")
            else:
                print("No habits to reset.")

        elif choice == "7":
            show_progress(habits)

        elif choice == "8":
            save_habits(habits)
            print("Progress saved, See you tomorrow!")
            break

        else:
            print("Invalid choice, try again.")

# calling the main function
if __name__ == "__main__":
    main()




