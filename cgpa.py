def calculate_cgpa():

    subjects = int(input("Enter number of subjects: "))

    total = 0

    print("\nEnter grades out of 10")

    for i in range(subjects):
        grade = float(input(f"Enter grade for subject {i+1}: "))
        total += grade

    cgpa = total / subjects

    print(f"\nYour CGPA is: {round(cgpa,2)}")