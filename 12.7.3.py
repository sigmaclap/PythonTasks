per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму, которую вы хотите положить под проценты: ")
deposit = []
perCentList = list(map(float, per_cent.values()))
sumValue = 0
for i in perCentList:
    sumValue += float(money) * i / 100
    deposit.append(int((sumValue)))
    sumValue = 0
print(deposit)
print("Максимальная сумма, которую вы можете заработать - ", max(deposit))
