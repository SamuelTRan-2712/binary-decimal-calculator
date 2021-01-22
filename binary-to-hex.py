# function to convert bin to hex non -floating
def bin_to_hex(bin_num: str) -> object:
    # python is so gay and I cant directly cast binary to hex, so what I did is to input the string, then convert the
    # string to an integer
    bin_num = int(bin_num, 2)

    # then convert the given decimal to hex
    bin_num = hex(bin_num)

    # get rid of the '0x' in front
    bin_num = bin_num.replace('0x', '')

    # switch all lower case to upper
    bin_num = bin_num.upper()
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


def toBin(hex):
    # initiate all the possible value for hex, which is equivalent to each of the case here
    bins = {'1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000',
            '9': '1001',
            'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111', '.': '.'}

    # initiate bin as a string with 0 element
    bin = ''

    # initiate digits as hex number, for exp: a,b,c,d,e,...
    digits = hex.lower()

    # loop to convert hex to dec
    for index in range(len(hex)):
        if index == 0:

            # initiate the substring, which is the first digit in hex value, for example: here I pass 2ab.ef. Then
            # substring = 0010 here = 2 in hex
            substring = bins[digits[0]]

            # loop to get rid of redundant 0s, all 0s that are located before the first number '1' doesnt matter and
            # need to get rid of
            for subindex in range(len(substring)):

                # this statement actually just add string that dont start with 0 as the value of the first subindex,
                # after detect to pass over the 0, the substring will start rightover with subindex with the value of 1
                if substring[subindex] == '1':
                    # add the original string which is bin = '' with the substring, which is now got rid of redundant
                    # 0s in the front
                    bin = bin + substring[subindex:]
                    break
        else:
            # this is after the first digits, just keep adding the rest of the string, which is whatever index input
            # in hex and being converted to decimal
            bin = bin + bins[digits[index]]

    return bin


# this is just the function for the inputs to detect if they have the floating point,... but, it doesnt matter,
# regardless the function, the code works perfectly 
def if_function(bin_fking_num: str):
    if "." in str(bin_fking_num):
        return BinaryTo_Hex(bin_fking_num)
    else:
        return bin_to_hex(bin_fking_num)


print(bin_to_hex('11011'))
print(BinaryTo_Hex('1110101.1'))
print(toBin('2ab.ef'))
