score = 0  # Variable to track the score

print("Welcome to General Knowledge Quiz!")
print("There are 3 questions. Good luck!\n")

# Question 1: Capital of France
print("Question 1: What is the capital of France?")
answer1 = input("Your answer: ").strip().lower()
if answer1 == "paris" or answer1 == "france":
    print("Correct!")
    score += 1  # Increment score variable
else:
    print("Incorrect. The answer is Paris.")

print()  # Blank line for readability

# Question 2: Largest planet
print("Question 2: What is the largest planet in our solar system?")
answer2 = input("Your answer: ").strip().lower()
if answer2 == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The answer is Jupiter.")

print()

# Question 3: Boiling point of water
print("Question 3: What is the boiling point of water in Celsius?")
answer3 = input("Your answer: ").strip().lower()
if answer3 == "100" or answer3 == "100 degrees":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The answer is 100°C.")

print()

# Control flow based on final score using if-else
print("Quiz completed!")
if score == 3:
    print("Excellent! You scored", score, "out of 3.")
elif score == 2:
    print("Good job! You scored", score, "out of 3.")
elif score == 1:
    print("Keep practicing! You scored", score, "out of 3.")
else:
    print("Try again! You scored", score, "out of 3.")