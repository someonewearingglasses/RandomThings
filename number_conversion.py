import random
def make_binary(d):
    return "b"
def make_octal(d):
    return "o"
def make_decimal(d):
    return "d"
def make_hexadecimal(d):
    return "h"

choices = ["binary", "octal", "decimal", "hexadecimal", "random"]
choices2 = choices.copy()
print("\nChoices:")
for i,x in enumerate(choices):
    print(f"[{i}] {x}")
choose = int(input("What type of number will be randomly generated(0-4)? "))
first = choices[choose]

if choose < 4:
    choices.remove(choices[choose])
print("\nChoices:")
for i,x in enumerate(choices):
    print(f"[{i}] {x}")
convert_to = int(input("How would you like to convert this number to? "))
second = choices[convert_to]

print("\nRules: \n 1. Convert the given number in one minute \n 2. Don't use calculator")
d = int(input("\nDifficulty(1-5): "))
listed_f = [make_binary(d), make_octal(d), make_decimal(d), make_hexadecimal(d)]
print(" ")

if choose < 4:
    print(listed_f[choose])
else:
    choices2.pop(4)
    first = random.choice(choices2)
    print(listed_f[choices2.index(first)])
    
if second == "random":
    choices.remove("random")
    second = random.choice(choices)
while first == second:
    first = random.choice(choices2)
print(f"Convert this from {first} to {second}")
