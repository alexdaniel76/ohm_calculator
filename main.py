# Калькулятор закона Ома
print('''
         ********************************
         *                              *
         *                              *
         *     Программа для расчета    *
         *                              *
         *         Закона Ома           *
         *                              *
         *         R = U / I            *
         *                              *
         *                              *
         ********************************''')
print('''
            Выберете искомую величину:
                R - 1, U - 2, I - 3  ''')
print()

# Выбор  величины
selectMenu = int(input("Для выхода выберете 4 "))

# Решение формулы
if selectMenu == 1:
    valueVoltage = int(input("Введите величину U (В) = "))
    valueCurrent = int(input("Введите величину I (А) = "))
    valueResistances = valueVoltage / valueCurrent
    print('Отве R (Ом) = ', valueResistances)
elif selectMenu == 2:
    valueVoltage = int(input("Введите величину U (В) = "))
    valueCurrent = int(input("Введите величину I (А) = "))
    valueResistances = valueVoltage / valueCurrent
    print('Ответ R (Ом) = ', valueResistances)
elif selectMenu == 3:
    valueVoltage = int(input("Введите величину U (В) = "))
    valueCurrent = int(input("Введите величину I (А) = "))
    valueResistances = valueVoltage / valueCurrent
    print('Ответ R (Ом) = ', valueResistances)

# Выход из программы
else:
    print("Выбран выход из программы")

    # Для показа термина после расчетов
    print()
    input('Для закрытия нажмите Enter')