import numpy as np

# ==========================================
# STUDENTS MARKS ANALYSIS USING NUMPY
# ==========================================


# Students names
students = np.array([
      "Aman",
      "Riya",
      "Rahul",
      "Priya",
      "Karan",
])

# Subjects 
subjects = np.array([
       "Python",
       "Maths",
       "Statistics",
        "SQL",
        "AI"
])

# Marks 
marks = np.array([
        [78,85,90,67,88],
        [56,72,65,70,60],
        [92,95,89,94,90],
        [45,55,60,50,48],
        [80,76,85,89,91]
])



# =======================================
# 1. BASIC INFORMATION
# =======================================

print("============= BASIC INFORMATION =============")

print("Students :")
print(students)

print("\nSubjects :")
print(subjects)

print("\nMarks :")
print(marks)

print("\nShape of marks :", marks.shape)
print("Number of students :", marks.shape[0])
print("Number of subjects :", marks.shape[1])



# =======================================
# 2. TOTAL MARKS OF EACH STUDENT
# =======================================

print("\n=========== TOTAL MARKS ============")

total_marks = np.sum(marks , axis = 1)

for i in range(len(students)):
    print(students[i], ":", total_marks[i])



# =========================================
# 3. AVERAGE MARKS OF EACH STUDENT
# =========================================

print("\n============ STUDENT AVERAGE ===========")

student_average = np.mean(marks , axis = 1)

for i in range(len(students)) :
    print(students[i], ":" , round(student_average[i], 2))



# ==========================================
# 4. HIGHEST AND LOWEST SCORER
# ==========================================

print("\n============ TOPPER ===========")

topper_index = np.argmax(student_average)
print(
    "Topper :",
    students[topper_index],
    "with average :",
    round(student_average[topper_index], 2)
)

lowest_index = np.argmin(student_average)

print(
     "Lower :",
     students[lowest_index],
     "with average :",
     round(student_average[lowest_index], 2)
)



# =======================================
# 5. SUBJECT-WISE AVERAGE
# ======================================

print("\n============== SUBJECT-WISE AVERAGE ============")

subject_average = np.mean(marks, axis = 0)

for i in range(len(students)):
    print(subjects[i], ":", round(subject_average[i], 2))



# ==========================================
# 6. HIGHEST MARKS IN EACH SUBJECT
# ==========================================

print("\n=========== HIGHEST MARKS IN EACH SUBJECT===========")

highest_subject_marks = np.min(marks , axis=0)

for i in range(len(subjects)):
    print(subjects[i], ":", highest_subject_marks[i])



# ===========================================
# 7. LOWEST MARKS IN EACH SUBJECT
# ============================================

print("\n============ LOWEST MARKS IN EACH SUBJECT =============")

lowest_subject_marks = np.min(marks , axis=0)

for i in range(len(subjects)):
    print(subjects[i], ":", lowest_subject_marks[i])



# ========================================
# 8. OVERALL HIGHEST AND LOWEST MARKS
# =========================================

print("\n============ OVERALL MARKS ============")

print("Highest marks :", np.max(marks))
print("Lowest marks :", np.min(marks))



# ======================================
# 9. STUDENTS WHO SCORE ABOVE 75 
# =======================================

print("\n========== STUDENTS WITH AVERAGE ABOVE 75 ==========")

high_performers = students[student_average > 75]

print(high_performers)



# ======================================
# 10. STUDENTS WHO SCORED BELOW 60
# =======================================

print("\n========== STUDENTS WITH AVERAGE BELOW 60 ==========")

low_performers = students[student_average < 60]

print(low_performers)




# ========================================
# 11. PASS / FAIL
# =========================================

print("\n========== PASS / FAIL ==========")

# Students passed if average >= 50

passed = student_average >= 50

for i in range(len(students)):

    if passed[i]:
        print(students[i], ": PASS")
    else :
        print(students[i], ": FAIL")



# =========================================
# 12. STANDARD DEVIATION
# ========================================

print("\n========== STANDARD DEVIATION ===========")

print("Overall nedian :", np.median(marks))



# ========================================
# 14. SORT STUDENTS BY AVERAGE
# =========================================

print("\n========== STUDENTS RANKING ==========")

ranking = np.argsort(student_average)[::-1]

rank = 1

for index in ranking :

    print(
        rank,
        ".",
        students[index],
        ".",
        round(student_average[index] , 2)
    )
    rank += 1



# ========================================
# 15. SUBJECT WITH HIGHEST AVERAGE
# ========================================

print("\n========== BEST SUBJECT ==========")

best_subject_index = np.argmax(subject_average)

print(
    "Best performing subject :",
    subjects[best_subject_index],
    "with average :",
    round(subject_average[best_subject_index], 2)
)



# ========================================
# 16. SUBJECT WITH LOWEST AVERAGE
# =========================================

worst_subject_index = np.argmin(student_average)

print(
    "Lowest performing subject :",
    subjects[worst_subject_index],
    "with average :",
    round(subject_average[worst_subject_index], 2)
)
