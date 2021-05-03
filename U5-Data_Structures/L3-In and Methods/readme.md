# Lesson 2 -In and Dictionary Methods



## Lesson Outline
### The Keyword In
- tests for the presence of something in a dictionary
- conditional expression that returns a boolean


---

### Does a dictionary have this key?
```python
char1 = {
    "name" : "Darth Vader"
    "side" : "dark",
    "lightsaber" : True
}

if name in char1:
    print(char1["name"])

if ship in char1:
    print(char1["ship"])
```


---

### Does this Dictionary have this value?
```python
char1 = {
    "name" : "Darth Vader"
    "side" : "dark",
    "lightsaber" : True
}

if "dark" in char1.values():
    print("Join the dark side")

if "light" in char1.values():
    print("Resist your anger")
```


---


## Dictionary Methods


---

### Clear
clear all the keys and values in a dictionary
```python
p1 = {
    "name" : "Billy",
    "score" : 375,
}

#Reset game
p1.clear()  #p1 now empty
```


---

### Copy
makes a copy of a dictionary
```python
player_steve = {
    "name" : "Steve",
    "score" : 375,
    "color" : "blue",
    "rank" : 10
    "weapon" : "slingshot"
}

p1 = player_steve.copy()  
```


---

### fromKeys
creats a new dictionary with key value pairs from comma separated values
```python
{}.fromKeys("a","b") #==>{'a', 'b'}\

#Initialize a new user
new_user = {}.fromKeys(["name", "email", "phone", "zip"], "unknown")
```


---

### Get
retrieves the value of a key in an object and None instead of an error if the key doesn't exist
```python
d = dict(a = 1, b = 2, c = 3)
d.get("a") #==> 1
d.get("b") #==> 2
```
