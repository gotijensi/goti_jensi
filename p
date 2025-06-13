print ("Welcome to the pattern and number analyzer")
print(" ")

print("Select an option: ")
print("1. right-angled triangle")
print("2. Pyramid")
print("3. left-angled triangle")
print("4. Analyze a range of Numbers")
choice = int(input("Enter your choice: "))
print(" ")

if choice == 1:

    row =int(input("Enter the number of rows for the pattern: "))
    print(" ")

    print("pattern: ")

    for i in range(1 , row + 1):
            print("*" * i)

elif choice == 2:

    row =int(input("Enter the number of rows for the pattern: "))
    print(" ")
   print("pattern: ")
    for i in range(1 , row + 1):
           print(" " * (row - i) + "*" * (2*i  -1))

elif choice == 3:

   row =int(input("Enter the number of rows for the pattern: "))
    print(" ")

    print("pattern: ")
    for i in range(1 , row + 1):
           print(" " * (row - i) + "*" * i)

elif choice == 4:

    start = int(input("Enter the start of the range:"))
    end = int(input("Enter the end of the range:"))
    total = 0
    for i in range(start , end + 1):
       if i % 2 == 0:
           print("Number", i , "us even")
       else:
            print("Number", i , "us odd")
        total = total +i
     print("Sum of all numbers from" , start , "to" , end , "is:" , total)

else:
    print ("invalid choice")
    print(" ")

print("Select an option: ")
print("1. right-angled triangle")
print("2. Pyramid")
print("3. left-angled triangle")
print("4. Analyze a range of Numbers")
choice = int(input("Enter your choice: "))

if choice == 1:

    row =int(input("Enter the number of rows for the pattern: "))
    print(" ")

    print("pattern: ")

    for i in range(1 , row + 1):
            print("*" * i)
 
elif choice == 2:

    row =int(input("Enter the number of rows for the pattern: "))
    print(" ")

    print("pattern: ")
    for i in range(1 , row + 1):
            print(" " * (row - i) + "*" * (2*i  -1))

elif choice == 3:

    row =int(input("Enter the number of rows for the pattern: "))
    print(" ")

    print("pattern: ")
    for i in range(1 , row + 1):
            print(" " * (row - i) + "*" * i)
 
elif choice == 4:

    start = int(input("Enter the start of the range:"))
    end = int(input("Enter the end of the range:"))
    total = 0
    for i in range(start , end + 1):
        if i % 2 == 0:
            print("Number", i , "us even")
        else:
            print("Number", i , "us odd")
        total = total +i
    print("Sum of all numbers from" , start , "to" , end , "is:" , total)

else:
    print ("invalid choice")
    print(" ")

print("Select an option: ")
print("1. right-angled triangle")
print("2. Pyramid")
print("3. left-angled triangle")
print("4. Analyze a range of Numbers")
choice = int(input("Enter your choice: "))

if choice == 1:

    row =int(input("Enter the number of rows for the pattern: "))
    print(" ")

    print("pattern: ")

    for i in range(1 , row + 1):
            print("*" * i)
 
elif choice == 2:

    row =int(input("Enter the number of rows for the pattern: "))
    print(" ")

    print("pattern: ")
    for i in range(1 , row + 1):
            print(" " * (row - i) + "*" * (2*i  -1))

elif choice == 3:

    row =int(input("Enter the number of rows for the pattern: "))
    print(" ")

    print("pattern: ")
    for i in range(1 , row + 1):
           print(" " * (row - i) + "*" * i)

elif choice == 4:

    start = int(input("Enter the start of the range:"))
    end = int(input("Enter the end of the range:"))
    total = 0
   for i in range(start , end + 1):
       if i % 2 == 0:
            print("Number", i , "us even")
        else:
           print("Number", i , "us odd")
        total = total +i
    print("Sum of all numbers from" , start , "to" , end , "is:" , total)

else:
    print ("invalid choice")
    print(" ")

print("Select an option: ")
print("1. right-angled triangle")
print("2. Pyramid")
print("3. left-angled triangle")
print("4. Analyze a range of Numbers")
choice = int(input("Enter your choice: "))

if choice == 1:

    row =int(input("Enter the number of rows for the pattern: "))
    print(" ")

    print("pattern: ")

     for i in range(1 , row + 1):
           print("*" * i)
 
elif choice == 2:

    row =int(input("Enter the number of rows for the pattern: "))
    print(" ")

    print("pattern: ")
    for i in range(1 , row + 1):
            print(" " * (row - i) + "*" * (2*i  -1))

elif choice == 3:

    row =int(input("Enter the number of rows for the pattern: "))
    print(" ")

    print("pattern: ")
    for i in range(1 , row + 1):
            print(" " * (row - i) + "*" * i)

elif choice == 4:

    start = int(input("Enter the start of the range:"))
    end = int(input("Enter the end of the range:"))
    total = 0
    for i in range(start , end + 1):
        if i % 2 == 0:
            print("Number", i , "us even")
        else:
            print("Number", i , "us odd")
        total = total +i
    print("Sum of all numbers from" , start , "to" , end , "is:" , total)

else:
    print ("invalid choice")
    print(" ")
