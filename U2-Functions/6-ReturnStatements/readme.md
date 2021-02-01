# Returning values from Functions
# Return Statement

# Lesson Goals
return a value from your functions

# Review
So far you have defined functions that print stuff.
You have used functions like round() or input() that return values.

```python
rounded_num = round(answer,2)

name = input("what is your name")
```

# Return Statement
use the return statement to end a function and return a value

```python
#gets the users name and returns it in title case
def name_title():
    name = input("what is your name?")
    name = name.title()
    return name
```

# Using what you return
just like when you called built-in functions, you have to assign the function call to a variable to use it in your programs.

```python
cap_name = yell_name()

score = my_math()
```

# What can I return?
a variable:

```python
def square3():
    answer = 3 * 3
    return answer
```

an expression:

```python
def square3():
    return 3*3
```

the result of another function:

```python
def my_math():
    answer = 2345/425
    return round(answer)
```

an exact value:

```python
def return9():
    return 9
```

# Return statement ends the function

```python
def yell_name():
    name = input("what is your name?")
    name = name.title()
    return name
    print("Hi " + name) #This line won't run

def yell_name():
    name = input("what is your name?")
    name = name.title()
    print("Hi " + name) #This line will run
    return name
```


