import random
import time
import matplotlib.pyplot as plt

# ==============================================================================
# 1. РЕАЛІЗАЦІЯ АЛГОРИТМІВ ПОШУКУ
# ==============================================================================

# Алгоритм 1: Послідовний пошук (Груба сила) - Складність O(N*M)
def brute_force_search(text, pattern):
    N = len(text)
    M = len(pattern)
    
    # Ітерація по всіх можливих початкових позиціях
    for i in range(N - M + 1):
        j = 0
        # Порівняння символів
        while j < M and text[i + j] == pattern[j]:
            j += 1
        
        # Знайдено повний збіг
        if j == M:
            return i
            
    return -1

# Допоміжна функція КМП: Побудова Префікс-функції (lps/π) - Складність O(M)
def compute_lps(pattern):
    M = len(pattern)
    lps = [0] * M
    length = 0  # Довжина попереднього найдовшого префікс-суфікса
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
    
    # 1. Попередня обробка
    lps = compute_lps(pattern)
    
    i = 0  # Індекс для тексту
    j = 0  # Індекс для шаблону
    
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
        if j == M:
            # Знайдено збіг
            return i - j
        
        elif i < N and pattern[j] != text[i]:
            # Обробка невідповідності за допомогою lps
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return -1

# ==============================================================================
# 2. ФУНКЦІЇ ДЛЯ ТЕСТУВАННЯ ТА ПОРІВНЯННЯ
# ==============================================================================

# Функція для вимірювання часу виконання
def measure_time(search_function, text, pattern):
    start_time = time.time()
    search_function(text, pattern)
    end_time = time.time()
    return end_time - start_time

# Функція для генерації тестових даних (Найгірший випадок для Грубої сили)
# T = aaaaa...ab, P = aa...ab
def generate_worst_case(N, M, char='a'):
    if N < M:
        raise ValueError("Довжина тексту N має бути більшою за довжину шаблону M.")
    
    # Генеруємо префікс, що повторюється, і додаємо різний останній символ
    prefix = char * (M - 1)
    pattern = prefix + chr(ord(char) + 1)
    text = (char * (N - M + 1)) + pattern[-1] # Створення майже-збігів по всьому тексту
    
    # Для коректного найгіршого випадку:
    text = (prefix + 'c') * (N // M) + text[:N % M] # Простіша генерація, що забезпечує багато порівнянь
    text = 'a' * (N - 1) + 'b'
    pattern = 'a' * (M - 1) + 'b'
    
    return text[:N], pattern

# Основна функція для запуску порівняння та побудови графіків
def compare_search_algorithms(input_N_sizes, M_const):
    brute_force_times = []
    kmp_times = []
    
    print(f"--- Тестування: N змінюється, M фіксовано ({M_const}). Найгірший випадок ---")
    
    for N in input_N_sizes:
        # Генеруємо найгірший випадок (багато майже-збігів)
        text, pattern = generate_worst_case(N, M_const)
        
        # Вимірювання часу
        bf_time = measure_time(brute_force_search, text, pattern)
        kmp_time = measure_time(kmp_search, text, pattern)
        
        brute_force_times.append(bf_time)
        kmp_times.append(kmp_time)
        
        print(f"N={N}: Груба сила: {bf_time:.6f} с, КМП: {kmp_time:.6f} с")

    # Побудова графіків
    plt.figure(figsize=(10, 6))
    plt.plot(input_N_sizes, brute_force_times, label="Груба Сила O(N*M)", marker='o', color='red')
    plt.plot(input_N_sizes, kmp_times, label="КМП O(N+M)", marker='o', color='blue')
    
    plt.xlabel("Довжина тексту N")
    plt.ylabel("Час виконання (секунди)")
    plt.legend()
    plt.title(f"Порівняння алгоритмів пошуку підрядка (M={M_const}, Найгірший випадок)")
    plt.grid(True)
    plt.show()

# ==============================================================================
# 3. ЗАПУСК ПРОГРАМИ
# ==============================================================================

if __name__ == "__main__":
    # Налаштування параметрів для тестування:
    # Довжина тексту N буде змінюватися
    input_N_sizes = [5000, 10000, 20000, 40000, 80000, 160000, 320000]
    
    # Фіксована довжина шаблону M (краще, щоб M було більшим, наприклад 100)
    M_constant = 100 
    
    compare_search_algorithms(input_N_sizes, M_constant)
