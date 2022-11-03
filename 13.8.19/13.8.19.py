totalSumTickets = 0
amountTickets = int(input("Сколько билетов вы хотите приобрести? Введите количество: "))
for i in range(amountTickets):
    while True:
        ageI = int(input(f"Сколько лет {i + 1} посетителю: "))
        if 0 < ageI < 18:
            totalSumTickets += 0
            break
        elif 17 < ageI < 26:
            totalSumTickets += 990
            break
        elif ageI > 25:
            totalSumTickets += 1390
            break
        else:
            print("Вы ввели некорректные данные по возрасту, введите их вновь...")
if amountTickets > 3:
    totalSumTickets = totalSumTickets - (totalSumTickets * 10 / 100)
    print(f"Ваша сумма к оплате составляет {totalSumTickets} рублей с учетом скидки 10%.")
else:
    print(f"Ваша сумма к оплате составляет {totalSumTickets} рублей.")

