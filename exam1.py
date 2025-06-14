print("welcme to the Bill splittr App!")

people = int(input("Enter number of people."))
if people <= 0:
  print("invalid nuber of people") 
  exit()

bill = float(input("Enter tatol bill amount"))
if bill < 0:
  print("invalid bill amount")
  exit()
   
tip_percent = int(input("Enter tip percentage (0,5,10,15,20):"))
if tip_percent not in[0, 5, 10, 20]:
  print("invalid tip percentage.")
  exit()

  tip = (tip_percent/100) * bill
  final_bill = bill + tip_amount
  per_person = final_bill / people

  print("tip_percentege / 100") * bill