habits = {}

def add_habit():
    habit = input("Enter a habit: ").strip()
    status = input("Did you complete it today? (yes/no): ").lower()

    if status == "yes":
        habits[habit] = "Completed"
    else:
        habits[habit] = "Pending"

    print("Habit recorded!")

def show_habits():
    print("\n--- Your Habit Tracker ---")

    if not habits:
        print("No habits recorded yet.")
        return

    for habit, status in habits.items():
        print(habit, ":", status)

while True:
    print("\n1. Add habit")
    print("2. View habits")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_habit()
    elif choice == "2":
        show_habits()
    elif choice == "3":
        print("Tracker closed!")
        break
    else:
        print("Invalid option!")
