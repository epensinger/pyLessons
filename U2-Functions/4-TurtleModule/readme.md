# Lesson 4 - Using the Turtle Module

## Lesson Goals
- Apply your method calling skills to draw using the turtle module
- THIS IS NOT TO MEMORIZE!  Your goal is to USE the nethods, not commit them to memory.

## Turtle Module

- provides a canvas and a way of drawing on it with python code.

- might also see it refered to as the Turtle library, same thing.

- to use it, import turtle just like we imported random in the last lesson

```python
import turtle

#OR

from turtle import *
```

on Trinket, you must be in a pygame trinket 

on repl.it you have to choose python(with Turtle) for the language

on a computer, it's included with python3

## Turtle Setup
1. Initialize the screen by assigning turtle.Screen() to a variable
2. Create a turtle (pen) to draw with by assigning turtle.Turtle() to a variable
3. At the bottom of the file add screen.exitonclick() to make the window stay open once your shape is drawn.

```python
screen = turtle.Screen()
pen = turtle.Turtle()

# Code will be here

screen.exitonclick()
```

It's ok to just think of this as the code you need to setup Turtle and not worry about the parts.
There are more things you can do at this phase to adjust colors and sizes and stuff, but that's for later.

## Turtle Methods
- the screen and pen vairables are now objects that have methods we can call on them, like the methods we called on strings. 

```python
pen.penup() - lifts the pen up (so you can move it without drawing)
pen.pendown() - puts the pen down (so when you move it, it will draw)
```

## Moving the pen
- to move the pen, call the method for the direction you want it to go.
- pass in the argument for the distance you want it to go (in pixels.)
- remember to put the pen down if you want to draw the path.

```python
pen.right(90)  #turn right 90 degrees
pen.forward(100) #move forward 100 pixels
pen.left(90) #turn left 90 degrees
pen.backward(100) #move backward 100 pixels
```

## Goals for now
- at this point, just work on drawing simple shapes.
- make sure you get the feel of moving the pen around and how those 6 methods work
- we will revisit Turtle in unit 4 (this is 2) when we talk about looping, that's when you will see some more complex work with shapes.
