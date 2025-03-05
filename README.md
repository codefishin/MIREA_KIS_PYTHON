# Если помогло, оставьте звёздочку на репозитории. (по приколу)

Второй курс, четвёртвый семестр, 2025

### Папки Task на этой странице: Задания из kispython.ru
### Папки Pract на этой странице: Задания из гита заданий true-grue

На сайте для каждого студента разные варианты, из-за этого задания не совпадут, но можете почитать для примера :)
```
https://github.com/true-grue/kispython
```
# Строка, которая позволяет выводить число с приблизительностью, как на kispython.ru
```
from decimal import Decimal

print(f"{Decimal(FUNCTION()):.2E}")  # Вместо FUNCTION() вводите что хотите
```
# Основы PEP8, за которыми стоит следить
### Ссылка на гайд по PEP8
```
https://peps.python.org/pep-0008/
```
### Следите за запятыми
Пример ошибки:
```
def main(x,y):
  # нету пробела разделяющий запятую и y

```
Правильный пример:
```
def main(x, y):

```
### EOF не содержит пустой строки
Пример ошибки
```
def main():
  # ... code, no EOF
```
Правильный пример
```
def main():
  # ... code
# EOF here, просто Enter лишний раз нажимайте в конце

```
### Строка привысила 79 символов
Пример ошибки:
```
def main():
  return 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 # тут слишком много символов

```
Правильный пример:
```
def main():
  return 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
# тот же самый return, но раздробленный.

```
### Расписывайте параметры правильно
Пример ошибки:
```
def func(Var1, Var2, Var3
  Var4):
  # ...

```
Правильный пример:
```
def func(
    Var1, Var2
    Var3, Var4):
  # Должны быть на одном уровне

```
### Перенос строки операторов
Пример ошибки:
```
def func(x, y):
  return x +
    y

```
Правильный пример:
```
def func(x, y):
  return x
  + y

```
### Интеграция библиотек
Пример ошибки:
```
import math, os
# ...
```
Правильный пример:
```
import math
import os
# ...

```
Но также правильно:
```
from subprocess import Popen, PIPE
# ...

```
### Пишите 2 enter после import / функций
Пример ошибки:
```
import math
def main():
  # ...
def func():
```
Правильный пример:
```
import math


def main():
  # ...


def func():

```
# P.S.
### В коде иногда будет прописано точное возвращение (как в C++). Это не влияет на PEP8
Про что речь:
```
def funcInt(x: int) -> int: # Строго возвращает целочисленную переменную
  # code...
def funcAny(x): # возвращает что попало
  # code...

```
