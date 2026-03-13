# "add2" add two numbers. like, add2(5, 6) will rusult "11"

def add2(num1, num2):
    add2result = num1 + num2
    return add2result

# "add3" add three numbers. like, add3(5, 6, 1) will rusult "12"

def add3(num1, num2, num3):
    add3result = num1 + num2 + num3
    return add3result

# "addall" adds any numbers. like, addall(5, 6, 1) will rusult "12"

def addall(*args):
    addallr = 0
    for num in args:
        addallr += num
    return addallr


# "multi2" multiply's two numbers. like, mult2(5, 6) will rusult "30"

def multi2(num1, num2):
    multi2result = num1 * num2
    return multi2result

# "show" is to make a text show up on the users side. show("message!")

def show(string1):
    showstring = string1
    print(showstring)

# "showall" is to make a text show up on the users side. showall("message!", hi)

def showall(*args):
    string = ""
    for s in args:
        string += str(s) + " "
    print(string.rstrip())
    return string

# "sub" subtract's two numbers. like, sub(5, 5) will rusult "1"

def sub(num1, num2):
    Subtracted = num1 - num2
    return Subtracted

# "sub" subtract's two numbers. like, sub(5, 5) will rusult "1"
# "show" is to make a text show up on the users side. show("message!")
# "multi2" multiply's two numbers. like, mult2(5, 6) will rusult "30"
# "add3" add three numbers. like, add3(5, 6, 1) will rusult "12"
# "add2" add two numbers. like, add2(5, 6) will rusult "11"
# "addall" adds any numbers. like, addall(5, 6, 1) will rusult "12"
# "showall" is to make a text show up on the users side. showall("message!", hi)

#if stuck try this as a base 
    #show("hello")

# start coding form this point, and on:

#code HERE :


