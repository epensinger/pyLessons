# For Loops on Lists

## Lesson Goal 
Use for loops to iterate through lists and repeat processes.


---

## Term Review

### Iterable Object
an object that can be iterated 
- so far we know string, range, list

### Iterate
to work through an interable object one by one

### Index
the position of each item in the iterable object
starts at zero

### List
a list is an ordered collection or grouping of data


---

## For loop

for item in iterable_object:

```python
friends = ["Mario", "Luigi", "Princess Peach", "Captain Toad"]

for friend in friends:
  print("Hello " + friend)
```

use a plural for the name of the list
use the singular version for the variable in the for loop


---

## Example: Printing a list

```python
friends = ["Mario", "Luigi", "Princess Peach", "Captain Toad"]

for friend in friends:
  print(friend)
```


---

## Example: Formatting a list

```python
friends = ["Mario", "Luigi", "Princess Peach", "Captain Toad"]

for friend in friends:
  friend = friend.upper()
  print(friend)
 
print(friends) #doesn't actually change the list
```


---

## Example: Mathing a list

```python
scores = [89, 73, 85, 93]

for score in scores:
  score += 5
  print(score)
  
print(scores)  #doesn't actually change the list
```

---

## Example: Checking items in a list

```python
secret_word = "pizza"
guesses = ["a", "f", "m", "p"]

for guess in guesses:
  if guess in secret_word: 
    print(guess + "is in the secret word!")
```


