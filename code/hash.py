import string
import random
import sys # Для вычисления размера обьекта в байтах для 3 задачи


def ten_random_chr(k=10):  # Вводим необязательный аргумент на сулай если надо будет выбрать не 10 элементов
    chr_list = list(string.ascii_letters)  # Полчаем строку символов и преобразуем ее в список
    num_list = list(string.digits)
    chr_list.extend(num_list)
    res_list = random.sample(chr_list, k=k)  # Если использовать random.choices то в выборке могут быть повторения
    return res_list


def dict_from_lists(value_list, key_list):
    res = dict()
    if len(value_list) == len(key_list):
        for i in range (len(key_list)): # В цикле каждому элементу списка ключей сопоставляем в словаре значение
            res[key_list[i]] = value_list[i]
    return res


def bytes_universal_hash(num, size):
    num = int(num)
    bytes_size = sys.getsizeof(num)
    str_bytes = num.to_bytes(bytes_size, 'big') # Использем big_endian порядок байт (от старшего к меньшему)
    hash = 0 # Будем считать хеш накопительным итогом по методу Горнера
    for elem in str_bytes:
        base = random.randint(0, size - 1)  # Тк мы высиляем рандомизированный хеш, то основание будет всегда случайным
        hash = (hash * base + elem) % size
    return hash


def gorner_ascii_hash(str, base, size):
    str_bytes = str.encode('ascii')
    hash = 0 # та же схема Горнера
    for elem in str_bytes:
        hash = (hash * base + elem) % size
    return hash


def main():
    print("Задание №1 - ")
    res = ten_random_chr()
    print(res)

    print("\nЗадание №2 - ")
    print("Введите текст из 10 слов (Или любые символы если нужно использовать текст по умолчанию)")
    text = input()
    text_list = text.split()  # Разбиваем текст по пробелам в список
    if len(text_list) != 10: # Если текст не ввели
        text = "Разбейте произвольный текст на слова и поставьте в соответствие каждому"
        print("Будет использован текст - " + text)
        text_list = text.split()
    dict_res = dict_from_lists(text_list, res)
    print("Полученный словарь - ")
    print(dict_res)

    print("\nЗадание №3 - ")
    print("Введите целое число для вычисление рандомизированной хэш-функции побайтно (желательно неск-ко байт)")
    str = input()
    print("Введите размер желаемого словаря (целое число, желательно простое)")
    # В качесте размера словаря выбирают простое число, тк все хеши берутся по его модулю (остаток от деления) и для
    # простого числа остатки деления на него будт повторятся реже чем в случае составного и хеши будут уникальными
    size = int(input())
    print("Рандомизированный побайтный хеш = ", bytes_universal_hash(str, size))

    print("\nЗадание №4 - ")
    print("Введите ascii строку для вычисления ключа методом Горнера")
    str = input()
    print("Введите константное основание (для ascii рекомендуется 127)")
    base = int(input())
    print("Введите размер желаемого словаря (целое число, желательно простое)")
    size = int(input())
    print("Хеш ascii строки по методу Горнера = ", gorner_ascii_hash(str, base, size))


if __name__ == "__main__":
    main()

