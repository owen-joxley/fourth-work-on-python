name = input("what is your name?")
age = int(input("how old are you?"))
id_number = int(input("what is your id number?"))

if age < 18:
    print(f"{name}, you are in the major league!")
else :
    print(f"{name}, you are in the minor league!")


if id_number % 2 == 0:
    print(f"{name}, you are in pacific slot!")
else :
    print(f"{name}, you are in atlantic slot!")