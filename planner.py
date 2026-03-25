def create_study_plan():
    subjects = int(input("Enter number of subjects: "))

    subject_list = []
    difficulty_list = []

    print("\nDifficulty Levels:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")

    for i in range(subjects):
        sub = input(f"\nEnter subject {i + 1}: ")
        diff = int(input("Enter difficulty (1-3): "))

        subject_list.append(sub)
        difficulty_list.append(diff)

    hours = float(input("\nEnter total study hours available today: "))

    total_weight = sum(difficulty_list)

    print("\n=== Your Smart Study Plan ===")

    for i in range(subjects):

        # Time for subject = (Subject Difficulty / Total Difficulty) × Total Study Hours

        time = (difficulty_list[i] / total_weight) * hours

        print(f"\n{subject_list[i]} → {round(time, 2)} hours")

        # Study Type Recommendation
        if difficulty_list[i] == 3:
            print("Study Method: Practice problems and deep learning")

        elif difficulty_list[i] == 2:
            print("Study Method: Revise concepts and examples")

        else:
            print("Study Method: Quick revision and notes reading")