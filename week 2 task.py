# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

name = input("what is name")
print(f"{name} nice to meet you")
degrees = float(input("what tempreture is it in degree celcius"))
print(f"""it is {degrees * 1.8 + 32} farenhight 
 and {degrees}" degree celcius""")
people = int(input("how many people"))
groups = people // 24
left = people % 24
print(f"this many full group {groups} and {left} this is leftover")
sweets = int(input("how many sweets?"))
students = int(input("how many students"))
leftover = sweets % students
print(f"studnets will recive{sweets // students} sweets and {leftover} is how many remain")