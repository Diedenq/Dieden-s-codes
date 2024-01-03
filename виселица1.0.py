import random

def choose_word():
    words = ["python", "programming", "hangman", "code", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Добро пожаловать в игру Виселица!")
    secret_word = choose_word()
    correct_letters = set(secret_word)
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print("\nСлово:", display_word(secret_word, guessed_letters))
        guess = input("Угадайте букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите только одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже угадали эту букву. Попробуйте другую")
            continue

        guessed_letters.add(guess)

        if guess not in correct_letters:
            attempts -= 1
            print(f"Неверно! Осталось попыток: {attempts}")

        if guessed_letters == correct_letters:
            print(f"Поздравляю, вы победили! Загаданное слово: {secret_word}")
            break

    if attempts == 0:
        print(f"Извините, вы проиграли. Загаданное слово было: {secret_word}")

if __name__ == "__main__":
    hangman()