
with open('input_2.txt', 'r') as file:
    lines = file.read().strip().split('\n')

numbers_list = [list(map(int, line.split())) for line in lines]

counter = 0

for numbers in numbers_list:
   
    is_rising = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    is_falling = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))
    
    if not (is_rising or is_falling):
        continue
    valid_gaps = all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))
    if valid_gaps:
        counter += 1

print(counter)