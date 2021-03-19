import functools


# Ejercicio 1
def multiply(a, b):
    result = 0
    positive = abs(b) == b
    cont = 0
    while cont < abs(b):
        result = result + a if positive else result - a
        cont += 1
    return result


a = multiply(50, -50)
print(a)


# Ejercicio 2
def get_biggest(arr):
    result = max(arr)
    return result


b = get_biggest([1, 4, 50, 200, 400, 1500, -56])
print(b)


# Ejercicio 3
def clean(arr):
    result = functools.reduce(lambda acc, el: acc + [el] if el else acc, arr, [])
    return result


c = clean([1, None, False, 0, 2, 3])
print(c)


# Ejercicio 4
def flatten(arr):
    result = functools.reduce(lambda acc, el: acc + el if type(el) is list else acc + [el], arr, [])
    return result


d = flatten([1, [2, 3], 4, [[5, 6], 7, 'a']])
print(d)


# Ejercicio 5
def repeated(string: str):
    lowered = string.lower()
    splitted = lowered.split(' ')
    reduced = functools.reduce(
        lambda acc, el: acc.update({el: acc[el] + 1}) or acc if acc.get(str(el), None) else acc.update({el: 1}) or acc,
        splitted, {})
    list_of_tuples = list(reduced.items())
    return max(list_of_tuples, key=lambda item: item[1])


f = repeated('this is a repeated word test list is a a')
print(f)


def is_palindrome(string: str):
    string = string.replace(' ', '')
    lowered = string.lower()
    splitted = list(lowered)
    splitted.reverse()
    joined = ''.join(splitted)
    return lowered == joined


e = is_palindrome('Ana')
print(e)
