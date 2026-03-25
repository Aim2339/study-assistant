import random


def show_tip():

    tips = [
        "Start with the hardest subject first.",
        "Study in 45-minute focused sessions.",
        "Take short breaks between subjects.",
        "Revise before learning new topics.",
        "Practice problems instead of only reading.",
        "Study at the same time daily for consistency.",
        "Remove distractions while studying.",
        "Set small achievable study goals.",
        "Review what you studied at the end of the day.",
        "Focus more on weak subjects."
    ]

    tip = random.choice(tips)

    print("\n=== AI Study Tip ===")
    print(tip)