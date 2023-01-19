def deposit():
    # ask for deposit until user enters valid amount
    while True:
        amount = input("enter the amount you want to deposit: Rs ")
        # digit method True if number
        #  -ve numbers are False
        if amount.isdigit():
            # convert to int
            amount = int(amount)

            if amount > 0:
                break
            else:

                print("amount must be greater than 0")
        # not a digit
        else:
            print("please enter a number")


deposit()