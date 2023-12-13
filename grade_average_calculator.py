# Create a function average_grades that takes in a tuple of student grades as input. Each grade is represented as a float. The function should calculate and return the average of all the grades.

def average_grades(greads):
    length = len(greads)
    if length == 0:
        return 0  # to avoid division of zero if tuple is empty 
    
    total_sum = sum(greads)

    avg = total_sum / length

    return avg

# test
student_grades = (98.5, 76, 88.5, 91, 84)
print(average_grades(student_grades))