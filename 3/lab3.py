
def get_calibration_number(text):
   
    numbers = [char for char in text if char.isnumeric()]
    
    if not numbers:
        return 0
    
    first_digit = numbers[0]
    last_digit = numbers[-1]
    
    return int(first_digit + last_digit)

def calculate_total_calibration(file_name):
   
    result = 0
    
    with open(file_name, 'r') as file:
        for line in file:
            cleaned_line = line.strip()
            calibration_number = get_calibration_number(cleaned_line)
            result += calibration_number
    
    return result


input_file = 'input_3.txt'


total_calibration = calculate_total_calibration(input_file)
print(f"Загальна сума калібрувальних значень: {total_calibration}")