def qan_tic(): # (1)
 tic = "QAN.AX" # (2)
 print(tic) # (3)
 return tic # (4)
tic = "WES.AX" # (5)
print(tic) # (6)
qan_tic() # (7)

def qan_tic(): # (1)
 tic = "QAN.AX" # (2)
 print(tic) # (3)
 return tic # (4)
tic = "WES.AX" # (5)
print(tic) # (6)
qan_tic() # (7)

def qan_tic(): # (1)
 print(tic) # (3)
 return tic # (4)
tic = "WES.AX" # (5)
print(tic) # (6)
qan_tic() # (7)

def qan_tic():
 print(tic) # (2)
 tic = "QAN.AX" # <-- local # (1)
 return tic
tic = "WES.AX" # <-- global
qan_tic()

def mk_csv_name(tic): # (1)
 tic = tic.lower() # (2)
 tic_base = tic.split('.')[0] # (3)
 return f'{tic_base}_stk_prc.csv' # (4)
name = mk_csv_name('QAN.AX') # (5)
print(name) # (6)

def mk_csv_name(tic, show=True):
 tic = tic.lower()
 tic_base = tic.split('.')[0]
 name = f'{tic_base}_stk_prc.csv'
 if show is True:
 print(name)
 return name
name = mk_csv_name('QAN.AX')

test_list = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]
def is_even_num(lis):
 evennum = []
 for n in lis:
 if n % 2 == 0:
 evennum.append(n)
 return evennum
is_even_num(test_list)

pairs = [
 ('a', 1),
 ('b', 2),
 ('c', 3),
 ]
# Dictionary comprehension
dic = {key:value for key, value in pairs}
print(dic)


# Create a dictionary
dic = {'a': 1, 'b': 2, 'c': 3}
# Create a list of (key, val) tuples called `pairs`
pairs = []
for key, value in dic.items():
 pairs.append((key,value))
print(pairs)

dic = {'a': 1, 'b': 2, 'c': 3}
keys = {key for key in dic}
print(f'The type of {keys} is {type(keys)}')

lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
new_lst = [x**2 for x in lst if x**2>150]
print(f'the new list with value of square greater than 150 is {new_lst}')

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
result = list({i for i in numbers if i % 2 == 0})