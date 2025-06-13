# marks

subject = input("Enter name of sbject:" )
marks1 = float(input(f"Enter marks for {subject}:"))

subject = input("Enter name of sbject:" )
marks2 = float(input(f"Enter marks for {subject}:"))

subject = input("Enter name of sbject:" )
marks3 = float(input(f"Enter marks for {subject}:"))

total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3

if average_marks >= 90:
    print(" Grade A ")
elif average_marks >= 75:
    print(" Grade B ")
elif average_marks >= 60:
    print(" Grade C ")
elif average_marks >= 40:
    print(" Grade D ")
else:
    print(" Grade F ")
