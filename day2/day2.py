# part 1
with open("day2-input", "r") as file:
    print(sum([1 for line in file.read().splitlines() if len(splitLine:=[int(num) for num in line.split()])>1 and len([0 for cur, fut in zip(splitLine[:-1], splitLine[1:]) if (1 if (splitLine[-1] > splitLine[0]) else -3) <= (fut - cur) <= (3 if (splitLine[-1] > splitLine[0]) else -1)]) == len(splitLine)-1]))
