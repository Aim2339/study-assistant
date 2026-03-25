while True:

    print("\n=== AI Smart Study Planner ===")
    print("1. Create Study Plan")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        subjects = int(input("Enter number of subjects: "))

        subject_list = []

        for i in range(subjects):
            sub = input(f"Enter subject {i+1}: ")
            subject_list.append(sub)

        hours = int(input("Enter study hours available today: "))

        print("\n=== Your Study Plan ===")

        if hours <= 2:
            print("Focus on important subjects:")
            print("-", subject_list[0])
            print("Revise notes")

        elif hours <= 4:
            print("Study these subjects:")
            for sub in subject_list[:2]:
                print("-", sub)
            print("Take short breaks")

        else:
            print("Full Study Plan:")
            for sub in subject_list:
                print("-", sub)
            print("Practice problems and revise")


    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")