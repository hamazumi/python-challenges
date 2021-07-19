# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    # ask for user method
    method = input("What method would you like to use?")

    # get numbers from user
    x = int(input("Enter number:"))
    y = int(input("Enter number:"))

    # define methods
    methods = {
        "add": x + y,
        "multiply": x * y,
        "divide": x / y,
        "subtract": x - y,
    }

    # What to do with chosen method key:value
    if (method in methods):
        return methods[method]
    else:
        return print("Error")


print(calculator())
