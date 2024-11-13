#GARCIA_LAB11_GRADES

grades = []
student_count = 0

while student_count < 5:
        if student_count == 0:
            number = "1st"
        elif student_count == 1:
            number = "2nd"
        elif student_count == 2:
            number = "3rd"   
        elif student_count == 3:
            number = "4th"   
        elif student_count == 4:
            number = "5th"   
                
        grade = float(input(f"Enter grade for {number} student: "))
            
        if 40 <= grade <= 100:
            grades.append(grade)
            student_count +=1
        else:
            print("Grade must be between 40 and 100")
                            
average_grade = sum(grades) / len(grades)

print ("================================")

passing_grades = 0 
for grade in grades:
    if grade >= 75: 
        passing_grades += 1
        

passing_percentage = (passing_grades / len(grades)) * 100

print("Grades: ", grades)
print(f"Average Grade: ", average_grade)
print(f"Passing Grade: ", passing_grades)
print(f"Passing Percentage: ", passing_percentage, "%")
