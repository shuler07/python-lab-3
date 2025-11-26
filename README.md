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

## How to use
Import the required functions from modules in src/ into the project
Or use CLI commands
