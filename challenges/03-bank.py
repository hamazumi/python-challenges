
balance = 0


def transaction():
    global balance

    print("Welcome to Chase bank.")

    question = input('check balance, withdraw, or deposit: ')

    if(question == 'check balance'):
        print(f'Current Balance: {balance}')
    elif(question == 'withdraw'):
        amount = int(input('Amount to withdraw:'))
        balance = balance - amount
        print(f'Current Balance: {balance}')
    elif(question == 'deposit'):
        amount = int(input('Amount to deposit:'))
        balance = balance + amount
        print(f'Current Balance: {balance}')

    print("Have a nice day!")


transaction()
