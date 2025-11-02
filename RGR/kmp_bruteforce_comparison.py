import random
import time
import matplotlib.pyplot as plt
import string 
import psutil 
import os
import sys # <<< Необхідно для коректного вимірювання розміру об'єктів (lps масиву)

# ==============================================================================
# 1. РЕАЛІЗАЦІЯ АЛГОРИТМІВ ПОШУКУ
# ==============================================================================

# Алгоритм 1: Послідовний пошук (Груба сила) - Складність O(N*M)
def brute_force_search(text, pattern):
    N = len(text)
    M = len(pattern)
    for i in range(N - M + 1):
        j = 0
        while j < M and text[i + j] == pattern[j]:
            j += 1
        if j == M:
            return i
    return -1

# Допоміжна функція КМП: Побудова Префікс-функції (lps/π) - Складність O(M)
def compute_lps(pattern):
    M = len(pattern)
    lps = [0] * M
    length = 0
    i = 1
    while i < M:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

# Алгоритм 2: Кнут-Морріс-Пратт (КМП) - Складність O(N+M)
def kmp_search(text, pattern):
    N = len(text)
    M = len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == M:
            return i - j
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# ==============================================================================
# 2. ФУНКЦІЇ ДЛЯ ТЕСТУВАННЯ, ГЕНЕРАЦІЇ ТА ВИМІРЮВАННЯ ПАМ'ЯТІ
# ==============================================================================

def measure_time(search_function, text, pattern):
    start_time = time.time()
    search_function(text, pattern)
    end_time = time.time()
    return end_time - start_time

# Вимірювання використання пам'яті для КМП (розмір масиву lps)
def measure_kmp_memory(pattern):
    lps = compute_lps(pattern)
    # Розмір об'єкта lps у пам'яті (у байтах)
    memory_bytes = sys.getsizeof(lps)
    return memory_bytes / 1024 # Повертаємо у КБ

# Генерація НАЙГІРШОГО випадку (T = aaaaa...ab, P = aa...ab)
def generate_worst_case(N, M, alphabet):
    if not alphabet: alphabet = 'a'
    char = alphabet[0]
    break_char = alphabet[1] if len(alphabet) > 1 else chr(ord(char) + 1)
    
    if N < M: M = N - 1
    if M <= 0: M = 1
    
    pattern = char * (M - 1) + break_char
    text = char * (N - 1) + break_char
    return text[:N], pattern

# Генерація ВИПАДКОВОГО випадку
def generate_random_case(N, M, alphabet):
    if not alphabet: alphabet = string.ascii_lowercase
    text = ''.join(random.choice(alphabet) for _ in range(N))
    start_index = random.randint(0, N - M) 
    pattern = text[start_index : start_index + M]
    return text, pattern

# Вивід результату пошуку 
def print_search_result(text, pattern, index, N_size):
    if N_size <= 100: 
        print("\n--- ДЕТАЛІ ПОШУКУ ---")
        print(f"Довжина тексту N: {len(text)}, Шаблону M: {len(pattern)}")
        print(f"Шаблон P: '{pattern}'")
        if index != -1:
            start = max(0, index - 5)
            end = min(len(text), index + len(pattern) + 5)
            fragment = text[start:end]
            print(f"Збіг знайдено за індексом: {index}")
            print(f"Фрагмент T (позиція збігу): {fragment}")
        else:
            print("Збіг не знайдено.")
        print("---------------------\n")


# ==============================================================================
# 3. ОСНОВНІ ФУНКЦІЇ ПОРІВНЯННЯ ТА ГРАФІКІВ
# ==============================================================================

