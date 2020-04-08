i = 0
dogyear = int(input("Enter dog year"))
if (dogyear == 1):
    print("Dog is 10.5 years old")
if dogyear == 2:
    print("Dog is 21 years old")
if dogyear > 2:
    for dogyear in range(0, dogyear+1):
    i += 4
print(f"{i + 13}")
