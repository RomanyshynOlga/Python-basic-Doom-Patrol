#1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print (id(int_a))
print (id(str_b))
print (id(set_c))
print (id(lst_d))
print (id(dict_e))
# 9790720
# 140334025374704
# 140334025341184
# 140334026247872
# 140334026199680


#2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(lst_d)
# [1, 2, 3, 4, 5]
print (id(lst_d))
#139696075431616


#3. Define the type of each object from step 1.
print(type(int_a))
print (type(str_b))
print (type(set_c))
print (type(lst_d))
print (type(dict_e))
# <class 'int'>
# <class 'str'>
# <class 'set'>
# <class 'list'>
# <class 'dict'>


# 4*. Check the type of the objects by using isinstance.
#
# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict)
# True
# True
# True
# True
# True

# String formatting:
#Replace the placeholders with a value:
#"Anna has ___ apples and ___ peaches."



# 5. With .format and curly braces {}
print("Anna has {}{}{} apples and {}{}{} peaches.".format(1, 0, 0, 2, 0, 1))
#Anna has 100 apples and 201 peaches.



#6. By passing index numbers into the curly braces
print("Anna has {0}{1}{2} apples and {3}{4}{5} peaches.".format(1, 0, 0, 2, 0, 1))
#Anna has 100 apples and 201 peache



#7. By using keyword arguments into the curly braces
print("Anna has {0}{1}{2} apples and {pr} peaches.".format(1, 0, 2, pr = "big"))
#Anna has 102 apples and big peaches.



#8*. With indicators of field size (5 chars for the first and 3 for the second)

print("Anna has {0:4} apples and {1:2} peaches.".format(1, 2))
#Anna has    1 apples and  2 peaches.




#9. With f-strings and variables
a = "big"
b = "small"
print(f"Anna has {a} apples and {b} peaches.")
#Anna has big apples and small peaches.



#10. With % operator
a = "any"
b = "many"
print("Anna has %s apples and %s peaches." % (a, b))
#Anna has any apples and many peaches.




#11.*. With variable substitutions by name (hint: by using dict)
a = "one"
b = "two"
data_dict = {"ap": a,"pe": b}
print("Anna has %(ap)s apples and %(pe)s peaches." % data_dict)
#Anna has one apples and two peaches.




#12
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
#[0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)
#[0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]




#13 (2) list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)
#[0, 10, 1, 30, 2, 50, 3, 70, 4, 90]
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append (num // 2)
    else:
        lst.append(num * 10)
print(lst)
#[0, 10, 1, 30, 2, 50, 3, 70, 4, 90]




#14. Convert (3) to dict comprehension.
(3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)
#{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

dict_comprehension = {x: x ** 2 for x in range(1, 11) if x % 2 == 1}
print(dict_comprehension)
#{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}




#15*. Convert (4) to dict comprehension.
(4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
#{1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

dict_comprehension = {x: x ** 2 if x % 2 == 1 else x // 0.5 for x in range(1, 11)}
print(dict_comprehension)
#{1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}



#16. Convert (5) to regular for with if.
(5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#{0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

d ={}
for num in range(10):
    if num ** 3 % 4 == 0:
        d[num] = num ** 3
print(d)
#{0: 0, 2: 8, 4: 64, 6: 216, 8: 512}


#17*. Convert (6) to regular for with if-else.
(6)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)
#{0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}

d ={}
for num in range(10):
    if num ** 3 % 4 ==0:
        d[num] = num **3
    else:
        d[num] = num
print(d)

#{0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}



#18. Convert (7) to lambda function
7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y
print(foo(1, 2))
#1

lmb = lambda x, y :x if x < y else y
print(lmb(1, 2))
#1


#19*. Convert (8) to regular function
(8)
foo = lambda x, y, z: z if y < x and x > z else y
print(foo(1, 2, 3))
#2

 def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y

print(foo(1, 2, 3))
#2


#20 Sort lst_to_sort from min to max
st_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

st_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print (sorted(st_to_sort))
#[1, 5, 13, 15, 18, 24, 33, 55]



#21.21. Sort lst_to_sort from max to min
print (sorted(st_to_sort, reverse = True))
#[55, 33, 24, 18, 15, 13, 5, 1]


#22. Use map and lambda to update the lst_to_sort by multiply each element by 2
st_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
def foo (x):
    return x * 2
old_list = [5, 18, 1, 24, 33, 15, 13, 55]
new_list =list(map(foo,old_list))
print(new_list)
#[10, 36, 2, 48, 66, 30, 26, 110]

new_list =list(map(lambda x: x * 2, old_list))
print(new_list)
#[10, 36, 2, 48, 66, 30, 26, 110]

#23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
lst_foo = list(map(lambda x, y: x ** y, list_A, list_B))
print(lst_foo)
#[32, 729, 16384]



#24. Use reduce and lambda to compute the numbers of a lst_to_sort.

 import functools
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort_n = functools.reduce(lambda a, b: a + b, lst_to_sort)
print(lst_to_sort_n)
#164


#25 Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort_new = list(filter(lambda x:(x % 2 ==1), lst_to_sort))
print(lst_to_sort_new)

#[5, 1, 33, 15, 13, 55]


#26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
lst_to_sort_rng = list(filter(lambda x: (x < 0), range (-10, 10)))
print(lst_to_sort_rng)
#[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

#27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
list_new = list(filter(lambda x: x in list_1, list_2))
print(list_new)

#[2, 3, 5, 7]


