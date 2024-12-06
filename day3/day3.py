# part 1
import re
with open("day3-input", "r") as file:
    print(sum(int(hit[0])*int(hit[1]) for hit in re.findall("mul\(([0-9]*),([0-9]*)\)", file.read())))
