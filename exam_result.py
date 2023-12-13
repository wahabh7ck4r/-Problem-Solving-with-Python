# write a python program to check weather a student is pass of fail.Student must req 40% marks in all sub and atleast 33% in each of the subect.

def result(marks):
    student_marks = marks
    total_marks = 0
    obt_marks = 0
    failed_subjects = []

    for subject, mark in student_marks.items():
        total_marks += 100
        obt_marks += mark
        
        if mark < 33:
            failed_subjects.append(subject)

    if len(failed_subjects) > 0:
        print(f"You failed in the following subjects due to marks less than 33: {', '.join(failed_subjects)}")
        return "You failed the examination."

    overall_percentage = (obt_marks / total_marks) * 100

    if overall_percentage >= 40:
        return f"Congratulations! You passed the examination with {obt_marks} marks out of {total_marks}.\nYour overall percentage is {overall_percentage:.2f}%."
    else:
        return "You failed the examination due to an overall percentage less than 40%."


student_marks = {
    "maths": 33,
    "English": 43,
    "Computer": 54,
    "Urdu": 33,
    "physics": 90,
}

check = result(student_marks)
print(check)
