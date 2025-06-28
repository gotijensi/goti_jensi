print("Welcome to the Data Analyser and Transformer Program\n")

while True:
    
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion) ")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")
    
    choice = int(input("Enter your choice [ 1 to 7 ]:"))
    
    if choice == 1:

        array_input = input("\nEnter data for a 1D array (seperated by spaces) : \n")
        arr = list(map(int , array_input.split()))

        print("\nData has been stored successfully!!")
        print("\n")
    
    elif choice == 2:
        
        print("\nData Summary: ")    
        print("- Total element :" , len(arr))
        print("- Minimum value :" , min(arr))
        print("- Maximum value :" , max(arr))
        print("- Sum of all value :" , sum(arr))
        print("- Average value : " , sum(arr) / len(arr))
        print("\n")

    elif choice == 3:

        fact = int(input("\nEnter a number to Calculate its factorial :"))
        def factorial(fact):
            if fact == 1:
                return 1
            else :
                return fact * factorial(fact-1)    
        print(f"\nFactorial of {fact} is : " , factorial(fact))  
        print("\n")  


    elif choice == 4:

        num = int(input("\nEnter a threshold value to filter out data below this value:\n"))
        filtered_data = list(filter(lambda x: x >= num, arr))
        print(f"\nFiltered Data (values >= {num}):")
        print(*filtered_data, sep=", ")

        print("\n")  


    elif choice == 5:

        print("\nChoose sorting option :")
        print("1. Ascending")
        print("2. Descending")

        num = int(input("\nEnter your choice : "))
        
        if num == 1:
            sorted_arr  = sorted(arr)
            print("\nSorted data in Ascending order :\n" , sorted_arr)
            print("\n")

        elif num == 2:
            sorted_arr = sorted(arr , reverse = True)
            print("\nsort by descending order :\n" , sorted_arr)
            print("\n")

        else:
            print("\nInvalid choice! Please Enter right choice [ 1 - 2 ]!!!")
            print("\n")

    elif choice == 6:

        print("\nDataset Statistics :")

        print("- Minimum value :" , min(arr))
        print("- Maximum value :" , max(arr))
        print("- Sum of all value :" , sum(arr))
        print("- Average value : " , sum(arr) / len(arr))
        print("\n")

    elif choice == 7:
        print("\nThank you for usingthe Data Analyzer and Transformer Program. Goodbye!!")
        print("\n")
        break

    else:
        print("\nInvalid choice! Please Enter right choice [ 1 to 7 ]!!!")
        print("\n")