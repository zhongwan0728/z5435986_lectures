
f = 0.2 + 0.2 + 0.2
print(f)

i = 1
type(i) # -> <class 'int'>
f = 1.0
type(f) # -> <class 'float'>
type(1.) # -> <class 'float'>

x = str('abc')


x = str('abc')
xup = str.upper(x)
print(xup)

x = str.upper('abc')
print(x)
y = 'abc'.upper()
print(y)

weird_case = "My fUnNy tYpEcAsE sTrInG"
weird_case_lower = weird_case.upper().lower()

a = True
b = 5
print(a,b)

a = True
b = 5
print(f"The value of a is {a} and the value of b is {b}")

x = str(5)
print(x)

length = 56
width = 33
height = 30.5
volume = length * width * height
print(f"the volume of the box is {volume} cubic centimeters.")

lst = [1, 2, 3]
print(lst) t = type(lst) # --> <class 'list'>
print(t)

lst_a = [1, "string", True, None]
lst_b = ["a" , lst_a]
print(lst_b)

my_list = [ "First", "Second", "Third", "Fourth"]
# ^ ^ ^ ^
# index: 0 1 2 3
# The following raises an error because there is no item with index larger than 3 in my_list
my_list[4]











