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

        hours = float(input("Enter total study hours available today: "))

        time_per_subject = hours / subjects

        print("\n=== Your Study Plan ===")

        for sub in subject_list:
            print(f"{sub} → {round(time_per_subject,2)} hours")


    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")