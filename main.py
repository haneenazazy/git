
# Smart Student Grade Management System
# Python Final Task - 2nd Year CS Student
# ==========================================

# قائمة لتخزين بيانات الطلاب (List of Dictionaries)
students_list = []

# دالة لحساب التقدير بناءً على الدرجة (تستخدم الشروط If/Elif/Else)
def calculate_grade(score):
    if score >= 90:
        return "A (Excellent)"
    elif score >= 80:
        return "B (Very Good)"
    elif score >= 70:
        return "C (Good)"
    elif score >= 60:
        return "D (Pass)"
    else:
        return "F (Fail)"

# دالة لإضافة طالب جديد (تستخدم Input و Variables)
def add_student():
    print("\n--- Add New Student ---")
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    
    # حماية الكود لو المستخدم دخل حروف مكان الأرقام
    try:
        score = float(input("Enter student score (0-100): "))
    except ValueError:
        print("Error: Please enter a valid numerical score!\n")
        return

    # حساب التقدير
    grade = calculate_grade(score)

    # تخزين بيانات الطالب في Dictionary
    student_dict = {
        "name": name,
        "id": student_id,
        "score": score,
        "grade": grade
    }

    # إضافة الـ Dictionary داخل الـ List
    students_list.append(student_dict)
    print(f"Success: Student '{name}' has been added successfully!\n")

# دالة لعرض جميع الطلاب (تستخدم For Loop)
def view_students():
    if not students_list:
        print("\nNotice: No students registered in the system yet.\n")
        return

    print("\n==============================")
    print("      ALL STUDENTS REPORT     ")
    print("==============================")
    for student in students_list:
        print(f"Name  : {student['name']}")
        print(f"ID    : {student['id']}")
        print(f"Score : {student['score']}")
        print(f"Grade : {student['grade']}")
        print("-" * 30)
    print()

# الدالة الرئيسية للبرنامج (تستخدم While Loop و Menu)
def main():
    while True:
        print("=== Smart Student System ===")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Exit Program")
        
        choice = input("Choose an option (1, 2, or 3): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("\nExiting program. Good luck with the team task, you've got this!")
            break
        else:
            print("\nInvalid choice! Please choose 1, 2, or 3.\n")

# 
if __name__=="__main__":
      main()