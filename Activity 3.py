num1=int(input("Enter a number "))
num2=int(input("Enter another number "))
while num2!=0:
    t=num2
    num2=num1%num2
    num1=t
hcf=num1
print("The HCF for the 2 numbers is ",hcf)