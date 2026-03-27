exams = []

def exam_manager():
    while True:

        print("\nExam Manager")
        print("1. Add Exam")
        print("2. View Exams")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            subject = input("Enter subject name: ")
            days = int(input("Days until exam: "))
            exams.append((subject, days))
            print("Exam added successfully")

        elif choice == "2":
            if not exams:
                print("No exams added")
            else:
                print("\nUpcoming Exams:")

                for exam in exams:
                    print(f"{exam[0]} - {exam[1]} days left")
        elif choice == "3":
            break
        else:
            print("Invalid choice")