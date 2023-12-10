money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0  # Счетчик месяцев
budget = money_capital + salary  # Первоначальный бюджет

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while budget - spend > 0:
    if count != 0:
        spend *= (1 + increase)
    budget = budget + salary - spend
    count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count)
