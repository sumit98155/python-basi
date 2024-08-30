conditional statement
#if-else
# player=9
# if player>=11:
#     print("your team is ready to play")
# else:
#     print("sorry...! please complete your team")
#elif: if there are more than two condition, elif condition will be required
# a= input(input("enter 1st number: "))
# b= input(input("enter 2nd number: "))
# c= input(input("enter 3rd number: "))
# if a>b and a>c:
#     print(f'{a} is the greatest number')
#     if b > c and b > a:
#         print(f'{b} is the greatest number')
#     else:
#             print(f'{c} is the greatest number')
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

if a > b and a > c:
    print(f'{a} is the greatest number..')

elif b > a and b > c:
    print(f'{b} is the greatest number')

else:
    print(f'{c} is the greatest number')

    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))
    c = int(input("Enter 3rd number : "))

    if a < b and a < c:
        print(f'{a} is the smallest number..')

    elif b < a and b < c:
        print(f'{b} is the smallest number')

    else:
        print(f'{c} is the smallest number')