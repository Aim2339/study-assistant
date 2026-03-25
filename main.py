from planner import create_study_plan
from cgpa import calculate_cgpa


while True:

    print("\n=== AI Smart Study Assistant ===")
    print("1. Create Study Plan")
    print("2. CGPA Calculator")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_study_plan()

    elif choice == "2":
        calculate_cgpa()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")