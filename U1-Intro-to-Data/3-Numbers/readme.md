# Numbers
In this lesson you will learn to use the 2 different types of numbers in python.
You will also learn to use the type function to figure out the data type of a value.

## What's a number?
- numbers represent a mathematical quantity.
- they are not stored as a sequence of characters, but as a value that can be manipulated mathematically.

## Integers
- an integer is a whole number (no decimal parts).
- can be positive or negative.

```python
5
5326
9
23049
123456843920358395023
```


## Floats
- any number with a decimal, even if the digits after the decimal are 0.
- the computer stores these in data differently, and they are approximations that are really close to exact.
- [here are the full details on why a float is an approximation](https://docs.python.org/3/tutorial/floatingpoint.html), if you want to know.

```python
5.0
23.2345
3.1459
13.99
```

## The Type function
- type() will return the type of a value
- type(5.0) returns float
- type("hello world") returns string
- type(10) returns int
