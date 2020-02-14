#Create an encoder program in Python. User enters a message and a integer.
msg = input("Enter a message: ")
sec = int(input("Enter a secret number: "))
for let in msg:
    print(chr(ord(let) + sec))


#The pythonic way of doing it
msg = input("Enter a message: ")
key = int(input("Enter a secret number: "))
print(''.join(map(lambda x: chr(ord(x)+key), msg)))
