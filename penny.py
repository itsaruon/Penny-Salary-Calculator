d = int(input("Enter the number of days: "))


def salary():

    
    print("Day         Pennies")
    print("-------------------------")
    x = 0.01
    calculation = 0

    
    for i in range(1,d+1):
        x = x*2
        calculation = x +calculation
        print(i,  "            ", "$ ", x)
    print("The total salary for", d, "days is: $",calculation)
    
salary()
