def second_compliment(n: str):
    string2 = ""
    string = n

    # loop for the first compliment to flip 1 to 0 and vice versa
    for i in range(len(string)):

        # if index = 0, change it to 1
        if string[i] == '0':
            # here u cant do string[i] = "1" for some reason so I assign to a completely new string called string2,
            # basically go & fuck around the bush cuz u cant go and fk directly =)))
            string2 += "1"

        # if index is 1, change it to 0
        if string[i] == '1':
            # like I explained above, the gayness of python =)))
            string2 += "0"

    # again, u need to do 2nd compliment, but u cant change a single index of a string by using a normal format that
    # is supposed to work even in c++ : string[:i] = '1', so what I did instead is that I format the string 2 after
    # the second compliment to a list, so I can push and pull any SINGLE index of that list
    string2 = list(string2)

    # again, second compliment
    if string2[len(string2) - 1] == '0':
        # change the last index of the string to 0 if it is 1
        string2[len(string2) - 1] = '1'

    if string2[len(string2) - 1] == '1':
        # change the last index of the string to 1 if it is 0
        string2[len(string2) - 1] == '0'

    # but then string2 is a list, and I supposed users doesnt wanna see a list as a result so again, I went and
    # fucked around the bush, I called the third, completely empty string then I joined string2 and save the result in
    # string3
    string3 = ""

    # save the result here
    return string3.join(string2)

# so u see, in Python, we all need to know how to fuck around the bushes, sometimes, u cant just stab straight =)))
# it works in this function if u do print (second_compliment("11001")) but here's the thing, the program works
# perfectly with numbers like 00010 or 11001, but... unfortunately, if u throw a number like 1111, it will overflow
# lol, and the reason behind it is the bit assign, for exp, if u throw a 1111, u compliment 2nd time would result in
# 0001, but that's wrong because its overflow, what it was supposed to be was to be input as 01111 and then get
# compliment to 10001 as the first 1 is sign bit, so then, here I have modified the second function to work and it
# asks u to assign how many bits u want

# second function, this time it takes bits as an argument
def bindigits(n, bits):
    # bla bla what the flying fk whatever this is, I got it online,... so if u wanna ask, ask the one who wrote it,
    # not copied it =)))
    s = bin(n & int("1" * bits, 2))[2:]

    # bada ding bada boom, Mr. Worldwide as I step in the room, Im a hustler baby.... WTF is this equation,
    # wtf is "{0:0>%s}" and that with the rest of the line, yeah like Usher sang, Da boss in the house and no one
    # understands shit
    return ("{0:0>%s}" % bits).format(s)


print(bindigits(-7, 4))
print(second_compliment("1001011"))
