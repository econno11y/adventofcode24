left_list = []
right_list = []

with open("day_1/inputs.txt", "r") as file:
    for line in file:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))
        
total = sum(abs(left - right) for left, right in zip(sorted(left_list), sorted(right_list)))
print(total)