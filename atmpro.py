#use function for fast cash
def fast_cash(e_num):
    a_amount = 0
    if e_num == 1:
        a_amount = 1000
    elif e_num == 1:
        a_amount = 2000
    elif e_num == 3:
        a_amount = 5000
    elif e_num == 4:
        a_amount = 10000

    if a_amount <  balance and a_amount % 500 == 0:
        print("Please take your cash")
    else:
        print("Invalid amount entered")



print("Welcome to Nishan Bank ")
count = 4
pin_code = **** #four digit pin code
balance = 50000
while count > 0:
    pin = int(input("Please enter the pin code "))
    if pin == pin_code:
        user_choice = int(input("Enter\n 1 for Fast Cash\n 2 for Cash Withdrawal\n 3 for Balance inquiry\n"))
        match user_choice:
            case 1:
                d_amt = int(input("Enter\n 1 --- 1000\n 2 --- 2000\n 3 --- 5000\n 4 --- 10000\n ")) 
                fast_cash(d_amt)
                break  #is break required
            case 2:
                amount = (int(input("Enter the amount to withdraw ")))
                if amount < balance and amount % 500 == 0:
                    print("Please take your cash. Thank you for using Nishan Bank service")
                else:
                    print("Invalid amount entered. The amount should be less than 25000\nand a multiple of 500")
                break
            case 3:
                print(f"Your Balance is {balance}")
                break
    else:
        print("Invalid pin code ")
        count = count - 1
        print(f"You have {count} times left ")
if count == 0:
    print("Oops! You entered the wrong pin multiple times. Your Account is blocked!")





