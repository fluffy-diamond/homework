from datetime import datetime


name = input("Enter your name: ")
mood = input("Enter your mood (happy/sad/stressed/relaxed): ").lower()
energy = int(input("Enter your energy level (1 to 10): "))


if energy <= 3:
    print("Your energy level is very low.")


if energy >= 5:
    print("You have enough energy for the day.")
else:
    print("You may need some rest today.")


if mood == "happy":
    advice = "Keep smiling and stay positive!"
elif mood == "sad":
    advice = "Try talking to a friend or listening to music."
elif mood == "stressed":
    advice = "Take a deep breath and do something relaxing."
elif mood == "relaxed":
    advice = "Great! Keep enjoying your calm mood."
else:
    advice = "Have a balanced and peaceful day."


current_time = datetime.now()
date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")


print("\n--- Final Report ---")
print("Name:", name)
print("Mood:", mood)
print("Energy level:", energy)
print("Advice:", advice)
print("Current date and time:", date_time)