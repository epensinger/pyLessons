# Lesson 6 Variable Expressions
In the last lesson we learned to assign values to variables. 
In this lesson we will learn how to use those variables in our expressions.

## Term Review
*expression* - 
*evaluate* -
*value* - 
*variable* - 
*operator* - 

## String Expressions with variables
- variables allow us store values to insert in our strings.
- in order to concatenate, the variable must be a string.
```python
player1 = "Mario"
player2 = "Luigi"

print("Welcome to Level One, " + player1 +".  Are you ready to crush " + player2 +"?")
```

## Numerical Expressions with variables
- use a variable to replace one or more values in the expression
- set the result equal to a new or existing variable

```python
account = 576
speedy_shoes = 100
red_jersey = 50

purchase_cost = red_jersey + speedy_shoes

account = account - purchase_cost

```

## Type shifting
- only variables with values that are numbers can be used in numerical expressions
- only variables with numbers that are strings can be used in string expressions
- use the str() or int() functions to change from one to the other (only works for digits)

```python
str(5) #==> "5"
int("6") #==> 6

"5" + 6 #==> error

"5" + str(6) #==> "56"
int("5") + 6 #==> 11

int("five") #==> error
```

## More Exmaples
```python
apples = 5
boxes = 15

strApples = str(apples)
strBoxes = str(boxes)
print("I have " + strApples + " apples and " + strBoxes + " boxes.")

```

```python
length = "15"
width = "16

length = int(length)
width = int(width)

area = length * width
```

