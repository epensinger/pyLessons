# Conversion Functions

Use these to convert from one type to another.

Right now we know 3 data types, so we can use 3 conversion Functions

## String

```python
str()
```
Takes a numerical value and stores it as a string.


## Integer

```python
int()
```

Takes a string that consists of numbers and stores it as an Integer.



## Float

```python
float()
```

Takes a string that consists of numbers and stores it as a Float.


## Example

```python
age = input("How old are you?")  #==> age is now "15"

age = int(age) #==> age is now 15

next_year = age + 1  #==> age is now 16

next_year = str(age) #==>  age is now "16"

print('Next year you will be " + next_year)
```



