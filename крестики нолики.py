def печать_доски(доска):
    for строка in доска:
        print(" | ".join(строка))
        print("-" * 9)
def проверить_победу(доска, символ):

    for i in range(3):
        if all(доска[i][j] == символ for j in range(3)) or all(доска[j][i] == символ for j in range(3)):
            return True
    
    if all(доска[i][i] == символ for i in range(3)) or all(доска[i][2 - i] == символ for i in range(3)):
        return True
    return False

def игра():
    доска = [[" " for _ in range(3)] for _ in range(3)]
    текущий_игрок = "X"

    while True:
        печать_доски(доска)
        ход = input(f"Игрок {текущий_игрок}, введите координаты в формате 'строка, столбец': ")
        строка, столбец = map(int, ход.split(","))

        if доска[строка][столбец] == " ":
            доска[строка][столбец] = текущий_игрок
        else:
            print("Эта ячейка уже занята. Попробуйте ещё раз.")
            continue

        if проверить_победу(доска, текущий_игрок):
            печать_доски(доска)
            print(f"Игрок {текущий_игрок} победил!")
            break

        if all(доска[i][j] != " " for i in range(3) for j in range(3)):
            печать_доски(доска)
            print("Ничья!")
            break

        текущий_игрок = "O" if текущий_игрок == "X" else "X"

if __name__ == "__main__":
    игра()