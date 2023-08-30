# 1. Basic - Print all integers from 0 to 150.
def print_to_150():
    for num in range(151):
        print(num)

print_to_150()


# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
def print_multiples_to_1000():
    for num in range(5, 1001, 5):
        print(num)

print_multiples_to_1000()


# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead.
# If divisible by 10, print "Coding Dojo".
def print_coding_or_dojo():
    for num in range(1,101):
        if not num % 10:
            print("Coding Dojo")
        elif not num % 5:
            print("Coding")
        else:
            print(num)

print_coding_or_dojo() 


# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def sum_huge_num():
    x = sum(list(range(1,500001,2)))
    print(x)

sum_huge_num()


# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
def countdown_by_fours():
    for num in range(2018, 0, -4):
        print(num)

countdown_by_fours()


# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum,
#  print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop
#  should print 3, 6, 9 (on successive lines)
def flexible_counter(low, high, mult):
    for num in range(low, high+1):
        if not num % mult:
            print(num)

flexible_counter(2,9,3)
        