shape_scores = {"X": 1, "Y": 2, "Z": 3}  # X - Камінь (1), Y - Папір (2), Z - Ножиці (3)


outcomes = {
    "A X": 3,  # Камінь vs Камінь - нічия
    "A Y": 6,  # Камінь vs Папір - перемога
    "A Z": 0,  # Камінь vs Ножиці - програш
    "B X": 0,  # Папір vs Камінь - програш
    "B Y": 3,  # Папір vs Папір - нічия
    "B Z": 6,  # Папір vs Ножиці - перемога
    "C X": 6,  # Ножиці vs Камінь - перемога
    "C Y": 0,  # Ножиці vs Папір - програш
    "C Z": 3   # Ножиці vs Ножиці - нічия
}


total_score = 0
try:
    with open("strategy_guide.txt", "r") as file:
        strategy_guide = file.readlines()
    
 
    for line in strategy_guide:
        line = line.strip()  
        if line:  
            opponent, you = line.split(" ")
         
            round_score = shape_scores[you] + outcomes[f"{opponent} {you}"]
            total_score += round_score

    print(f"Загальна сума очок: {total_score}")

except FileNotFoundError:
    print("Помилка: Файл 'strategy_guide.txt' не знайдено. Переконайтеся, що файл існує в цій директорії.")
except Exception as e:
    print(f"Виникла помилка: {e}")