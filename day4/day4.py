# part 1
with open("day4-input", "r") as file:
    wordsearch = file.readlines()

SEARCH = "XMAS"
count = 0

def search(i:int, j:int, down:int, right:int) -> int:
    if (i < len(SEARCH)-1 and down == -1) or (i > len(wordsearch)-len(SEARCH) and down == 1) or (j < len(SEARCH)-1 and right == -1) or (j > len(wordsearch)-len(SEARCH) and right == 1):
        return 0
    for k in range(1, len(SEARCH)):
        if wordsearch[i+k*down][j+k*right] != SEARCH[k]:
            return 0
    return 1

for i in range(len(wordsearch)):
    for j in range(len(wordsearch[i])):
        if (wordsearch[i][j] != "X"):
            continue
        for k in range(-1, 2):
            for l in range(-1, 2):
                count += search(i, j, k, l)
print(count)

# part 2
SEARCH = "MAS"
count = 0
for i in range(len(wordsearch) - 2):
    for j in range(len(wordsearch[0]) - 3):
        s1 = "".join([wordsearch[i][j], wordsearch[i+1][j+1], wordsearch[i+2][j+2]])
        s2 = "".join([wordsearch[i+2][j], wordsearch[i+1][j+1], wordsearch[i][j+2]])
        if (s1 == SEARCH or s1 == SEARCH[::-1]) and (s2 == SEARCH or s2 == SEARCH[::-1]):
            count += 1
print(count)
