parrot = "Norwegian Blue"

for character in parrot:
    print(character)

number  = "9,223;372:036 854,775;807"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(values)
print(sum(int(val) for val in values))



quote = """Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?"""

for char in quote:
    if char.isupper():
        print(char)