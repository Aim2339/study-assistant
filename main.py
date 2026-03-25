from planner import create_study_plan
from cgpa import calculate_cgpa
from emotion import detect_emotion
from timetable import create_timetable

# The looping menu overshadowed the result from previous choice, so I did this
def pause():
    input("\nPress Enter to return to menu...")


while True:

    print("\n=== AI Smart Study Assistant ===")
    print("1. Create Study Plan")
    print("2. CGPA Calculator")
    print("3. Emotion Based Suggestion")
    print("4. Time Table Creator")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_study_plan()
        pause()

    elif choice == "2":
        calculate_cgpa()
        pause()

    elif choice == "3":
        detect_emotion()
        pause()

    elif choice == "4":
        create_timetable()
        pause()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")