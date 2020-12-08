
#   LINK: https://realpython.com/python-zip-function/

#   zip() is a builtin function
#>%     print(dir(__builtins__))
#   Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

a = [1, 2, 3]
zipped = zip(a)
print(zipped)
print(list(zipped))
print()

integers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped = zip(integers, letters, floats)  # Three input iterables
print(list(zipped))
print()

#   With arguments of unequal length - use length of shortest
print(list(zip(range(5), range(100))))
print(list(zip(range(100), range(5))))
print()

#   zip_longest()
from itertools import zip_longest
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
print(list(zipped))
print()

#   zip, python 3 vs 2
#   In python2, zip() returns a list
#   In python3, zip() returns an itterator
#   In python3, list(zip()) is equivelent to zip() in python2
#   In python2, itertools.izip(*iterables) is equivelent to zip() in python3
#   Alternatively, for a python3 like zip() in python2:
#>%     try:
#>%         from itertools import izip as zip
#>%     except ImportError:
#>%         pass


#   Itterating over lists in parallel
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print(f'Letter: {l}')
    print(f'Number: {n}')
print()

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
operators = ['*', '/', '+']
for l, n, o in zip(letters, numbers, operators):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print(f'Operator: {o}')
print()

#   dictionaries are ordered in python3.6+ 
dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)
print()


#   Unzipping
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(numbers)
print(letters)
print()

#   Sorting is done by first list in zip
letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data1 = list(zip(letters, numbers))
print(data1)
data1.sort()  # Sort by letters
print(data1)
data2 = list(zip(numbers, letters))
print(data2)
data2.sort()  # Sort by numbers
print(data2)
#   Or alternatively
data = sorted(zip(letters, numbers))  # Sort by letters
print(data)
data = sorted(zip(numbers, letters))  # Sort by letters
print(data)
print()

#   Sum lists element-wise using zip()
total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]
for sales, costs in zip(total_sales, prod_cost):
    profit = sales - costs
    print(f'Total profit: {profit}')
print()

#   Creating, and updating, dictionary from lists using zip,
fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
a_dict = dict(zip(fields, values))
print(a_dict)
new_job = ['Python Consultant']
field = ['job']
a_dict.update(zip(field, new_job))
print(a_dict)
print()



