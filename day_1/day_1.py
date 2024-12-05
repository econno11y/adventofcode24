from utils.get_inputs import inputs


lines = inputs(1)
left_list = []
right_list = []
for line in lines:
    left, right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))
        
total = sum(abs(left - right) for left, right in zip(sorted(left_list), 
                                                     sorted(right_list)))
print(total)