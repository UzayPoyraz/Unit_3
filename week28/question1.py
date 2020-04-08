calc = input("Enter a sentence: ")

num = 0
let = 0

for x in calc:
    if x.isdigit():
        num += 1
    elif x.isalpha():
        let += 1

print(f"Total Numbers are: {num} Total Letters are: {let}")
