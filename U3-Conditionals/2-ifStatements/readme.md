# Conditional Statements with IF

# Lesson Goals
- Buld if statements from comparison expressions

## But first review
*Comparison expression* - value **comparison operator** value
- comparison expressions evaluate to True or False
- True and False are boolean values - not strings

## Review Practice:

```python
"tree" == "branch"
4 <= 2
10 < 500
8 < 8
8 <= 8
```

## Conditional Statements

- represent different paths a program can take depending on stated conditions
- the code in an if statement only runs if the expression after if evaluates to the boolean True

Syntax:
```python
If (comparison expression):
    code to run
    might be lots of lines
    notice it's indented

This line will run wither the if statement is true or not
```

## Examples:

```python
If (score > 50):
    print("You win!")

print(game over)
```

## Examples:
```python
If tryPass == realPass:
    print("You are correct")
```

## Examples:
```python
If cash > cost:
    newCash = cash - cost
    print("You will have " + str(newCash) + " left if you purchase this item!")
```

## Examples:
you can call a function from an if statement
```python
def printRules:
    print("Guess a number between 0 and 10")
    print("Please only type a digit")
    print("Press enter after you type your number")
    
#Imagine a whole guess the number game

print("You did something wrong.")
print("Would you like to review the rules?")
rules = input("Type y to see the rules, or n to continue")

if rules == "y":
    printRules
