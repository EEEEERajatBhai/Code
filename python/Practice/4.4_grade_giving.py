def give_grade(marks):
    if marks <= 0 or marks >= 100 :
        print("invalid Grade")
        return -1
    else :
        if marks >= 90 and marks <= 100 :
            Grade = 'A'
        elif marks >= 80 and marks <= 89 :
            Grade = 'B'
        elif marks >= 70 and marks <= 79 :
            Grade = 'C'
        elif marks >= 60 and marks <= 69 :
            Grade = 'D'
        elif marks >= 50 and marks <= 59 :
            Grade = 'E'
        elif marks >= 0 and marks <= 50 :
            Grade = 'F'
        return Grade
        


marks = float(input("Enter the marks:"))
Grade = give_grade(marks)
print(Grade)