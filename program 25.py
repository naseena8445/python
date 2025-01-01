names = ["arya", "arjun", "johna", "hebla"]
count = 0

for x in names:
    for i in x:
        if i == "a":
            count += 1


print("Number of 'a' in the list:", count)
