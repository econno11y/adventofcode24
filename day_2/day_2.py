from utils.get_inputs import inputs

lines = inputs(2)

list_of_levels = []

for line in lines:
    level = line.split()
    list_of_levels.append([int(number) for number in level])
    

def is_safe(level):
    i = len(level) - 1
    while i > 0:
        distance = abs(int(level[i]) - int(level[i - 1]))
        # is distance between 1 and 3?
        if distance < 1 or distance > 3:
            return False
        # are i and next two neighbors consecutive?
        if i > 1:
            if level[i] < level[i - 2]:  # decreasing
                if level[i] > level[i - 1]:  # increasing
                    return False
                if level[i - 1] > level[i - 2]:  # increasing
                    return False
            else:  # increasing
                if level[i] < level[i - 1]:  # decreasing
                    return False
                if level[i - 1] < level[i - 2]:  # decreasing
                    return False
                
        i -= 1
    return True


safe_reports = sum(is_safe(level) for level in list_of_levels)
        
print(safe_reports)
    

