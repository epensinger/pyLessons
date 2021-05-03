# Lesson 4 More Dictionary Methods


## Lesson Outline

---

### Pop
Takes a single argument corresponding to a key and removes that key-value pair from the Dictionary
Returns the value corresponding to the key that was removed.

```python
d = dict(a=1,b=2,c=3)
d.pop() #Error - which one do i pop?
popped = d.pop('a') #==>1
d #==> {'c':3, 'b': 2}
d.pop('e') #KeyError - not there!
```


---

### Popitem
Removes a random key from the dictionary

```python
d = dict(a=1,b=2,c=3,d=4,e=5)
d.popitem() #==> ('d', 4)
d.popitem('a') #==> Error, it didn't want a key.
```


---

### Update
Update keys and values in a dictionary with another set of key value pairs.

```python
first = dict(a=1,b=2,c=3,d=4,e=5)
second{}

second.update(first)
second # {'a':1, 'b':2, 'c':3, 'd':4, 'e': 5}

#let's overwrite an existing key
second['a'] = "AMAZING"

#If we update again
second.update(first)# {'a':1, 'b':2, 'c':3, 'd':4, 'e': 5}

#That update overrode our Amazing!
```


---

### Dictionary Comprehension
```python
{ ____:____ for ___ in ____}

```
- iterates over keys by default

- to iterate over keys and values using .items()


---

###  Dictionary Comprehension Example

```python
numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key,value in numbers.items()}

print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}
```


---

### More Examples
```python
{num: num**2 for num in [1,2,3,4,5]}

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))} 
print(combo) # # {'A': '1', 'B': '2', 'C': '3'}
```


---

### Conditional logic with dictionaries
```python
num_list = [1,2,3,4]

{ num:("even" if num % 2 == 0 else "odd") for num in num_list }

# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
```


---

### Summary of Dictionary lessons
- dictionaries are key value pairs that are useful when describing collections and order is not important
- you can create dictionaries with curly braces or the dict function
- you can iterate over dictionaries using keys(), values() and items()
- use methods like get to handle errors more gracefully than directly accessing keys in a dictionary
- dictionary comprehension is useful for creating dictionaries from other data structures


