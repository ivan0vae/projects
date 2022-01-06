X = int(input("Сколько билетов вы хотите приобрести?\n"))
price = []
for i in range(1, X + 1):
    age = int(input(f"Возраст {i} участника?\n"))
    if age < 18:
        price.append(0)
    if 18 <= age < 25:
        price.append(990)
    if age >= 25:
        price.append(1390)

if X > 3:
    print("Сумма к оплате с учетом скидки: ", sum(price) * 0.9,
          "рублей")  # параметр sum(price)*0.9 - это сумма билетов с учетом скидки 10%
else:
    print("Сумма к оплате: ", sum(price), "рублей")
