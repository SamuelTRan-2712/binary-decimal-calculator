# function to convert decimal to binary
def decimalToBinary(number):
    if (number > 1):
        decimalToBinary(number // 2)
    print(number % 2, end='')


def dec2bin(num):
    """"
    Function to convert a floating point decimal number to binary number
    """
    global whole_list
    global dec_list
    whole, dec = str(num).split('.')
    whole = int(whole)
    dec = int(dec)
    counter = 1

    while (whole / 2 >= 1):
        i = int(whole % 2)
        whole_list.append(i)
        whole /= 2

    decproduct = dec
    while (counter <= places):
        decproduct = decproduct * (10 ** -(len(str(decproduct))))
        decproduct *= 2
        decwhole, decdec = str(decproduct).split('.')
        decwhole = int(decwhole)
        decdec = int(decdec)
        dec_list.append(decwhole)
        decproduct = decdec
        counter += 1


n = input("Enter your choices of converting (enter N for no decimal point and F for decimal places): ")
if (n == "N"):
    r = int(input("Please input the number in decimal: "))
    print("The number in binary is:", end=' ')
    a = decimalToBinary(r)
    print(end="\n")
    b = input("Please enter a binary number: ")
    print("The number in decimal is:", int(b, 2))

if (n == "F"):
    whole_list = []
    dec_list = []
    try:
        num = float(input('Enter a floating point decimal number: '))

    except(ValueError):
        print('Please enter a valid floating point decimal')

    try:
        places = int(input('Enter the number of decimal places in the result: '))
        dec2bin(num)
        if (len(whole_list) > 1):
            whole_list.reverse()
        whole_list.insert(0, 1)


        print('The binary number of {0} is:'.format(num), end=" ")
        print(*whole_list, end='')
        print('.', end=' ')
        print(*dec_list)


    except(ValueError):
        print('Please enter a valid integer number for places')