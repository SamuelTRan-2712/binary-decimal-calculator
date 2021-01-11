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

print(hex2dec('34'))
print(decTohex(12665656))