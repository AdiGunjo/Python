def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def main():
    num_subjects = int(input("Enter number of subjects: "))
    marks = []
    for i in range(num_subjects):
        while True:
            mark = float(input(f"Enter marks for subject {i + 1} (out of 100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Invalid marks. Enter a value between 0 and 100.")

    total = sum(marks)
    percentage = total / num_subjects
    grade = get_grade(percentage)

    print("\nResult Card")
    print("-" * 30)
    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i}: {mark}")
    print("-" * 30)
    print(f"Total Marks = {total}/{num_subjects * 100}")
    print(f"Percentage = {percentage:.2f}%")
    print(f"Grade = {grade}")

    if grade == "F":
        print("Result: FAIL")
    else:
        print("Result: PASS")


if __name__ == "__main__":
    main()