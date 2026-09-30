# Student Result Analyzer - Skyrovix Internship Task 2
# Author: Uppiretla Pavanteja

def input_validation():
    try:
        name = input("Enter Student Name: ").strip()
        if not name:
            raise ValueError("Name empty undakudadu!")
        roll = input("Enter Roll Number: ").strip()
        subjects = int(input("Enter No. of Subjects: "))
        if subjects <= 0:
            raise ValueError("Subjects 1 kante ekkuva undali")
        marks_list = []
        for i in range(subjects):
            while True:
                try:
                    mark = int(input(f"Subject {i+1} Marks (0-100): "))
                    if 0 <= mark <= 100:
                        marks_list.append(mark)
                        break
                    else:
                        print("Marks 0-100 madhya matrame ivvu!")
                except ValueError:
                    print("Number matrame ivvu!")
        return name, roll, marks_list
    except Exception as e:
        print(f"Error: {e}")
        return None

def data_processing(marks):
    try:
        total = sum(marks)
        avg = total / len(marks)
        if avg >= 90: grade = "A+"
        elif avg >= 80: grade = "A"
        elif avg >= 70: grade = "B"
        elif avg >= 60: grade = "C"
        elif avg >= 35: grade = "D"
        else: grade = "F"
        status = "PASS" if all(m >= 35 for m in marks) else "FAIL"
        return total, avg, grade, status
    except Exception as e:
        print(f"Processing Error: {e}")
        return None

print("=== Student Result Analyzer ===")
student_data = input_validation()
if student_data:
    name, roll, marks = student_data
    result = data_processing(marks)
    if result:
        total, avg, grade, status = result
        print("\n" + "="*35)
        print(f"Name   : {name}")
        print(f"Roll   : {roll}")
        print(f"Marks  : {marks}")
        print(f"Total  : {total}")
        print(f"Avg    : {avg:.2f}%")
        print(f"Grade  : {grade}")
        print(f"Result : {status}")
        print("="*35)
