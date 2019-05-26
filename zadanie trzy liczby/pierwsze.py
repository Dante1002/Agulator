#! /usr/bin/env python
# -*- coding: UTF-8 -*-
1
# ~/python/01_if.py

op = "t"
while op == "t":
    a, b, c = input("Podaj trzy liczby oddzielone spacjami i przecinkami: ").split(" ")

    print("Wprowadzono liczby:", a, b, c,)
    print("\n Najmniejsza: ")

    if a < b:
        if a < c:
            print(a)
        else:
            print(c)
    elif b < c:
        print(b)1
    else:
        print(c)

    op = input("Jeszcze raz (t/n)? ")

print("By, by...")