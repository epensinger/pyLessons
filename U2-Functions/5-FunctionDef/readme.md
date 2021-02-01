# Lesson - 5 Defining Functions

## Lesson Goal

Be able to write your own Functions
Be able to call the function that you write


## Function Definition

To define a function is to tell Python it exists and write the code that will run when it is called.

The function definition must come above the function call in the code.


## Syntax

```python
def my_function():
    print("Hello")
```

def is the keyword to indicate you are creating a new function

my_function() - this is the name of the function, what you will use to call it later

empty parenthesis mean that there are no parameters to send to the function

The code that runs when the function is called is indented below


## Example - rules()
```python
# A function to display the rules of a game:

func rules():
    print("Please remember to follow these rules:")
    print("Only choose 1 number.")
    print("Do not include any other characters in your choice.")
    print("Press enter after the number")

# Type this whenever you want the rules to print out:
rules()
```

## Example
```python
def f():
    s = '--This is inside f()'
    print(s)

print('Before calling f()')
f()
print('After calling f()')
```


## Variables inside Functions
- any variables you assign inside a function only exist inside that function
- any variables you assign outside a function are not usable inside a function
    - unless you pass them as arguments, more later.

```python
name = "Fluffy"
age = 3

def welcome():
    name = "Fido"
    age += 1 #This won't run
    print("Hi " + name) # Prints Hi Fido


print("Hi " + name) # Prints Hi Fluffy
welcome() # Prints Hi Fido
```

## Why define a function?

### 3 answers:
1. Abstraction and Reusability

2. Modularity

3. Namespace separation


say what???


### 1. Abstraction and Reusability
- if you copy and paste to reuse code, any changes would have to be made anywhere.
- if you put that code in a function instead, you only have to change the function.

## 2. Modularity
- build (and test) the program in manageable parts.

## 3. Namespace separation
- variable names are LOCAL to a function
- I don't have to worry about whether variable names are used elsewhere in the program.



