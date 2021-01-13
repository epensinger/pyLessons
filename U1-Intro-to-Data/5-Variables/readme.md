# Lesson 5 - Variable Assignment
In this lesson you will learn how to store data in variables
## Lesson Goals
- assign values to variables
- naming restrictions and conventions


## Lesson Outline

### Variables introduction
- a variable is a named space that holds a value.
- think of it as a box that holds a value.
- helpful to think of it like a variable in math.
- variables have three parts - a name, the value currently stored there, and the type of data that is stored there.

### Variable Assignment
- you must tell python that a variable exists and give it a value before you can use it in code.
- *assignment statement* - stores a value inside of the variable
- *assignment operator* - the equals sign, used to store values in variables.
- ex: <code>id = 57436</code>
- use variables to write expressions to evaluate data that could change.

#### Some fine print
- data in python variables can be either dynamic or static.
- dynamic data is data that will or could change throughout the course of the program.
- constant data is data that is not to be changed during the course of the program.


### Variables Can Be:
- assigned to other variables
- <code>num_of_cats = num_of_felines</code>
- reassigned at any time
- <code>num_of_cats = 30</code>
- assigned at the same time as other variables
- <code>dogs, cats, pets= 5, 99, 104</code>

### Naming Restrictions
1. Variables must start with a letter or underscore
2. The rest of the name must consist of letters, numbers, or underscores
3. Names are case sensative
Violating restrictions usually leads to an invalid syntax error

### Naming Conventions
1. Most variables should be in <code>snake_case</code>
2. Most variables should be lowercase, <code>CAPITAL_SNAKE_CASE</code> can be used for constants
3. UpperCamelCase - is used for a class type (more info much later)
4. Variables that start and end with double underscore are marked by the initial developer as not to be changed (ex: <code>__no_touchy__</code>)
Violating conventions won't cause an error but causes problems in collaboration and usability of your code.

### Naming Restrictions Quiz
