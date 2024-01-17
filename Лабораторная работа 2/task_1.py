money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months = 0
while True:
    diff = spend - salary
    if diff > money_capital:
        break

    months += 1
    spend *= 1 + increase
    money_capital -= diff

print("Количество месяцев, которое можно протянуть без долгов:", months)
