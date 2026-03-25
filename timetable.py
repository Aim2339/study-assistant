def create_timetable():

    subjects = int(input("Enter number of subjects: "))

    subject_list = []

    for i in range(subjects):
        sub = input(f"Enter subject {i+1}: ")
        subject_list.append(sub)

    subjects_per_day = int(input("\nEnter number of subjects per day: "))

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    print("\n=== Weekly Time Table ===")

    index = 0

    for day in days:
        print(f"\n{day}:")

        for i in range(subjects_per_day):
            print("-", subject_list[index % subjects])
            index += 1