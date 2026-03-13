
valueA = int(input("Enter first number: "))
valueB = int(input("Enter second number: "))

selArith = input("Enter arithmetic equations (+ ,- , *, /): ")

if(selArith == "+"):
    {
        print("The value for A + B is: ", valueA + valueB)
    }
elif(selArith == "-"):
    {
        print("The value for A - B is: ", valueA - valueB)
    }
elif(selArith == "*"):
    {
        print("The value for A * B is: ", valueA * valueB)
    }
elif(selArith == "/"):
    {
        print("The value for A / B is: ", valueA / valueB)
    }
else:
    {
        print("Invalid input given")
    }
