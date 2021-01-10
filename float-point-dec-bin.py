#function to convert decimal to binary
def decimalToBinary(number):

    if (number > 1):
        decimalToBinary(number // 2)
    print(number % 2, end = '')

# Python program to convert float
# decimal to binary number

# Function returns octal representation
def float_bin(number, places):
    # split() seperates whole number and decimal
    # part and stores it in two seperate variables
    whole, dec = str(number).split(".")

    # Convert both whole number and decimal
    # part from string type to integer type
    whole = int(whole)
    dec = int(dec)

    # Convert the whole number part to it's
    # respective binary form and remove the
    # "0b" from it.
    res = bin(whole).lstrip("0b") + "."

    # Iterate the number of times, we want
    # the number of decimal places to be
    for x in range(places):
        # Multiply the decimal value by 2
        # and seperate the whole number part
        # and decimal part
        whole, dec = str((decimal_converter(dec)) * 2).split(".")

        # Convert the decimal part
        # to integer again
        dec = int(dec)

        # Keep adding the integer parts
        # receive to the result variable
        res += whole

    return res


# Function converts the value passed as
# parameter to it's decimal representation
def decimal_converter(num):
    while num > 1:
        num /= 10
    return num


# Driver Code
n = input("Enter your choices of converting (enter N for no decimal point and F for decimal places): ")
if (n == "N"):
    r = int(input("Please input the number in decimal: "))
    print("The number in binary is:", end=' ')
    a = decimalToBinary(r)
    print(end="\n")
    b = input("Please enter a binary number: ")
    print("The number in decimal is:", int(b, 2))

if (n == "F"):
    # Take the user input for
    # the floating point number
    m = input("Enter your floating point value : ")
    # Take user input for the number of
    # decimal places user want result as
    p = int(input("Enter the number of decimal places of the result : "))
    print(float_bin(n, places=p))

