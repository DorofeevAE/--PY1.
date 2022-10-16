money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
spend_expenses = spend
# Количество
while True:
    spend_expenses = spend_expenses * (1 + increase) ** (month + 1)
    money_capital = money_capital + salary - (spend_expenses * (1 + increase))
    if money_capital < 0:
        break
    month += 1

print(month)