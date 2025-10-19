# Taking inputs
name = input("Enter your name: ")
age = float(input("Enter your age: "))
student_class = float(input("Enter which class you are in: "))
last_result = float(input("Enter your last exam result: "))

deny_text = "🚫 Sorry, but you cannot take this test."

if student_class < 5:
    print(deny_text)
elif age < 11:
    print(deny_text)
elif last_result < 80:
    print(deny_text)
else:
    print("✅ You are ready to take the test, good luck!🍀")
