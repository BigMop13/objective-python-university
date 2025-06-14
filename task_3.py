import numpy as np
import math
import random
from timeit import timeit

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def compare_performance():
    math_time = timeit(lambda: [math.sin(i) for i in range(10**6)], number=1)
    numpy_time = timeit(lambda: np.sin(np.arange(10**6)), number=1)
    
    list_time = timeit(lambda: [i + 1 for i in range(10**6)], number=1)
    numpy_array_time = timeit(lambda: np.arange(10**6) + 1, number=1)
    
    return {
        'math.sin vs np.sin': (math_time, numpy_time),
        'list vs numpy array': (list_time, numpy_array_time)
    }

def extend_array(arr, new_values):
    return np.append(arr, new_values)

def create_chessboard(size):
    board = np.zeros((size, size), dtype=int)
    board[1::2, ::2] = 1
    board[::2, 1::2] = 1
    return board

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def create_diagonal_matrix(values):
    return np.diag(values)

def reverse_array(arr):
    return np.array(arr).flatten()[::-1]

def select_elements():
    arr = np.arange(1, 101).reshape(10, 10)
    mask = (arr % 2 == 0) & (arr % 3 != 0)
    return arr[mask]

def generate_matrix_with_determinant(size, target_det, min_val=1, max_val=10):
    while True:
        matrix = np.random.randint(min_val, max_val, size=(size, size))
        det = np.linalg.det(matrix)
        if abs(det - target_det) < 0.1:
            return matrix

if __name__ == "__main__":  
    text = "Hello, World!"
    encrypted = caesar_cipher(text, 3)
    print(f"Task 1 - Encrypted text: {encrypted}")
    
    perf_results = compare_performance()
    print("\nTask 2 - Performance comparison:")
    for test, (time1, time2) in perf_results.items():
        print(f"{test}: {time1:.4f} vs {time2:.4f} seconds")
    
    arr = np.array([10, 20, 30])
    extended = extend_array(arr, [40, 50])
    print(f"\nTask 3 - Extended array: {extended}")
    
    chessboard = create_chessboard(4)
    print("\nTask 4 - Chessboard:")
    print(chessboard)
    
    fahrenheit = np.array([0, 12, 45.21, 34, 99.91])
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"\nTask 5 - Celsius temperatures: {celsius}")
    
    diag_matrix = create_diagonal_matrix([4, 5, 6, 7])
    print("\nTask 6 - Diagonal matrix:")
    print(diag_matrix)
    
    input_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    reversed_array = reverse_array(input_array)
    print(f"\nTask 7 - Reversed array: {reversed_array}")
    
    selected = select_elements()
    print("\nTask 8 - Selected elements:")
    print(selected)
    
    matrix = generate_matrix_with_determinant(3, 10)
    print("\nTask 9 - Generated matrix with determinant ≈ 10:")
    print(matrix)
    print(f"Actual determinant: {np.linalg.det(matrix):.2f}")
