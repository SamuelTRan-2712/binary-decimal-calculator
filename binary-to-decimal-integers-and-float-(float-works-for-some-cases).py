# helper function
def dec_to_bin_int(dec_num: str) -> str:
        bin_num = bin(int(dec_num)).replace("0b", "")
        return bin_num

# helper function
def dec_to_bin_float(num: str, places=5) -> str: # default decimal places to 5
    """"
    Function to convert a floating point decimal number to binary number
    """

    whole_list = []
    dec_list = []
    whole, dec = str(num).split('.')

    if len(dec) > places:
        places = len(dec)

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

    if (len(whole_list) > 1):
        whole_list.reverse()
    whole_list.insert(0, 1)

    # clean up decimal places
    # e.g: 11.10000 -> 11.1
    while True:
        last_ele = dec_list[-1]
        if last_ele == 0:
            dec_list.pop()
        else:
            break

    # convert result to string format
    whole_list = "".join([str(i) for i in whole_list]) # convert to a string e.g: 101
    dec_list = "".join([str(i) for i in dec_list]) # convert to a string e.g: 101
    result = whole_list + '.' + dec_list # join 2 parts

    # return result as a string
    # e.g: 11.1
    return(result)


def bin_to_dec_float(num: str):
    left_side = ""
    right_side = ""
    dec_left_side = 0
    dec_right_side = 0
    for x in range(len(num)):

        if (num[x] != '.'):
            left_side = left_side + num[x]
        else:
            right_side = num[x + 1:]
            break

    for i in range(len(left_side)):
        if (left_side[i] == '1'):
            dec_left_side = dec_left_side + 1 * 2 ** (len(left_side) - (i + 1))

        else:
            pass

    for j in range(len(right_side)):
        if (right_side[j] == '1'):
            dec_right_side = dec_right_side + 1 * 2 ** (-(j + 1))
        else:
            pass

    return (dec_left_side + dec_right_side)



# main function
def dec_to_bin(num: str) -> str:
    if "." in str(num):
        return dec_to_bin_float(num)
    else:
        return dec_to_bin_int(num)


# testing
print(dec_to_bin(2))
print(dec_to_bin(3))
print(dec_to_bin(4))
print(dec_to_bin(3.5))
print(dec_to_bin(4.25))
print(bin_to_dec_float("11110101.001010110"))