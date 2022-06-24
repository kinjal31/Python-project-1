coordinates = (3, 4)
# cant be changed/modified
print(coordinates[1])
# immutable
list1=[(1, 2),(3, 4),(5, 6)]
print(list1,coordinates)

# if

is_male= False
is_female=True
if not is_male:
    print("male")

# if
def max_num(num1, num2, num3):
    if(num1>=num2 and num1>=num3):
        return num1
    elif (num2 >= num1 and num2 >= num3):
        return num2
    else:
        return num3

print(max_num(3,4,5))


def calculator(choice,n1,n2):
    if choice == "+":
        return n1+n2
    elif choice=="-":
        return n1-n2
    elif choice=="*":
        return n1*n2
    elif choice=="/":
        return n1/n2
    else:
        return "invalid"
 # calculator
choice=input(" +,-,*,/ : ")
num1=float(input("num1 :"))
num2=float(input("num2 :"))
print(calculator(choice,num1,num2))


a=5
print(a)
a=True
print(a)
a="changed"
print(a)
