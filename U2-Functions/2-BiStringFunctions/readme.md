# Lesson 2 - Built in Functions with Strings

## Lesson Goals
Call built in functions
Pass strings to built in functions

## Functions
**Function** - a block of code that carries out a specific task (not attached to an object)
**Built in Function** - functionality that is always available

```
print("This")
#Print is a built-in function!
```

## Passing Values to Functions
**Function Call** - an expression that tells python to execute a function

**Argument** - values that are passed to a function in the function call

Many functions take a value (or a few values), do something with it, and give a value back.  

You should know what kind of value it's expecting and what it will do with it.

The value you are passing into the function goes in the parenthesis.

You can pass in the actual value, or a variable. 

IF the function takes multiple arguments, you pass them in order, separated by commas (more later).


## Print Function
Takes a string
Displays it in the interpreter 

```python
print("Hello World!")
```


## Input Function
```
name = input("What is your name?")
```
- Displays the argument (like the print statement)
- Returns the user's input as a string.
- Make sure to store the result in a variable

Alternatively:
```python
print("What is your name?")
name = input()
```


(For later 
## Type Function
Takes any object
Sends back the type of object

```python
cat = "Scout"
type(cat) #==> str

cost = 5.99
type(cost) #==> float
)
