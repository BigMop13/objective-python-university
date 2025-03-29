import math
import random

def multiply_numbers():
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    product = num1 * num2

    return product


def is_odd():
    num1 = float(input("Podaj liczbę: "))

    if num1 % 2 == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieparzysta")

    return num1

def sum_of_numbers():
    num1 = input("Podaj jedną liczbę: ")
    sum_numbers = 0

    for i in range(1, int(num1) + 1):
        sum_numbers += i ** 2

    return sum_numbers

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def least_common_multiple(a, b):
    return abs(a * b) // math.gcd(a, b)

def factorial_iterative(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]

def cumulative_sums(*args):
    sums = []
    current_sum = 0
    for num in args:
        current_sum += num
        sums.append(current_sum)
    return sums

def arithmetic_sum(*args):
    current_sum = 0
    count_elements = len(args)
    for num in args:
        current_sum += num

    return current_sum / count_elements

def reverse_string(s):
    return s[::-1]

def count_case(s):
    upper, lower = 0, 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return {'upper': upper, 'lower': lower}

def unique_elements(arr):
    return list(set(arr))

def character_frequencies(s):
    frequencies = {}
    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies

def split_into_words(s):
    return s.split()

def to_camel_case(s):
    words = s.split()
    return words[0] + ''.join(word.capitalize() for word in words[1:])

def from_camel_case(s):
    return ''.join(' ' + char if char.isupper() else char for char in s).lower()

def babylonian_sqrt(n):
    x = n
    y = (x + 1) / 2
    while y < x:
        x = y
        y = (x + n / x) / 2
    return x

def estimate_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            inside_circle += 1
    return 4 * inside_circle / num_samples

def zip_lists(a, b):
    return list(zip(a, b))

def filter_numbers():
    return [i for i in range(100) if i % 3 == 0 and i % 5 != 0]
