#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test():
    """
    Определить число.
    """
    x = int(input("Число? "))
    if x < 0:
        negative()
    if x > 0:
        positive()


def negative():
    """
    Дать ответ.
    """
    print("Отрицательный")


def positive():
    """
    Дать ответ.
    """
    print("Положительный")


if __name__ == '__main__':
    test()
