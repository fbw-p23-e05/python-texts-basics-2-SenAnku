# Task 1

text = "Berlin is a world city of culture, politics, media and science."
print(len(text))

# Task 2 

text = "Berlin is a world city of culture, politics, media and science."

firstChar = text[0]
lastChar = text[-1]

print(firstChar, lastChar)

# Task 3

text = "Berlin is a world city of culture, politics, media and science."

first_three = text[0:3]
print(first_three.upper())


# Task 4

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"

print("B appears:", text.count("B"),"times")


# Task 5

text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

lastTenChar = text[-10:]

print("Last ten characters:",lastTenChar)


# Task 6

text = "---Python programming---"
print(text.replace("-",""))

# Task 7

Firstname = "Sena"
Lastname = "Adigbo"

print(f"Firstname:{Firstname}\n Lastname: {Lastname}")