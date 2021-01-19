
#we have collected a user's name
user1 = "steve smith"
#we want to greet the user formally so we make sure the first letter of his name is capitalzed
print("Hello " + user1.title())

#we have collected a user's age
age = "6"
#we want to make sure we can convert it to a number
age.isdigit()  #We will learn how to use this test soon.  For now it just gives us True

#we want to search in this string
word = "superCalifFagilisTicesPialidocious"
#we don't want to test for both S and s in our search so we make it all lower
word = word.lower()

# Some users mess up and type a space before their name.  
#We want to use strip to make sure we aren't storing a space at the front.

username = "   fluffy"
username = username.lstrip()
print(username)

# It's possible if we are working with breaking up a chunk of words that we end up with spaces we don't want.
# We want to use strip to remove spaces on both sides of the word.
keyword = "  puzzle   "
keyword = keyword.strip()
print(keyword)

# We want to make sure the user entered a number before we turn it into a number
length = "six"
height = "5"

print(length.isdigit())
print(height.isdigit())
#again, more on the true an false responses in the next unit.
