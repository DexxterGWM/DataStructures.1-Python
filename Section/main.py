print('\n\t Data Structures in Python\n\t #Section 1')

'''
Division of groups used:
 1 - Sequence type objects: text, lists and tuples.
 2 - Set type objects.
 3 - Objects of the mapping type (dictionary).
 4 - NumPy array objects.
'''

# // Sequence Type Objects

'''
Operation     Result                                                     Note
 x in s     |  True if an item of s is equal to x, else False          |  True if an item of s is equal to x, else False
 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
 s + t      |  Concatenation of s and t                                |  Concatenates (joins) two sequences
 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
 n * s      |  Add s to itself n times                                 |  Multiply the string n times
 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
 s[i]       |  Accesses the value stored at position i of the sequence |  The first value occupies position 0
 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
 s[i:j]     |  Accesses the values ​​from position i to j                |  The j value is not included
 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
 s[i:j:k]   |  Accesses the values ​​from position i to j, with step k   |  The j value is not included
 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
 len(s)     |  Length of s                                             |  Built-in function used to know string size
 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
 min(s)     |  Smallest value of s                                     |  Built-in function used to know the smallest value of the sequence
 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
 max(s)     |  Highest value of s                                      |  Built-in function used to know the highest value of the sequence
 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
 s.count(x) |  Total number of occurrences of x in s                   |  Count how many times x was found in the sequence
'''

# // Sequence of characters

txt = 'Data Analysis with Python!'

print(
f'''
 ——————————
 len(txt): {len(txt)}
 \'Python\' in txt: {'Python' in txt}
 count(txt): {txt.count('a')}
 The first 3 letters are: {txt[0:3]}
 ——————————''')

# //

txt = 'Data with Python!'

print(
f'''
 ——————————
 {txt.upper()}
 {txt.replace('t', '*')}
 ——————————''')

# //

txt = 'Data Analysis with Python!'
words = txt.split()

print(
f'''
 ——————————
 txt = {txt}
 words = {words}
 len(txt): {len(txt)}  |  len(words): {len(words)}
 ——————————''')

# // Exemplifiing

txt = '''
String Operators
Python provides operators for processing text (i.e. string values).
Like numbers, strings can be compared using comparison operators: ==, !=, <, >, and so on.
The == operator, for example, returns True if the strings on both sides of the operator have the same value (Perkovic, p. 23, 2016).
'''

print(f'\n ——————————\n len(txt): {len(txt)}')

txt = txt.lower()
txt = txt.replace(',', '').replace('.', '').replace('(', '').replace(')', '').replace('\n', ' ')
listWords = txt.split()
total = listWords.count('string') + listWords.count('strings')

print(
f''' len(listWords): {len(listWords)}
 count(string/strings): {total}
 ——————————\n
''', end=' ——————————\n')

# // Lists

'''
 • Using a pair of square brackets to denote an empty list: list1 = [].
 • Using a pair of square brackets and elements separated by commas: list2 = ['a', 'b', 'c'].
 • Using a "list comprehension": [x for x in iterable].
 • Using the type constructor: list().
'''

# //

vowels = ['a', 'e', 'i', 'o', 'u'] # Could also have been created using double quotes

for vowel in vowels:
    print (f' Position: {vowels.index(vowel)+1}, value = {vowel}')
else: print(' ——————————')

# //

# Same result
vowels = []
print(f'\n ——————————\n Object type vowels: {type(vowels)}')

vowels = ('a e i o u').split() # Still being '<class list>'
print(f' {vowels}', end='')

for p, x in enumerate(vowels):
    print(f'\n Position = {p}, value = {x}', end='')
else: print('\n ——————————')

# //

fruits, grades = ['apple', 'banana', 'grape', 'papaya', 'apple'], [8.7, 5.2, 10, 3.5]

print(
f'''
 ——————————
 {'apple' in fruits}
 {'avocado' in fruits}
 {'avocado' not in fruits}
 {min(fruits)}
 {max(fruits)}
 {fruits.count('apple')}
 {fruits + grades}
 {2 * fruits}
 ——————————''')

# //

List = ['Python', 30.61, 'Java', 51 , ['a', 'b', 20], 'apple']
print(f'\n ——————————\n len(List): {len(List)}')

for i, item in enumerate(List):
    print(f' Position: {i},\t value: {item} ———> individual type = {type(item)}')

print(' Examples of slices:')

