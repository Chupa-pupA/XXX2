import random


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


computer_choices = ["A", "B", "C"]


total_score = 0
round_number = 0

print("Граємо в Камінь, Папір, Ножиці!")
print("Вводь: X (Камінь), Y (Папір), Z (Ножиці). Для завершення введи 'stop'.")

while True:
    user_choice = input("Твій вибір (X/Y/Z або 'stop'): ").upper()
    
    if user_choice == "STOP":
        break
    
    if user_choice not in shape_scores:
        print("Неправильний вибір! Введи X, Y або Z.")
        continue
    
    computer_choice = random.choice(computer_choices)
    round_number += 1
    
    round_key = f"{computer_choice} {user_choice}"
    shape_score = shape_scores[user_choice]
    outcome_score = outcomes[round_key]
    round_score = shape_score + outcome_score
    
    total_score += round_score
    
    print(f"\nРаунд {round_number}:")
    print(f"Комп'ютер вибрав: {computer_choice}")
    print(f"Ти вибрав: {user_choice}")
    print(f"Результат: {'Ти виграв!' if outcome_score == 6 else 'Нічия!' if outcome_score == 3 else 'Ти програв!'}")
    print(f"Очки за раунд: {shape_score} (фігура) + {outcome_score} (результат) = {round_score}")
    print(f"Загальні очки: {total_score}")

print(f"\nГра завершена! Твій підсумковий результат: {total_score} очок за {round_number} раундів.")