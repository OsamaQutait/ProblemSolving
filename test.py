
characters = {")": [1,2,5],
              "}": [1,2,5],
              "]": "["}
print(characters[")"])
print(list(characters["}"]))
characters["}"] = list(list(characters["}"])) + [66]
print(characters["}"])

print("a")
print(list("a"))

