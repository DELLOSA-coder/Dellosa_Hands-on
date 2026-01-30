words = input("Enter a word: ")
length = len(words)
x = 0
average = 0
lista = []
while length > x:
    number = int(input("Input a number: "))
    x += 1
    lista.append(number)
    average += number
print(lista)
print(f"The length of the word is {length}")
print(f"The average is {average / length}")

if length > average:
    print(f'The length of the word "{words}" is greater than average')
elif length < average:
    print(f'The length of the word "{words}" is less than average')
else:
    print(f'The length of the word "{words}" is equal the average')

    