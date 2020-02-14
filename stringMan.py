## TO USE THIS POGRAM YOU NEED A TEXT FILE CALLED extract.txt and not necessary but you can paste the text in google classroom

file = open("extract.txt", "r")
extract = file.read()

print(extract)
#extract words by splitting by spaces
words = extract.split()
print(words)
print("Answer to Q1: ", len(words), "words")
keywords = ['house', 'worker', 'master', 'hard', 'responsible', 'skillful']
#question 2
for kwd in keywords:
    print("Checking for word {} in the text: ".format(kwd))
    print(kwd in extract)
#Q3)
name = 'john'
print(f"hello {name}")
countAlpha = 0
for letter in extract:
    if letter.isalpha():
        countAlpha += 1

print(f'there are {countAlpha} letters (a-z) out of {len(extract)} total')
#Q4 (all lower case)
print(extract.lower())

#Q5 words longer than 5
wordsLong = list(filter(lambda x: len(x)>5, words))
print(len(wordsLong))
print('#'.join(wordsLong))

for word in words:
    if len(word)>5:
        print('#', word)
#Q6
total = 0
for letter in extract:
    total += ord(letter)
print(total)

