# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('Adam')
degrees = float(input("what tempreture is it in degree celcius"))
print(f"it is {degrees * 1.8 + 32} farenhight and {degrees} degree celcius")
bat = int(1014)
notout = int(162)
runs = int(48426)
print(runs / (bat - notout))
people = int(input("how many people"))
groups = people // 24
left = people % 24
print(f"this many full group {groups} and {left} this is leftover")