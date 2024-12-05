from utils.get_inputs import inputs
import re

input_lines = inputs(3)

pattern = r"mul\((\d+),(\d+)\)"

total = 0
for line in input_lines:
    match = re.findall(pattern, line)
    if match:
        total += sum(int(x) * int(y) for x, y in match)
        
print(total)