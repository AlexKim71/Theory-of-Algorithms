def quicksort_recursive(a, l, r):
    """Рекурсивна реалізація QuickSort (схема Хоара)."""
    total_comparisons = 0
    total_assignments = 0
    
    # Базовий випадок: якщо підмасив має 0 або 1 елемент
    if l >= r:
        return 0, 0, 0
    
    total_recursive_calls = 1 # Рахуємо поточний виклик

    # 1. Розбиття масиву
    q, c1, a1 = partition_hoare_original(a, l, r)
    total_comparisons += c1
    total_assignments += a1
        
    # 2. Рекурсивні виклики: [l, q] та [q + 1, r]
    c2, a2, r2 = quicksort_recursive(a, l, q)
    c3, a3, r3 = quicksort_recursive(a, q + 1, r)
        
    total_comparisons += c2 + c3
    total_assignments += a2 + a3
    total_recursive_calls += r2 + r3
        
    return total_comparisons, total_assignments, total_recursive_calls

def partition_hoare_original(a, l, r):
    """Функція розділення за схемою Хоара. Півот = a[l]."""
    comparisons = 0
    assignments = 0
    
    pivot = a[l]
    assignments += 1
    
    i = l - 1
    j = r + 1
    assignments += 2
    
    while True:
        # Рух i вправо (шукаємо a[i] >= pivot)
        i += 1; assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1; assignments += 1
        comparisons += 1  # Порівняння, що завершило цикл

        # Рух j вліво (шукаємо a[j] <= pivot)
        j -= 1; assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1; assignments += 1
        comparisons += 1  # Порівняння, що завершило цикл
        
        # Перевірка на перетин
        comparisons += 1
        if i >= j:
            return j, comparisons, assignments # Повертаємо індекс розділу j
            
        # Обмін a[i] та a[j] (3 присвоєння)
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        assignments += 3

# --- Блок виконання ---
try:
    input_str = input("Введіть елементи масиву через кому: ")
    my_list_rec = [int(x.strip()) for x in input_str.split(',')]
    
    if not my_list_rec:
        print("Масив порожній.")
    else:
        print("\n--- РЕКУРСИВНЕ ШВИДКЕ СОРТУВАННЯ (схема Хоара) ---")
        print(f"Оригінальний список: {my_list_rec}")

        list_copy = my_list_rec.copy()

        total_comps, total_assigs, total_calls = quicksort_recursive(list_copy, 0, len(list_copy) - 1)

        print(f"Відсортований список: {list_copy}")
        print(f"Загальна кількість порівнянь: {total_comps}")
        print(f"Загальна кількість присвоювань: {total_assigs}")
        print(f"Загальна кількість рекурсивних викликів: {total_calls}")

except ValueError:
    print("\nПомилка: Некоректний формат введених даних.")
except Exception:
    print(f"\nВиникла непередбачувана помилка.")
