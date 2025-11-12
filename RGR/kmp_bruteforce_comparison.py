import random
import time
import matplotlib.pyplot as plt
import string 
import psutil 
import os
import sys 

# ==============================================================================
# 1. РЕАЛІЗАЦІЯ АЛГОРИТМІВ ПОШУКУ (без змін)
# ==============================================================================
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

def measure_kmp_memory(pattern):
    lps = compute_lps(pattern)
    memory_bytes = sys.getsizeof(lps)
    return memory_bytes / 1024 

def generate_worst_case(N, M, alphabet):
    if not alphabet: alphabet = 'a'
    char = alphabet[0]
    break_char = alphabet[1] if len(alphabet) > 1 else chr(ord(char) + 1)
    
    if N < M: M = N - 1
    if M <= 0: M = 1
    
    prefix = char * (M - 1)
    pattern = prefix + break_char
    text = (char * (N - M)) + pattern 
    
    return text[:N], pattern

def generate_random_case(N, M, alphabet):
    if not alphabet: alphabet = string.ascii_lowercase
    text = ''.join(random.choice(alphabet) for _ in range(N))
    start_index = random.randint(0, N - M) 
    pattern = text[start_index : start_index + M]
    return text, pattern

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
# 3. ОСНОВНА ФУНКЦІЯ ПОРІВНЯННЯ ТА ГРАФІКІВ
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

        if scenario == "worst":
            text, pattern = generate_worst_case(N, M_const, alphabet)
        else:
            text, pattern = generate_random_case(N, M_const, alphabet)[0:2] 

        bf_time = measure_time(brute_force_search, text, pattern)
        kmp_time = measure_time(kmp_search, text, pattern)
        used_memory = measure_kmp_memory(pattern) 

        brute_force_times.append(bf_time)
        kmp_times.append(kmp_time)
        kmp_memory_usage.append(used_memory) 
        
        if N == input_N_sizes[0]:
            print_search_result(text, pattern, kmp_search(text, pattern), N)

        print(f"Input Size: {N}")
        print(f"Brute Force Time: {bf_time:.8f} seconds")
        print(f"KMP Time: {kmp_time:.8f} seconds")
        print(f"KMP Memory Usage: {used_memory:.3f} KB") 
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

    # Побудова графіків (Пам'ять) - O(M) для фіксованого M
    plt.figure(figsize=(10, 6))
    if kmp_memory_usage:
        plt.plot(tested_N_sizes, [kmp_memory_usage[0]] * len(tested_N_sizes), label="КМП Пам'ять (O(M))", linestyle='--', color='green')
    
    plt.xlabel("Довжина тексту N")
    plt.ylabel("Використана пам'ять (КБ)")
    plt.legend()
    plt.title(f"Використання пам'яті КМП (Залежить лише від M={M_const})")
    plt.grid(True)
    plt.show()


# НОВА ФУНКЦІЯ: Звіт O(M) для фінального графіка (викликається, якщо M було списком)
def final_M_impact_plot(M_list, N_const, alphabet, scenario):
    memory_usage_m = []
    brute_force_times = []
    kmp_times = []
    
    for M in M_list:
        if M <= 0 or M >= N_const: continue
        
        text, pattern = generate_worst_case(N_const, M, alphabet) 
        
        used_memory = measure_kmp_memory(pattern) 
        bf_time = measure_time(brute_force_search, text, pattern)
        kmp_time = measure_time(kmp_search, text, pattern)
        
        memory_usage_m.append(used_memory)
        brute_force_times.append(bf_time)
        kmp_times.append(kmp_time)

    tested_M_sizes = [M for M in M_list if 0 < M < N_const]
    
    if not tested_M_sizes: return

    # Фінальний Графік Пам'яті O(M) (Рисунок 7.5)
    plt.figure(figsize=(10, 6))
    plt.plot(tested_M_sizes, memory_usage_m, label="КМП Пам'ять O(M)", marker='o', color='green')
    plt.xlabel("Довжина шаблону M")
    plt.ylabel("Використана пам'ять (КБ)")
    plt.legend()
    plt.title(f"Рисунок 7.5 – Споживання додаткової пам'яті КМП (Залежність від M)")
    plt.grid(True)
    plt.show()

# ==============================================================================
# 4. ФУНКЦІЯ ІНТЕРАКТИВНОГО ЗАПУСКУ (ФІНАЛЬНА ВЕРСІЯ)
# ==============================================================================

def run_interactive_comparison():
    
    print("\n--- ВВЕДЕННЯ ПАРАМЕТРІВ ДЛЯ ТЕСТУВАННЯ ---")
    
    # 1. Запит довжин N 
    input_N_sizes_str = input("Enter a comma-separated list of input sizes (N): ")
    try:
        input_N_sizes = [int(size.strip()) for size in input_N_sizes_str.split(',') if size.strip()]
    except ValueError:
        print("Помилка: Розміри N мають бути цілими числами, розділеними комами.")
        return

    # 2. Запит довжин M 
    M_input_str = input("Enter the constant pattern length (M): ")
    try:
        M_list = [int(m.strip()) for m in M_input_str.split(',') if m.strip()]
        if not M_list:
             print("Помилка: Введіть коректний список довжин M.")
             return
    except ValueError:
        print("Помилка: Довжина M має бути цілим числом або списком чисел через кому.")
        return

    # 3. Інші параметри
    alphabet_str = input("Enter the alphabet characters (e.g., ab): ")
    if not alphabet_str:
        alphabet_str = string.ascii_lowercase
    
    scenario_type = input("Enter scenario type (worst/random): ").lower().strip()
    if scenario_type not in ["worst", "random"]:
        scenario_type = "worst"

    # Вивід заглушок
    print("Enter the minimum value (e.g., 1): 1")
    print("Enter the maximum value (e.g., 1000000): 1000000") 
    
    # Сортуємо N для коректного відображення на графіку
    sorted_N = sorted(input_N_sizes)
    
    # Запускаємо основне порівняння, перебираючи кожен M
    for M_const in M_list:
        if M_const <= 0: continue
        compare_N_impact(sorted_N, M_const, alphabet_str, scenario_type)
        
    # === ФІНАЛЬНИЙ КРОК: БУДУЄМО ГРАФІК O(M), ЯКЩО БУЛО ВВЕДЕНО КІЛЬКА ЗНАЧЕНЬ M ===
    if len(M_list) > 1:
        # Використовуємо найбільше N як константу для тесту M
        N_const_for_M_test = sorted_N[-1]
        final_M_impact_plot(M_list, N_const_for_M_test, alphabet_str, scenario_type)

# ==============================================================================
# 5. ЗАПУСК ПРОГРАМИ
# ==============================================================================

if __name__ == "__main__":
    run_interactive_comparison()
