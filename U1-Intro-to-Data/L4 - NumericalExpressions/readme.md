# Numerical Expressions
In this lesson you will learn how to write numerical expressions that can be evaluated by the computer.
In plain English this means you will be learning how to get the computer to do math.

## Term review
_expression_ a combination of values and operators that evaluate to a single value.

_value_ - a single piece of data that exists (ex: 5)

_operator_ - symbol that indicates how to evaluate data (ex: +, -)

_evaluate_ - to reduce an expression to its simplest form (solve the math problem, combine the strings, determine truthiness or falseness)

value operator value 

OR

value operator value operator value operator value, etc.

## Mathematical Operators
### Addition
- Use <code>+</code> to add two numbers together.
- If you add a float and a float or a float and an int the result will always be a float.  Python will keep .0 on the end.

### Subtraction
- Use <code>-</code> to subtract.
- As in addition, if either number is a float, it will return a float.

### Multiplication
- Use <code>*</code> to multiply.
- x is a letter in python, it can't also be an operator!
- Once again, if either of the numbers is a float, the result will also be a float.

### Division
- Use <code>/</code> to divide.
- Division will always return a float
- Division that results in a repeating decimal will print 16 places and quit.

#### The first quiz is over this much

### Exponentiation
- Use <code>**</code> to create an exponent.  
- <code>2**3</code> is read "two to the third" and evaluates to 8 (2*2*2)
- <code>3**2</code> is read "three squared" and evaluates to 9 (3*3)

### Modulo
- Use <code>%</code> to find the modulo
- The modulo is the remainder after one number is divided by another number
- <code>5 % 2</code> returns 1
- <code>12 % 5</code> returns 2
- <code>22 % 5</code> also returns 2
- Useful for idenfiying whether a number is odd or even, or finding every 3rd, etc.

### Integer Division
- Use <code>//</code> for integer division
- Integer division always returns an integer
- If the result isn't a whole number, the decimal portion is chopped off. 
- Not highly used, but helpful for converting float to int, or along with the modulo.

### PEMDAS - order of operations
- When evaluating an expression in Python the computer follows this process:
    1. Solve anything in *p*arentheses
    2. Solve any *e*xponents
    3. Do any *m*ultiplication, *d*ivision, modulo, and integer division (from left to right)
    4. Do any *a*ddition and *s*ubtraction
