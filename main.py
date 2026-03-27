from planner import create_study_plan
from cgpa import calculate_cgpa
from emotion import detect_emotion
from tips import show_tip
from exam import exam_manager

# The looping menu overshadowed the result from previous choice, so I did this
def pause():
    input("\nPress Enter to return to menu...")

while True:
    print("\nAI Smart Study Assistant")
    print("1. Create Study Plan")
    print("2. CGPA Calculator")
    print("3. Emotion Based Suggestion")
    print("4. Study Tips")
    print("5. Exam Manager")
    print("6. Exit")

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
        show_tip()
        pause()

    elif choice == "5":
        exam_manager()
        pause()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")