def decimalToBinary(number):

    if (number > 1):
        decimalToBinary(number // 2)
    print(number % 2, end = '')

r = int(input("Please input the number in decimal: "))
print("The number in binary is:", end = ' ')
a = decimalToBinary(r)
print(end = "\n")

b = input("Please enter a binary number: ")
print ("The number in decimal is:",int(b,2))
