# Break Statement in python

#for i in range(1 , 6):
#     if i ==4:
#        break
#  print("For Loop : " , i)

# continue Statement in python

#for i in range(1 , 6 ):
#    if i == 4:
#        continue
#    print("For Loop : " , i)
    

# Break and continue in Nested loop

# for i in range(1 , 4):
#   for j in range(1 , 2):
#      if j == 2:
#         break
#   print("j loop: " , j)
#   print("i loop: " , i)

# for i in range(1 , 4):
#    print("i loop: " , i)
#    for j in range(2):
#       if i == 2:
#           break
#        print("j loop: " , j)

# 1 pattern print in python

# for i in range(1 , 7):
#    for j in range(1 , i):
#        print(f"{j}" , end="")
#    print()

# 3 pattern
for i in range(1 , 7):
   for j in range(i):
       print(f"{i}" , end="")
   print()

# 2 pattern
#for i in range (6):
#    for j in range(i ,-1 , -1):
#        print(f"{j+1}" , end="")
#    print()

#4 pattern

#for i in range (6):
#    for j in range(i+1 ):
#        print(f"{6-i}" , end="")
#    print()

# 5 pattern
#  for i in range (6):
# for j in range(i , -1 , -1):
#         print(f"{6-j}" , end="")
#     print()

# 6 pattern
# for i in range (6):
#   for j in range(i+1):
#       print(f"{6-j}" , end="")
#   print()
