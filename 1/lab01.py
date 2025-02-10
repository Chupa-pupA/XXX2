right = []
left = []
with open(r'C:\Users\LS\Documents\IZRAIL\python\2c\input_1.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            left_num = int(parts[0])
            right_num = int(parts[1])
            left.append(left_num)
            right.append(right_num)
left_sorted = sorted(left)
right_sorted = sorted(right)

total = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

print(total)



