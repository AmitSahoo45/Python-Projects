while(True):
    print("press 'q' to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a > 6:
            print("You entered a number greater than 6.")
        else:
            print("You entered a number less than 6.")
    except Exception as e:
        print(e)
        print("You did not enter a number.")
        continue

