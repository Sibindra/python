a = input("enter first val a:")
b = input("enter second val b:")


# menu
print("\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Exponential\n6.a Power b")

choice = input("\nEnter your choice:")

if choice == 1:
    print(a+b)

elif choice == 2:
    print(a-b)

elif choice == 3:
    print(a*b)

elif choice == 4:
    print(a/b)

elif choice == 5:
    print(a//b)

elif choice == 6:
    print(a**b)

else:
    print("Invalid choice")
