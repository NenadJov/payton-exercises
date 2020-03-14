file = open("bear.txt")
content = file.read()
file.close()

#print(content[:90])

with open("bear.txt") as file:
    content = file.read()

#print(content)


def inside_func(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

#print(inside_func('w'))

with open("file.txt", "w") as cont:
    cont.write("snail")

#print(cont)

with open("bear.txt") as file:
    content = file.read()
with open("first.txt", "w") as file:
    file.write(content[:90])

with open("bear1.txt", "r") as file:
    content = file.read()
with open("bear2.txt", "a") as file:
    file.write(content)

with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)
    
#print(content)


