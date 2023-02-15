b = int(input("Введите необходимое количество билетов"))
i = 0
sum = 0
while i < b:
    age = int(input("Введите возраст участника"))
    i = i + 1
    if age < 18:
        sum = sum + 0
    elif 18 <= age < 25:
        sum = sum + 990
    elif age >= 25:
        sum = sum + 1390
if b > 3:
    sum = int(sum * 0.9)
print("Сумма к оплате:", sum)