print(
f''' {List[1]}: {List[1]}\n {List[0:2]}: {List[0:2]}
 {List[:2]}: {List[:2]}\n {List[3:5]}: {List[3:5]}
 {List[3:6]}: {List[3:6]}\n {List[3:]}: {List[3:]}
 {List[-2]}: {List[-2]}\n {List[-1]}: {List[-1]}
 {List[4][1]}: {List[4][1]}
 ——————————''')

# // List Comprehension (List Comprehensions)

# languages = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split() # This syntax produces the same result as the one below.
languages = ['Python', 'Java', 'JavaScript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin']
print(f'\n ——————————\n Before the listcomp: {languages}')

languages = [item.lower() for item in languages]
print(f' After the listcomp: {languages}\n ——————————')

# //

languages = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
print(f'\n ——————————\n Before the listcomp: {languages}')

for i, item in enumerate(languages):
    languages[i] = item.lower()

print(f' After the listcomp: {languages}\n ——————————')

# //

languages = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
languageJava = [item for item in languages if 'Java' in item]

print(f'\n ——————————\n {languageJava}\n ——————————')

# // Functions map() and filter()

print('\n ——————————\n Example 1')
languages = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

newList = map(lambda x: x.lower(), languages)
print(f' The new list is: {newList}')

newList = list(newList)
print(f' Now yes, the new list is: {newList}')

print(' Example 2')
numbers = [0, 1, 2, 3, 4, 5]

squares = list(map(lambda x: x*x, numbers))
print(f' List with the number raised to itself: {squares}\n ——————————')

# //

numbers  = list(range(0, 21))
oddsNumbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f'\n ——————————\n {oddsNumbers}\n ——————————')

# // Tuples

'''
 • Using a pair of parentheses to denote an empty tuple: tuple1 = ()
 • Using a pair of parentheses and elements separated by commas: tuple2 = ('a', 'b', 'c')
 • Using the type constructor: tuple()
'''

# //

vowels = ('a', 'e', 'i', 'o', 'u')
print(f'\n ——————————\n Object type vowels: {type(vowels)}')

for p, x in enumerate(vowels):
    print(f' Position: {p+1}, value: {x}')
else: print(' ——————————')

# //

vowels = ()
''' vowels.append('a') ''' # ———> AttributeError

# //

vowels = ('a', 'e', 'i', 'o', 'u')
print(f'\n ——————————\n {[item for item in enumerate(vowels)]}\n ——————————')
    
# print(tuple(enumerate(vowels)))
# print(list(enumerate(vowels)))

# // Set-type Objects

'''
 • len(s)
 • x in s
 • x not in s
'''

'''
 • Using a pair of braces and elements separated by commas: set1 = {'a', 'b', 'c'}
 • Using the type constructor: set(iterable)
'''

# //

vowels1 = {'aeiou'} # No use of constructor
vowels2 = set('aeiouaaaaaa') # String constructor
vowels3 = set(['a', 'e', 'i', 'o', 'u']) # Builder with list
vowels4 = set(('a', 'e', 'i', 'o', 'u')) # Constructor with tuple

print(
f'''
 ——————————
 {type(vowels1)}  |  {vowels1}
 {type(vowels2)}  |  {vowels2}
 {type(vowels3)}  |  {vowels3}
 {type(vowels4)}  |  {vowels4}
 {set('banana')}
 ——————————''')

# //

def createReport():
    componentsVerified = set(['speakers', 'cooler', 'heat sink', 'cpu', 'hd', 'stabiliser', 'cabinet', 'hub', 'printer', 'joystick', 'ram memory', 'microphone', 'modem', 'monitor', 'mouse', 'UPS', 'capture card', 'sound card', 'video card', 'motherboard', 'scanner', 'keyboard', 'webcam'])
    componentsWithDefect = set(['hd', 'monitor', 'sound card', 'scanner'])
    
    amountCheckedComponents = len(componentsVerified)
    amountDefectiveComponents = len(componentsWithDefect)
    
    componentsOk = componentsVerified.difference(componentsWithDefect)
    
    print(
f'''
 ——————————
 Were checked {amountCheckedComponents} components.
 {amountDefectiveComponents} components were defective.
 The components that can be sold are:
''', end='')
    
    for item in componentsOk: print(f' {item}')
    else: print(' ——————————')

createReport()

# // Mapping Type Objects

