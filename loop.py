input = int(input("Enter the number of rows you want: "))
print("\n")
i = 0
star = "*       "

while i < input + 1:

    starNum = star * i
    starNum = starNum.center(125)
    print(starNum)
    starNum = "*       "
    i += 1

print("\nDone!")


