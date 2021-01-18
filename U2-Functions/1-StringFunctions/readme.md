# Lesson 1 - Built in Methods with Strings

## Lesson Goals
- call built-in methods on strings

- pass strings to built in functions

## Built-In String Methods
**Method** block of code that carries out a specific task on an object or class.

**Built-In** refers to functionalities that are included in python as opposed to functionalities we have to add ourselves

(functionality means it's able to do something)

These methods wil carry out specific tasks on strings.

## Syntax to call a method
the string, followed by a period

then the name of the method, followed by parenthesis

this can be stored in a variable, or printed right out

you can use a variable that is a string in place of the string

```python
"steve".upper()
"Steve".lower()
"THIS IS FUN".title()
```

## Methods to use
s.lower() - turns the string to lower case

s.upper() - turns the string to upper case

s.title() - turns the string to title case

s.lstrip() - removes any spaces to the left of the string

s.rstrip() - removes any spaces to the right of the string

s.strip() - removes any spaces to either side of the string

s.isalpha() - checks to see if all the characters are letters

s.isdigit() - checks to see if all the charaters are digits

s.isspace() - checks to see if all the characters are space


google python string methods for all sorts more

## Examples
```python
#we have collected a user's name
user1 = "steve"
#we want to greet the user formally so we make sure the first letter of his name is capitalzed
print("Hello " + user1.title())

#we have collected a user's age
age = "6"
we want to make sure we can convert it to a number
age.isdigit()  #We will learn how to use this test soon.  For now it just gives us True

#we want to search in this string
word = "superCalifFagilisTicesPialidocious"
#we don't want to test for both S and s in our search so we make it all lower
word = word.lower()
```


## Yes the empty parenthesis matter
The () syntax tels python this is a task to execute

Without (), python looks for values and doesn't execute the task