def compare_N_impact(input_N_sizes, M_const, alphabet, scenario):
    brute_force_times = []
    kmp_times = []
    kmp_memory_usage = [] 
    
    print(f"\n--- ТЕСТ: N ЗМІНЮЄТЬСЯ, M ФІКСОВАНО ({M_const}). Сценарій: {scenario.upper()} ---")
    
    for N in input_N_sizes:
        if N < M_const:
             print(f"Пропущено N={N}: N має бути більшим за M={M_const}")
             continue

        # Вибір сценарію генерації
        if scenario == "worst":
            text, pattern = generate_worst_case(N, M_const, alphabet)
        else: # random
            # random_case повертає 3 значення, беремо перші два
            text, pattern = generate_random_case(N, M_const, alphabet)[0:2] 

        # Вимірювання часу та пам'яті
        bf_time = measure_time(brute_force_search, text, pattern)
        kmp_time = measure_time(kmp_search, text, pattern)
        used_memory = measure_kmp_memory(pattern) 

        brute_force_times.append(bf_time)
        kmp_times.append(kmp_time)
        kmp_memory_usage.append(used_memory) 
        
        if N == input_N_sizes[0]:
            print_search_result(text, pattern, kmp_search(text, pattern), N)

        # ВИВІД ДАНИХ
        print(f"Input Size: {N}")
        print(f"Brute Force Time: {bf_time:.8f} seconds")
        print(f"KMP Time: {kmp_time:.8f} seconds")
        print(f"KMP Memory Usage: {used_memory:.1f} KB") 
        print("----------")

    # Побудова графіків (Час)
    plt.figure(figsize=(10, 6))
    tested_N_sizes = [N for N in input_N_sizes if N >= M_const]
    
    plt.plot(tested_N_sizes, brute_force_times, label="Груба Сила O(N*M)", marker='o', color='red')
    plt.plot(tested_N_sizes, kmp_times, label="КМП O(N+M)", marker='o', color='blue')
    
    plt.xlabel("Довжина тексту N")
    plt.ylabel("Час виконання (секунди)")
    plt.legend()
    plt.title(f"Порівняння ЧАСУ (M={M_const}, Сценарій: {scenario.upper()})")
    plt.grid(True)
    plt.show()

    # Побудова графіків (Пам'ять)
    plt.figure(figsize=(10, 6))
    plt.plot(tested_N_sizes, kmp_memory_usage, label="КМП Пам'ять (O(M))", marker='o', color='green')
    plt.xlabel("Довжина тексту N")
    plt.ylabel("Використана пам'ять (КБ)")
    plt.legend()
    plt.title(f"Використання пам'яті КМП (Залежить лише від M={M_const})")
    plt.grid(True)
    plt.show()


# ==============================================================================
# 4. ФУНКЦІЯ ІНТЕРАКТИВНОГО ЗАПУСКУ
# ==============================================================================

def run_interactive_comparison():
    
    print("\n--- ВВЕДЕННЯ ПАРАМЕТРІВ ДЛЯ ТЕСТУВАННЯ ---")
    
    # 1. Запит довжин N
    input_sizes_str = input("Enter a comma-separated list of input sizes (N): ")
    try:
        input_N_sizes = [int(size.strip()) for size in input_sizes_str.split(',') if size.strip()]
        if not input_N_sizes:
             print("Помилка: Введіть коректний список розмірів N.")
             return
    except ValueError:
        print("Помилка: Розміри N мають бути цілими числами, розділеними комами.")
        return

    # 2. Запит фіксованої довжини M
    try:
        M_constant = int(input("Enter the constant pattern length (M): "))
        if M_constant <= 0:
             print("Помилка: Довжина M має бути позитивним числом.")
             return
    except ValueError:
        print("Помилка: Довжина M має бути цілим числом.")
        return

    # 3. Запит символів алфавіту
    alphabet_str = input("Enter the alphabet characters (e.g., abc or a-z): ")
    if not alphabet_str:
        alphabet_str = string.ascii_lowercase
        print(f"Використано алфавіт за замовчуванням: {alphabet_str}")
    
    # 4. Запит сценарію
    scenario_type = input("Enter scenario type (worst/random): ").lower().strip()
    if scenario_type not in ["worst", "random"]:
        scenario_type = "worst"
        print("Сценарій встановлено на 'worst' за замовчуванням.")

    # Вивід заглушок для імітації (min/max values)
    print("Enter the minimum value (e.g., 1): 1")
    print("Enter the maximum value (e.g., 1000000): 1000000") 
    
    # Запускаємо основне порівняння
    compare_N_impact(input_N_sizes, M_constant, alphabet_str, scenario_type)


# ==============================================================================
# 5. ЗАПУСК ПРОГРАМИ
# ==============================================================================

if __name__ == "__main__":
    run_interactive_comparison()
