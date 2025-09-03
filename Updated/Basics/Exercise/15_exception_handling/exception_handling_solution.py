def calculate_letter_grade(score: int) -> str:
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

try:
    user_input = input("Enter your grade (0–100): ")
    grade = int(user_input)

    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100.")

    letter = calculate_letter_grade(grade)
except ValueError as ve:
    print(f"⚠️ {ve}")
else:
    print(f"✅ Your letter grade is: {letter}")
finally:
    print("🎓 Thank you for using the Grade Calculator. Goodbye!")
