# function to convert bin to hex non -floating
def bin_to_hex(bin_num: str) -> object:
    # python is so gay and I cant directly cast binary to hex, so what I did is to input the string, then convert the
    # string to an integer
    bin_num = int(bin_num, 2)

    # then convert the given decimal to hex
    bin_num = hex(bin_num)

    # get rid of the '0x' in front
    bin_num = bin_num.replace('0x', '')
    return bin_num


# print(bin_to_hex('11011'))

def BinaryTo_Hex(bin: str):
    # binary number is stored in a variable bin
    # bin = '0010100011100.10010'

    # split the number based on the . and store in a list list1
    # list1[0] = 0010100011100 and list1[1] = 10010
    list1 = bin.split(".")

    # convert the decimal part in to hex
    # 0010100011100 to 0x51c and append a .
    hex1 = hex(int(list1[0], 2)) + "."

    # second part(fractional part)
    # append zeros to make the length of fractional part into multible of 4
    for i in range(4 - len(list1[1]) % 4):
        list1[1] = list1[1] + '0'

    j = 0

    # take each 4 bit and convert to hex
    # and append to the first part in hex1
    for i in range(0, len(list1[1]) // 4):
        # list1[1][j : j+4] -> take each 4 bit
        # hex(int(list1[1][j : j+4], 2)) -> convert each 4 bit in to hex1
        # hex(int(list1[1][j : j+4], 2))[2:] -> remove 0x from the convert hex value
        hex1 = hex1 + hex(int(list1[1][j: j + 4], 2))[2:]

        # increment j by 4 to take the next 4 bit
        j = j + 4

    # convert all lower case to upper
    hex1 = hex1.upper()

    # get rid of 0x before hex number
    hex1 = hex1.replace('0X', '')
    return hex1


# this is just the function for the inputs to detect if they have the floating point,... but, it doesnt matter, 
# regardless the function, the code works perfectly 
def if_function(bin_fking_num: str):
    if "." in str(bin_fking_num):
        return BinaryTo_Hex(bin_fking_num)
    else:
        return bin_to_hex(bin_fking_num)


print(bin_to_hex('11011'))
print(BinaryTo_Hex('1110101.1'))
