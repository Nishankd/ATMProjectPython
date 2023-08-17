print("Welcome to Nishan Bank ")
count = 4
pin_code = 1313
balance = 50000
while count > 0:
    pin = int(input("Please enter the pin code "))
    if pin == pin_code:
        user_choice = input("Enter 1 for Balance Inquiry or 2 for Cash Withdrawal ")
        match user_choice:
            case '1':
                print(f"Your Balance is {balance}")
                break
            case '2':
                amount = (int(input("Enter the amount to withdraw ")))
                if amount <= 25000 and amount % 500 == 0:
                    print("Please take your cash. Thank you for using Nishan Bank service")
                else:
                    print("Invalid amount entered. The amount should be less than 25000\nand a multiple of 500")
                break
    else:
        print("Invalid pin code ")
        count = count - 1
        print(f"You have {count} times left ")
if count == 0:
    print("Oops! You entered the wrong pin multiple times. Your Account is blocked!")