'''
 • Using a pair of braces to denote an empty dict: dictionary1 = {}
 • Using a pair of elements in the form, key : value separated by commas: dictionary2 = {'one': 1, 'two': 2, 'three': 3}
 • Using the type constructor: dict()
'''

# //

# Example 1 - Creation of an empty dictionary, with subsequent assignment of key and value
dict1 = {}
dict1['name'], dict1['age'] = 'Bro', 30

# Example 2 - Creating a dictionary using a pair of elements in the form, key : value
dict2 = {'name': 'Bro', 'age': 30}

# Example 3 - Creating a dictionary with a list of tuples. Each tuple represents a key : value pair.
dict3 = dict([('name', 'Bro'), ('age', 30)])

# Example 4 - Creating a dictionary with the zip() built-in function and two lists, one with the keys, the other with the values.
dict4 = dict(zip(['name', 'age'], ['Bro', 30]))

print(f'\n ——————————\n {dict1 == dict2 == dict3 == dict4}\n ——————————') # Testing whether the different constructions result in equal objects.

# //

cadastre = {
    'name' : ['Bro', 'Mona', 'Po', 'Mini'],
    'city' : ['Brampton', 'Burlington.', 'Bancroft', 'Cambridge'],
    'age' : [25, 33, 37, 18]
}

print(
f'''
 ——————————
 len(cadastre) = {len(cadastre)}
 cadastre.keys() = {cadastre.keys()}
 cadastre.values() = {cadastre.values()}
 cadastre.items() = {cadastre.items()}
 cadastre['name'] = {cadastre['name']}
 cadastre['name'][2] = {cadastre['name'][2]}
 cadastre['age'][2:] = {cadastre['age'][2:]}
 ——————————''')

# //

'''
 • cadastre.keys(): returns a list of all keys in the dictionary.
 • cadastre.values(): returns a list of values. Since values ​​are also lists, we have a list of lists.
 • cadastre.items(): returns a list of tuples, each of which is composed of a key and a value.
 • cadastre['name']: accesses the value assigned to the key 'name'; in this case, a list of names.
 • cadastre['name'][2]: accesses the value in position 2 of the list assigned to the key 'name'.
 • cadastre['age'][2:]: accesses the values ​​from position 2 to the end of the list assigned to the key 'name'.
'''

# //

print(
f'''
 ——————————
 {len(cadastre['name'])}
 {len(cadastre['city'])}
 {len(cadastre['age'])
}''')

amountItens = sum([len(cadastre[key]) for key in cadastre])
print(f' Number of elements in the dictionary: {amountItens}\n ——————————')

# // Numpy Array Type Objects

'''
 • A powerful N-dimensional array object.
 • Sophisticated functions.
 • Tools to integrate C/C++ and Fortran code.
 • Useful linear algebra, Fourier transform, and random number resources.
'''

# //

import numpy

matriz1_1 = numpy.array([1, 2, 3]) # Create matrix 1 row and 1 column
matriz2_2 = numpy.array([[1, 2], [3, 4]]) # Create matrix 2 rows and 2 columns
matriz3_2 = numpy.array([[1, 2], [3, 4], [5, 6]]) # Create matrix 3 rows and 2 columns
matriz2_3 = numpy.array([[1, 2, 3], [4, 5, 6]]) # Create matrix 2 rows and 3 columns

print(
f'''
 ——————————
 {type(matriz1_1)}
 matriz1_1 = {matriz1_1}
 matriz2_2 = {matriz2_2}
 matriz3_2 = {matriz3_2}
 matriz2_3 = {matriz2_3}
 ——————————''')

# //

m1 = numpy.zeros((3, 3)) # Creates 3 x 3 matrix with zero only
m2 = numpy.ones((2,2)) # Creates 2 x 2 matrix with only one
m3 = numpy.eye(4) # Creates 4 x 4 identity matrix
m4 = numpy.random.randint(low = 0, high = 100, size = 10).reshape(2, 5) # Creates 2 X 5 matrix with integers

print(
f'''
 ——————————
 numpy.zeros((3, 3)) = {numpy.zeros((3, 3))}
 numpy.ones((2,2)) = {numpy.ones((2,2))}
 numpy.eye(4) = {numpy.eye(4)}
 m4 = {m4}
 Sum of values in m4 = {m4.sum()}
 Minimum value in m4 = {m4.min()}
 Maximum value in m4 = {m4.max()}
 Average values in m4 = {m4.mean()}
 ——————————''')
