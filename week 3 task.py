name = input("hello. what is your name?")
if name == "":
    name = ("stranger")
    print(f"hello {name} how shall i learn your name")
else:
    print(f"hello {name} nice to meet you")

x = 0
badpass = ["password", "letmein", "sesame", "hello", "justinbieber"]
while x == 0:
    nopass = input("type your new password")
    password = nopass
    askpass = input("please input password")
    if askpass == password and askpass not in badpass and len(password) >= 8 and len(password) <= 12:
        print("that is a valid password")
        x = x + 1
        if x == 1:
            break
    else:
        print("password incorrect/not valid")
y = 0
mrange = range(13,0)
while y == 0:
    multiply = int(input("pick an number from 0 to 12 inclusive or -7 to list times table"))
    if multiply == -7:
       for x in mrange:
        result = 7 * x
        print(7,"*",x,"=",result)
    if multiply in range(0,12) :
        print(7 * multiply)
        y = y + 1
        if y == 1:
            break
    else:
        print("number not in standard times table try again")