colors = ["apple","mango","jack fruit"]
print(colors[1])
print(colors[2])

data = ["sachin",28.5,True]
print(data[2])
print(data[2])

#lists are mutable
data = ["sachin",28.5,True]
data[1] = 56.7
print(data)

numbers = [10, 20, 30]

numbers[2] = 50

print(numbers)

#append()
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)

#remove()
fruits = ["Apple", "Mango", "Orange"]

fruits.remove("Mango")

print(fruits)

numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)

#len()
numbers = [10, 20, 30, 40, 50]

print(len(numbers))

languages = ["Python", "Java", "C", "Go"]

print(len(languages))

#in , not in
fruits = ["mango","apple","orange"]

print("mango" in fruits)
print("mango" not in fruits)