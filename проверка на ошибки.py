try:
    x = int(input("Введите число: "))
    result = 10 / x
    print("Результат:", result)

except ValueError:
    print("Ошибка: Введите числовое значение.")

except ZeroDivisionError:
    print("Ошибка: Деление на ноль невозможно.")

except Exception as e:
    print("Произошла ошибка:", e)

else:
    print("Блок try выполнен без ошибок.")

finally:
    print("Этот блок выполнится всегда, независимо от наличия ошибок.")