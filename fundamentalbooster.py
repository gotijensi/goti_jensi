# name, age, hight , fav num

name = input("please enter your name : ")

age = input("please enter your age : ")

height  = input("please enter your height in meters : ")

number = input("please enter your favourite number : ")

print("Thank you! Here is the information we collected : ")

print(f"name : {name} (Type : {type(name)} , Memory Address : {id(name)})")

print(f"age : {age} (Type : {type(age)} , Memory Address : {id(age)})")

print(f"height : {height} (Type : {type(height)} , Memory Address : {id(height)})")

print(f"number : {number} (Type : {type(number)} , Memory Address : {id(number)})")