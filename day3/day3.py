# part 1
import re
with open("day3-input", "r") as file:
    print(sum(int(hit[0])*int(hit[1]) for hit in re.findall("mul\(([0-9]*),([0-9]*)\)", file.read())))

# part 2
count = 0
with open("day3-input", "r") as file:
    enabled = True
    for hit in re.findall("mul\([0-9]*,[0-9]*\)|don't\(\)|do\(\)", file.read()):
        hit = hit.strip("/")
        if hit == "do()":
            enabled = True
        elif hit == "don't()":
            enabled = False
        else:
            match = re.findall("mul\(([0-9]*),([0-9]*)\)", hit)[0]
            if enabled:
                count += int(match[0]) * int(match[1])
print(count)
