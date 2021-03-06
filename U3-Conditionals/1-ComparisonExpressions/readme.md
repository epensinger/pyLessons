# 1 - Comparison Expressions

# Lesson Goals
in this lesson you will learn to use comparison operators to write comparison expressions that evaluate to booleans

## Term Review:

value - a single piece of data that exists

operator - symbol that indicates how to evaluate data

evaluate - to reduce an expression to its simplest form

expression -  a combination of values and operators that evaluate to a single value.

(value operator value)


## Expressions we already know

### Concatenation:

```python
message = "Hello there " + name
```

### Numerical Expressions

```python
area = length * width
apples_left = 35 % 8
score += 5
```


## Comparison Expressions

Comparison expressions use a comparison operator to evaluate the relationship between values.

Comparison Operators: (sometimes also called conditional or boolean expressions)

```python

>   greater than
<   less than
>=  greater than or equal to 
<=  less than or equal to
==  equal to
!=  not equal to

```


## Writing Comparison Expressions

value operator value

```python
5 <= 3  
4 >= 3
"tree" == "hat"
age >= 21
```

## Evaluating Comparison Expressions

Comparison expressions evaluate to boolean values

Boolean is a data type that can store one of two values - true or false.

True is NOT a string, it is the state of being truthy.

False is NOT a string, it is the state of being falsey.

IF the comparison expression is truthy it will evaluate to true.
IF the comparison expression is falsey it will evaluate to false.

Check it out - type(true) will return bool


## For example:

```python
print(5 <= 3)
print(4 >= 3)
print("tree" == "hat")
print(age >= 21)

#this would print:
false
true
false
and then throw an error bc age is not defined.
```

## Exercise

It's now time for the obligatory ritual in which I give you comparison expressions
and you evaluate true or false.  

