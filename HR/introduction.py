
# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def is_leap(year):
    if ( year % 400 ) == 0:
        return True
    if ( year % 100 ) == 0:
        return False
    if ( year % 4) == 0: 
        return True
    else:
        return False

# https://www.hackerrank.com/challenges/python-print/problem
def printFunction(n):
    s = ''
    for x in range(n) :
        s = s + str(x + 1)
    print (s)

# https://www.hackerrank.com/challenges/swap-case
def swap_case(s):
    result = ''
    for x in s:
        if x.isupper():
            result += x.lower()
        else:
            result += x.upper()
    return result

# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def split_and_join(line):
    return '-'.join(line.split(" "))

# https://www.hackerrank.com/challenges/whats-your-name/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def print_full_name(first, last):
    return "Hello firstname lastname! You just delved into python.".replace("firstname", first).replace("lastname", last)

# https://www.hackerrank.com/challenges/python-mutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def mutate_string(string, position, character):
    return

# print(is_leap(2020))
# print(printFunction(5))
# print(swap_case('test'))
# print (split_and_join("this is a test"))
# print (print_full_name("Andrea", "Girardi"))
