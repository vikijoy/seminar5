# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


def func(file_path: str):
    a, b, c = '\\'.join(file_path.split('\\')[:-1]), \
        file_path.split('\\')[-1].split('.')[0], \
        file_path.split('\\')[-1].split('.')[1]
    return a, b, c

res = func(input('Введите путь до файла: '))
print(res)


# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии


def func(names: list[str], bets: list[int], bonus: list[str]) -> dict[str:int]:
    return {name: bet / 100 * float(bon) for name, bet, bon in
            zip(names, bets, map(lambda x: x.replace('%', ''), bonus))}


# Создайте функцию генератор чисел Фибоначчи
from collections.abc import Generator


def func(n: int) -> Generator[int]:
    fib_1, fib_2 = 0, 1
    for x in range(n):
        yield fib_2
        fib_1, fib_2 = fib_2, fib_1 + fib_2


for x in func(int(input('Введите число Фибоначчи: '))):
    print(x)
