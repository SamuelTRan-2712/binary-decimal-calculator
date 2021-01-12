def hex2dec (hex_num: str) -> str:
    conversion_table1 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hex_num.strip().upper()
    dec_temp = 0

    power = len(hex_num[-1])

    for digit in hex_num:
        dec_temp += conversion_table1[digit] * 16 ** power
        power = power - 1
    return (dec_temp)

def decTohex(n):
    conversion_table2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
    if(n <= 0):
        return ''
    remainder = n%16
    return  decTohex(n//16)+conversion_table2[remainder]


# Function for converting decimal to binary
def float_bin(my_number, places=3):
    my_whole, my_dec = str(my_number).split(".")
    my_whole = int(my_whole)
    res = (str(bin(my_whole)) + ".").replace('0b', '')

    for x in range(places):
        my_dec = str('0.') + str(my_dec)
        temp = '%1.20f' % (float(my_dec) * 2)
        my_whole, my_dec = temp.split(".")
        res += my_whole
    return res


def IEEE754(n):
    # identifying whether the number
    # is positive or negative
    sign = 0
    if n < 0:
        sign = 1
        n = n * (-1)
    p = 30
    # convert float to binary
    dec = float_bin(n, places=p)

    dotPlace = dec.find('.')
    onePlace = dec.find('1')
    # finding the mantissa
    if onePlace > dotPlace:
        dec = dec.replace(".", "")
        onePlace -= 1
        dotPlace -= 1
    elif onePlace < dotPlace:
        dec = dec.replace(".", "")
        dotPlace -= 1
    mantissa = dec[onePlace + 1:]

    # calculating the exponent(E)
    exponent = dotPlace - onePlace
    exponent_bits = exponent + 127

    # converting the exponent from
    # decimal to binary
    exponent_bits = bin(exponent_bits).replace("0b", '')

    mantissa = mantissa[0:23]

    # the IEEE754 notation in binary
    final = str(sign) + exponent_bits.zfill(8) + mantissa

    # convert the binary to hexadecimal
    hstr = '%0*X' % ((len(final) + 3) // 4, int(final, 2))
    #hstr = '0x%0*X' % ((len(final) + 3) // 4, int(final, 2)) is if you want to have '0x' in front of hex num
    return (hstr)


# Driver Code
if __name__ == "__main__":
    print(IEEE754(263.3)) #test the IEE754 format
    print(IEEE754(-263.3))

print(hex2dec('34'))
print(decTohex(12665656))