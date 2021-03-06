# Lesson 7 - Updating Variables
## Lesson Goals
- change the value assigned to a variable
- update the value assigned to a varaible

## Lesson Outline

### Change a variable's value
- to overwrite the value assigned to a variable, simply assign it a new value
```python
user = "Johnny"
#The user updates his name
user = "John Smith"
```

```python
favorite_color = "blue"
#You change your mind
favorite_color = "blue"
```

### Using the new variable
- remember, python runs in order from top to bottom
- if you update the variable after an expression, the expression will use the old variable
- if you update the variable before an expression, the expression will use the new variable

```python
name = "Johnny"
print(name) #==> prints Johnny
name = "John Smith" 
print(name) #==> prints "John Smith"
```

```python
cash = 10
have = cash - 5 #==> have = 5
chash = 20
print(have) #==> have is still 5.
```

### Updating the value in a variable
use the variable in an expression in an assignment statement

```python
cash = 5
# I get 10 bucks
cash = cash + 10   #cash now equals the old cash plus 10
```
```python
name = "John"
name = name + " Smith"   #name now equals the old name plus " Smith"
```

### Updating shortcut
use += instead of retyping the variable

```python
cash = 5
cash += 5    #==> cash now equals 10
```
```python
name = "John"
name += " Smith"   #name now equals "John Smith"
```

### Other Operators work the same

```python
cash = 100
cash -= 20   #==> cash is now 80
cash += 5 #==> cash is now 85
```



 
