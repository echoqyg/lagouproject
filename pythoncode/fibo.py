#!/usr/bin/env python
# encoding: utf-8

# Fibonacci numbers module


def fib(n):  # write Fibonacci series up to n
    """result None"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def fib3():  # write Fibonacci series up to 500
    """result None"""
    a, b = 0, 1
    while a < 500:
        print(a, end=' ')
        a, b = b, a + b
    print()
