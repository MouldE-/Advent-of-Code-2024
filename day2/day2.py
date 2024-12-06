# part 1
with open("day2-input", "r") as file:
    print(safe:=len([0 for line in file.read().splitlines() if len(splitLine:=[int(num) for num in line.split()])>1 and len([0 for cur, fut in zip(splitLine[:-1], splitLine[1:]) if (1 if (splitLine[-1] > splitLine[0]) else -3) <= (fut - cur) <= (3 if (splitLine[-1] > splitLine[0]) else -1)]) == len(splitLine)-1]))

# part 2
with open("day2-input", "r") as file:
    for splitLine in [splitLine for line in file.read().splitlines() if len(splitLine:=[int(num) for num in line.split()])>1 and len([0 for cur, fut in zip(splitLine[:-1], splitLine[1:]) if (1 if (splitLine[-1] > splitLine[0]) else -3) <= (fut - cur) <= (3 if (splitLine[-1] > splitLine[0]) else -1)]) != len(splitLine)-1]:
        for splitLineCopy in [(splitLine[:i] + splitLine[i+1:]) for i in range(len(splitLine))]:
            if len([0 for cur, fut in zip(splitLineCopy[:-1], splitLineCopy[1:]) if (1 if (splitLineCopy[-1] > splitLineCopy[0]) else -3) <= (fut - cur) <= (3 if (splitLineCopy[-1] > splitLineCopy[0]) else -1)]) == len(splitLineCopy)-1:
                safe += 1
                break
print(safe)
