word = "python"

print(word[0])
print(word[3])

#negative
print(word[-4])

#slicing
word = "Computer"

print(word[2:6])

name = "Sachin"

print(name[:4])

text = "Programming"

print(text[3:])

name = "Sachin"

print(name[:])

#upper(),lower(),strip(),replace(),count(),find(),len()
name = "Sachin"
print(name.upper())

language = "PYTHON"
print(language.lower())

text = "  Hello World  "
print(text.strip())

text = "python programming"
print(text.title())

text = "I like java"
print(text.replace("java","python"))

word ="king cobra"
print(word.find("o"))

word = "banana"
print(word.count("a"))
print(word.count("n"))

city = "coimbatore"
print(len(city))