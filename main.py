a=float(input("enter num:"))
b=float(input("enter num:"))


print("1.+")
print("2.-")
print("3.*")
print("4./")
print("5.%")

choice=int(input("Enter your choice:"))
if choice==1:
    print(f"the add of {a} and {b} is ",a+b)
elif choice==2:
    print(f"the sub of {a} and {b} is",a-b)
elif choice==3:
    print(f"the mul of {a} and {b} is ",a*b)
elif choice==4:
    print(f"the div of {a} and {b} is ",a/b)
elif choice==5:
    print(f"the mod of {a} and {b} is ",a%b)

