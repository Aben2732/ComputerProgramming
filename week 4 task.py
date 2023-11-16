number = int(input("pick a number between 0 and 100 inclusive"))
def numchecker(number):
    if number in range(0, 101):
        print("True")
    else:
        print("False")

numchecker(number)

word = str(input("write a word and ill tell you how many Upper and Lower case letters in it"))
def lettercheck(word):
    low = 0
    up = 0
    for x in word:
        if (x.islower()):
            low += 1
        else:
            up += 1
    print("this is how many lowercase", low)
    print("this is how many uppercase", up)

lettercheck(word)

name = str(input("hello. what is your name?"))
if name == "":
    name = "stranger"
    print(f"hello {name} how shall i learn your name")
else:
    print(f"hello {name.lower().capitalize()} nice to meet you")

    string = str(input("enter string for least character to be eaten"))


    def stringeater(string):
        if len(string) <= 1:
            print(string)
        else:
            string = string.rstrip(string[-1])
            print(string)

    stringeater(string)

faren1 = float(input("Enter temperature in Fahrenheit: "))

def fartocel(faren1):
    cel1 = (faren1 - 32) * 5/9
    print(f"{cel1} in Celsius")

cel2= float(input("Enter temperature in celcius: "))

fartocel(faren1)

def celtofar(cel2):
    faren2 = (1.8 * cel2) + 32
    print(f"{faren2} in Celsius")

celtofar(cel2)

cel3 = int(input("Enter the Temperature in Celsius"))
far3 = (1.8 * cel3) + 32
print(f"Temperature in Fahrenheit : {far3} temp in celcius cel3 {cel3}C")

list = [36,39,43,25,98.46]
print(max(list))
print(min(list))
print(sum(list)/len(list))