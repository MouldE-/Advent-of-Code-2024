# part 1
rules:dict[str, str] = {}
manuals:list[str] = []

def isValid(pages:list[str]) -> bool:
    for i in range(len(pages)):
        if rules.get(pages[i]) == None:
            continue
        for j in range(i):
            if pages[j] in rules[pages[i]]:
                return False
    return True

def reorder(pages:list[str]):
    for i in range(len(pages)):
        if rules.get(pages[i]) == None:
            continue
        for j in range(i):
            if pages[j] in rules[pages[i]]:
                pages.insert(j, pages.pop(i))

with open("day5-input", "r") as file:
    while (line := file.readline()) != "\n":
        key, value = line[:-1].split("|")
        rules[key] = rules.get(key, []) + [value]
    manuals = file.readlines()

print(sum([int(pages[len(pages)//2]) for pages in [manual.strip("\n").split(",") for manual in manuals] if isValid(pages)]))

# part 2
print(sum([int(pages[len(pages)//2]) for pages in [manual.strip("\n").split(",") for manual in manuals] if not isValid(pages) and reorder(pages) == None]))

