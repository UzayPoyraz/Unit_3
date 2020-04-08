I found how to do this but i cant get it to split:
word = input("Enter words to be sorted and added coma in between: ")

spliting = word.split(",")
sorting = sorted(spliting)
joining = ",".join(sorting)

print(joining)
