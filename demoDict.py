#demoDict.py

colors = {"apple":"red", "banana":"yellow"}
print(len(colors))

colors["cherry"] = "red"
colors["apple"] = "green"
print(colors)

del colors["apple"]

for item in colors.items():
    print(item)

print(colors["banana"])