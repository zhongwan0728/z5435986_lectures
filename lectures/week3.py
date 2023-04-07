x = str(5)
print(x)

lst1 = ['a']
print(f'This is lst1: {lst1}')
lst3 = ['b', ['a']]
print(f'This is lst3: {lst3}')
lst3[1].append('c')
print(f"This is lst3 after appending 'c': {lst3}")

happy = False
if happy is True:
 print("I am happy")
print("This will print regardless of the value of happy")

happy = True
if happy is True:
 print("I am happy")
print("This will print regardless of the value of happy")

happy = True
very_happy = True
if happy is True:
    print("I am happy") # <-- 4 spaces indentation
    if very_happy is True: # <-- 4 spaces indentation
        print("Actually, I'm really happy!") # <-- 8 spaces indentation

happy = 5
if happy:
 print("I am happy")

 a = -1
 b = True
 if a != 0:
     print("a is non-zero")
 elif b is True:
     print("b is True")
 elif a < 0 and b is True:
     print("a is negative and b is True")
 else:
     print("None of the conditions above hold")



letters_lst = ["a", "b", "c", "d"]
for letter in letters_lst:
 print(letter)

 tickers = set()
 tickers.add("QAN.AX")
 tickers.add("QAN.AX")
 tickers.add("WES.AX")
 for tic in tickers:
     print(tic)

for i in range(5,0):
 print("This will not execute because start is greater than stop.")
for i in range(5,0,-1):
 print("This message will self-destruct in {} secs...".format(i))

 letters = ["a", "b", "c", "d", "e"]
 for tup in enumerate(letters):
     print(tup)

numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
temp_largest = numbers[0]
print('Before', temp_largest)
for number in numbers:
if number > temp_largest:
temp_largest = number
print(number, temp_largest)
print(f'The largest value is {temp_largest}')

numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
largest = max(numbers)
print(f'The largest value is {largest}')

for i in range(1, 4):
 for j in range(1, 4):
 if i <= j:
 print(i, j)