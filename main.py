from planner import create_study_plan

while True:

    print("\n=== AI Smart Study Planner ===")
    print("1. Create Study Plan")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_study_plan()

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")