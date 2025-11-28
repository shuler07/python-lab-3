# (Rus) Лабораторная работа #3
Мини-пакет алгоритмов, включающий в себя рекурсивные и итеративные функции факториала и фибоначи, сортировки (пузырьковая, быстрая, подсчетом, поразрядная, блочная, пирамидальная), структуры хипа и стека на списках, кастомные генераторы числовых списков, бенчмарки выполнения функции, функций сортировок. Поддержка CLI через typer

## Реализованный функционал через typer
1. fibonacci {n: int} {--type: iter / recurs}
2. factorial {n: int} {--type: iter / recurs}
3. sort {a: list[int]} {--type: bubble / quick / counting / radix / bucket / heap} {--reverse: int}

## Структура проекта

<pre>
    .
    ├── practice/                          # Практические задачи написания сортировок, структур и алгоритмов
    ├── src/                               # Исходный код  
    │   ├── app.py                         # Команды CLI
    │   ├── benchmarks.py                  # Функции бенчмарка функции, бенчмарка сортировок
    │   ├── factorial.py                   # Функция итеративного и рекурсивного факториала
    │   ├── fibonacci.py                   # Функция итеративного и рекурсивного фибоначи
    │   ├── generators.py                  # Функции генерации случайных списков чисел
    │   ├── heap.py                        # Класс структуры хипа
    │   ├── sort.py                        # Функции сортировок
    │   ├── stack.py                       # Класс структуры стэка
    │   ├── validation.py                  # Функции валидации списков
    │   ├── errors.py                      # Сообщения об ошибках
    │   ├── main.py                        # Точка входа
    ├── tests/                             # Тесты
    │   ├── test_factorial.py              # Тесты функций факториала
    │   ├── test_fibonacci.py              # Тесты функций фибоначи
    │   ├── test_sort.py                   # Тесты функций сортировок
    ├── uv.lock                            # Зависимости проекта
    ├── .gitignore                         # .gitignore файл
    ├──.pre-commit-config.yaml             # Средства автоматизации проверки кодстайла
    ├── README.md                          # Описание проекта, этот файл
</pre>

## Бенчмарки сортировок на различных входных данных
|             List name              |     bubble     |     quick      |    counting    |     radix      |     bucket     |      heap      |
|------------------------------------|----------------|----------------|----------------|----------------|----------------|----------------|
|     int, 10\**3 (-10\**5, 10\**5)     |    0.08923s    |    0.00207s    |    0.03114s    |    0.00126s    |    0.00365s    |    0.00525s    |
|       int, 10\**3 (-100, 100)       |    0.10071s    |    0.00212s    |    0.00037s    |    0.0006s     |    0.00264s    |    0.00569s    |
|int, 10\**3 (-10\**5, 10\**5), distinct|    0.09157s    |    0.00236s    |    0.04545s    |    0.0008s     |    0.00389s    |    0.00636s    |
|float, 10\**3 (-10\**5, 10\**5)           |    0.11567s    |    0.00372s    |   unsupported  |   unsupported  |  0.00422s    |    0.00533s    |

## Как использовать
Импортируйте в проект нужные функции из модулей в src/
Или используйте команды CLI

# (Eng) Lab #3
A mini-package of algorithms, including recursive and iterative factorial and Fibonacci functions, sorts (bubble, quick, counting, radix, bucket, heap), heap and stack structures on lists, custom numeric list generators, function execution benchmarks, and sorting functions. CLI support via typer

## Implemented functionality via typer
1. fibonacci {n: int} {--type: iter / recurs}
2. factorial {n: int} {--type: iter / recurs}
3. sort {a: list[int]} {--type: bubble / quick / counting / radix / bucket / heap} {--reverse: int}

## Project Structure

<pre>
    .
    ├── practice/                          # Practical tasks of writing sorting methods, structures and algorithmes
    ├── src/                               # Source code
    │     ├── app.py                       # CLI commands
    │     ├── benchmarks.py                # Functions for benchmarking functions, sorting benchmark
    │     ├── factorial.py                 # Iterative and recursive factorial function
    │     ├── fibonacci.py                 # Iterative and recursive Fibonacci function
    │     ├── generators.py                # Functions for generating random lists of numbers
    │     ├── heap.py                      # Heap structure class
    │     ├── sort.py                      # Sorting functions
    │     ├── stack.py                     # Structure class stack
    │     ├── validation.py                # List validation functions
    │     ├── errors.py                    # Error messages
    │     ├── main.py                      # Entry point
    ├── tests/                             # Tests
    │     ├── test_factorial.py            # Factorial function tests
    │     ├── test_fibonacci.py            # Fibonacci function tests
    │     ├── test_sort.py                 # Sorting function tests
    ├── uv.lock                            # Project dependencies
    ├── .gitignore                         # .gitignore file
    ├──.pre-commit-config.yaml             # Automation tools Codestyle checks
    ├── README.md                          # Project description, this file
</pre>

## Sorting benchmarks on various input data
|             List name              |     bubble     |     quick      |    counting    |     radix      |     bucket     |      heap      |
|------------------------------------|----------------|----------------|----------------|----------------|----------------|----------------|
|     int, 10\**3 (-10\**5, 10\**5)     |    0.08923s    |    0.00207s    |    0.03114s    |    0.00126s    |    0.00365s    |    0.00525s    |
|       int, 10\**3 (-100, 100)       |    0.10071s    |    0.00212s    |    0.00037s    |    0.0006s     |    0.00264s    |    0.00569s    |
|int, 10\**3 (-10\**5, 10\**5), distinct|    0.09157s    |    0.00236s    |    0.04545s    |    0.0008s     |    0.00389s    |    0.00636s    |
|float, 10\**3 (-10\**5, 10\**5)           |    0.11567s    |    0.00372s    |   unsupported  |   unsupported  |  0.00422s    |    0.00533s    |

## How to use
Import the required functions from modules in src/ into the project
Or use CLI commands
