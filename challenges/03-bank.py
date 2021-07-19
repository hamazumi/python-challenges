
balance = 0
done = "no"


def transaction():
    global balance
    global done

    print("Welcome to Chase bank.")

    while(done != "yes"):
        question = input('check balance, withdraw, or deposit: ')

        if(question == 'check balance'):
            print(f'Current Balance: {balance}')
            done = input("done?")
        elif(question == 'withdraw'):
            amount = int(input('Amount to withdraw:'))
            balance = balance - amount
            print(f'Current Balance: {balance}')
            done = input("done?")
        elif(question == 'deposit'):
            amount = int(input('Amount to deposit:'))
            balance = balance + amount
            print(f'Current Balance: {balance}')
            done = input("done?")

    print("Have a nice day!")


transaction()
