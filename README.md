# Имитация воронки
[![License: MIT ](https://img.shields.io/badge/License-MIT-fuchsia.svg)](https://opensource.org/licenses/MIT)
[![Build, Test](https://github.com/Spfeed/rotating-funnel/actions/workflows/ci.yml/badge.svg)](https://github.com/Spfeed/rotating-funnel/actions/workflows/ci.yml)

## Описание задачи

Создайте программу, которая имитирует "воронку". Несколько дисков с разными радиусами, упорядоченными по возрастанию; глубина (расстояние между дисками) и цвет периодически изменяется.

## Иллюстрация работы приложения 
![](https://github.com/Spfeed/rotating-funnel/blob/main/img/funnel.gif)

## Реализовано с помощью:

| Язык        | Среда разработки | 
|-------------|------------------|
| Python 3.11 | PyCharm 2023.1   |

## Используемые библиотеки и наборы инструментов

- `PyOpenGL` для работы с графикой и трехмерной графикой, в том числе для отрисовки воронки.
- `pygame` для инициализации окна, обработки событий графического интерфейса.
- `math` для выполнения математических операций в проекте, таких как вычисление координат точек на диске.

## Установка и запуск
1. Клонируйте репозиторий:
   ```
    git clone https://github.com/Spfeed/rotating-funnel.git
   ```
2. Скачайте [Python](https://www.python.org/);
3.  Перейдите в директорию проекта, введя команду:
    ```
    cd rotating-funnel
    ```
4. Установите необходимые библиотеки, введя команду:
    ```
    pip install -r requirements.txt
    ```
5. Введите команду:
    ```
   python main.py
   ```
