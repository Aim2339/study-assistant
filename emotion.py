def detect_emotion():

    text = input("How are you feeling today? ").lower()

    if "tired" in text or "sleepy" in text or "exhausted" in text:
        emotion = "Tired"
        suggestion = "Study easy subjects and revise notes."

    elif "stress" in text or "stressed" in text or "worried" in text:
        emotion = "Stressed"
        suggestion = "Focus on revision instead of learning new topics."

    elif "happy" in text or "motivated" in text or "excited" in text:
        emotion = "Motivated"
        suggestion = "Start with the hardest subject."

    elif "sad" in text or "low" in text or "depressed" in text:
        emotion = "Low"
        suggestion = "Start with light study and build momentum."

    else:
        emotion = "Neutral (or not sure)"
        suggestion = "Follow your regular study plan."

    print("\nDetected Mood:", emotion)
    print("Study Suggestion:", suggestion)