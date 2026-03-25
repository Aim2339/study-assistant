while True:

    print("\n=== AI Smart Study Planner ===")
    print("1. Create Study Plan")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        hours = int(input("Enter study hours available today: "))

        if hours <= 2:
            print("\nStudy Plan:")
            print("- Study 1 easy subject")
            print("- Revise notes")

        elif hours <= 4:
            print("\nStudy Plan:")
            print("- Study 2 subjects")
            print("- Take short breaks")
            print("- Revise important topics")

        else:
            print("\nStudy Plan:")
            print("- Study 3 subjects")
            print("- Practice problems")
            print("- Revise all topics")

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")