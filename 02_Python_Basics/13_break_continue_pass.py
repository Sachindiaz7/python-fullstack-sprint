#break
for i in range(1,6):
    print(i)

    if i == 3:
        break

count = 1

while count <= 5:
    if count == 4:
        break

    print(count)
    count = count + 1

print("Loop Ended")

#continue
for i in range(1,6):
    if i == 3:
        continue

    print(i)

for i in range(1,8):
    if i == 5:
        continue
    print(i)

#break
for i in range(1,6):
    if i == 3:
        break
    print(i)

count = 1

while count <= 5:
    count = count + 1

    if count == 3:
        continue

    print(count)

print("Done")

#pass
age = 18

if age >= 18:
    pass

print("Eligible")

for i in range(1, 5):

    if i == 2:
        pass

    print(i)

print("Done")